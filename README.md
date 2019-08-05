# Automatic graph creating tool for LCMS metabolomics analysis
島津製作所LCMSデータ解析用ソフトLabsolutionsで出力したメタボローム解析データを自動でグラフ化できるちょっと便利なデータ処理ツール．

## Requirements
* Python3

## How to export the data from Labsolutions
「ブラウザ」から対象のデータを「定量結果のエクスポート」でテキストファイルとして取り出す．
このときに各列の項目が，左から順に「データファイル名」，「サンプル名」，「保持時間」，「面積」，「内部標準面積」，「面積比」になっていることをあらかじめ確認する（表示項目については別途設定が可能）．
株ごとのサンプル数は，全ての株で同じである必要があるので注意．