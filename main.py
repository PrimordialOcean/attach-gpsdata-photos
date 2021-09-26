import bs4
import csv
import piexif
import math
import pandas as pd
from fractions import Fraction

# sets type alias
NumSexagesimal = tuple[int, int, float, str]
LocSexagesimal = tuple[NumSexagesimal, NumSexagesimal]
GPSExif = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]

# converts gpx format GPS files to csv format files
def convert_gpx_to_csv(gpxfile: str):
    with open(gpxfile, encoding="utf-8") as f:
        soup = bs4.BeautifulSoup(f, "lxml")

    with open("output.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for i in soup.find_all("trkpt"):
            writer.writerow([i["lat"], i["lon"], i.ele.string, i.time.string])

# converts decimal coordinate data to sexagesimal tuple type data
def convert_loc(loc_decimal: tuple[float, float]) -> LocSexagesimal:
    # converts decimal to sexagesimal
    def convert_to_sexagesimal(degree_decimal: float, directions: tuple[str, str]) \
            -> NumSexagesimal:
        if degree_decimal >= 0:
            direction = directions[0]
        elif degree_decimal < 0:
            direction = directions[1]
        
        degrees = int(math.modf(degree_decimal)[1])
        minutes = int(math.modf(60 * math.modf(degree_decimal)[0])[1])
        seconds = 60 * math.modf(60 * math.modf(degree_decimal)[0])[0]
        return (degrees, minutes, seconds, direction)

    latitude_decimal = loc_decimal[0]
    longlitude_decimal = loc_decimal[1]
    latitude_sexagesimal = convert_to_sexagesimal(latitude_decimal, ("N", "S"))
    longlitude_sexagesimal \
        = convert_to_sexagesimal(longlitude_decimal, ("E", "W"))
    loc_sexagesimal = (latitude_sexagesimal, longlitude_sexagesimal)
    return loc_sexagesimal

# converts sexagesimal longlitude/latitude data into exif format
def generate_exifloc(loc_sexagesimal: LocSexagesimal) -> dict:
    latitude_sexagesimal = loc_sexagesimal[0]
    longlitude_sexagesimal = loc_sexagesimal[1]

    # converts coordinate to rational numbers
    def convert_to_exifloc(sexagesimal: NumSexagesimal) -> GPSExif:
        def change_to_rational(number: float) -> tuple[int, int]:
            f = Fraction(str(number))
            return (f.numerator, f.denominator)
        
        exif = (change_to_rational(sexagesimal[0]),
                change_to_rational(sexagesimal[1]),
                (round(100 * sexagesimal[2]), 100)
        )
        return exif
    
    exif_latitude = convert_to_exifloc(latitude_sexagesimal)
    exif_longlitude = convert_to_exifloc(longlitude_sexagesimal)

    gps_ifd = {
        piexif.GPSIFD.GPSVersionID: (2, 0, 0, 0),
        piexif.GPSIFD.GPSLatitudeRef: latitude_sexagesimal[3],
        piexif.GPSIFD.GPSLatitude: exif_latitude[0:3],
        piexif.GPSIFD.GPSLongitudeRef: longlitude_sexagesimal[3],
        piexif.GPSIFD.GPSLongitude: exif_longlitude[0:3],
    }
    gps_exif = {"GPS": gps_ifd}
    return gps_exif

# inserts exif data
def edit_exif_to_img(filename: str, exif_add: dict):
    exif_data = piexif.load(filename)
    exif_data.update(exif_add)
    piexif.insert(piexif.dump(exif_data), filename)
    piexif.load(filename)

def main():
    gpxfile = "gpsdata/20210725.gpx"
    convert_gpx_to_csv(gpxfile)
    loc_decimal = (36.948731, 139.975301) # dummy value

    loc_sexagesimal = convert_loc(loc_decimal)
    gps_exif = generate_exifloc(loc_sexagesimal)
    edit_exif_to_img("img/test.jpg", gps_exif)

if __name__ == "__main__":
    main()