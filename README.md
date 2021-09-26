# attach-gpsdata-photos
時間情報を基にしてスマートフォンやGPSロガーの位置情報を写真に付与します

## Installation
以下のサードパーティ製ライブラリを必要とします．使用前に `pip install ${packagename}` でインストールしてください．

- `lxml`
- `bs4`
- `piexif`
- `pandas`
- `numpy`
- `datetime`
- `dateutil`

## Usage
- カメラとGPSロガー（`gpx`形式のデータを出力できるものであればスマートフォンアプリ等も使用可能です）の時刻を正確に合わせます．
- 撮影中にGPSのログを記録します．
- `img`ディレクトリに撮影した`jpg`形式の写真を，`gpx`ディレクトリに`gpx`形式のGPSログファイルを格納します．
- `main.py`を実行すると，`img`ディレクトリ中の写真に位置情報が付されます．またGPSログファイルは`out.csv`として出力されます．

## Author
* Motohiro Sato (佐藤初洋)
* E-mail: msatores "at" gmail.com

## License
Copyright (C) 2021 Motohiro Sato

diffusion-calculator is released under [MIT license](https://opensource.org/licenses/mit-license.php).