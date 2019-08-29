# Automatic graph creating tool for LCMS metabolomics analysis
島津製作所 LCMS データ解析用ソフト Labsolutions で出力したメタボローム解析データを
自動でグラフ化できるちょっと便利なデータ処理ツール．

## Requirements
* Python3
  - Python3.6.5 (macOS Mojave 10.14.5) にて動作確認済

## How to export the data from Labsolutions
「ブラウザ」から対象のデータを「定量結果のエクスポート」でテキストファイルとして取り出す．
このときに各列の項目が，左から順に「データファイル名」，「サンプル名」，「保持時間」，「面積」，「内部標準面積」，「面積比」になっていることをあらかじめ確認する（表示項目については別途設定が可能）．
株ごとのサンプル数は，全ての株で同じである必要があるので注意．

## Usage
1. Clone or download ボタンから Download ZIP でファイルを保存する．
2. ダウンロードしたファイルを解凍する．
3. dat ファイル内に Labsolutions から出力したテキストファイルを入れる（例として sample_data.txt を配置済）．
4. Labsolutions から出力したテキストファイルに応じてconfig ファイルを編集する（config ファイルの編集の仕方は **How to edit config file** を参照）．
5. lcms （またはlcms-master）のディレクトリで `make` と打って処理を実行する．
6. 処理が正しく実行された場合，img フォルダが生成され，img フォルダの中にはそれぞれの代謝物のグラフ（png 形式）と全てのグラフをまとめた pdf ファイル (graph_all.pdf) が生成される．

## How to edit config file
初期状態では sample_data.txt に合わせた設定になっているので，グラフ出力したい LCMS データごとに書き換えて変更する必要がある．config ファイルのフォーマットは以下の通りである．空白なし，カンマ区切りで入力する（config ファイルはテキストエディタで開いて編集できる）．テキストファイル名や株名にも空白を入れない．

* 1行目：sample_data.txt は LCMS で出力したテキストデータのファイル名
* 2行目：strain_i は株 i の名前
* 3行目：od_i は株 i の濁度
* 4行目：m は株の数，n はサンプル数

```
sample_data.txt
strain_1,strain_2,strain_3
od_1,od_2,od_3
m,n
```
