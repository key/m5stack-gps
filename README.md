# ここは何？

M5Stack と GPS Module (u-blox NEO-M8N)を使ったコード片を集めています。

## Requirements

- M5Stack Base or Gray (Fire は対応していません)
- M5Stack GPS Module

## ディレクトリの説明

- mpu9250_gbowl
  - G ボウルを描画します
  - MPU9250 搭載モデル専用
- satellite_view
  - 衛星描画します
  - [Ambient さんのブログ](https://ambidata.io/blog/2018/10/12/m5stack_gpswatch/)にあったコードを pyflake にかけて清書しました
- ublox_agps
  - ublox UBX protocol のテスト
