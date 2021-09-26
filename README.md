# attach-gpsdata-photos
時間情報を基にしてスマートフォンやGPSロガーの位置情報を写真に付与します．

## Installation
本プログラムは以下のライブラリを必要とします．`pip install ライブラリ名`で予めインストールしてください．
- bs4
- lxml
- piexif
- pathlib
- pandas
- datetime
- dateutil

## Usage
- 撮影前にカメラ本体とGPSロガーの時刻を一致させます．
- 撮影中はGPSロガーで位置情報を記録しておきます．
- 位置情報を`gpx`形式でエクスポートして`gpx`ディレクトリにコピーします．
- 位置情報を付与したい画像データを`img`ディレクトリにコピーします．
- `main.py`を実行すると位置情報が画像に付与されます．

## Author
* Motohiro Sato (佐藤初洋)
* E-mail: msatores "at" gmail.com

## License
Copyright (C) 2021 Motohiro Sato

diffusion-calculator is released under [MIT license](https://opensource.org/licenses/mit-license.php).