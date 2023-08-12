# Pythonのいろいろなサンプルを吐き出すリポジトリです。

## init

### 前提

- `Python`はインストール済みであること。
- dockerを実行可能な状態であること。

### 初期化

Install

```shell
pip install -r ./requirements.txt
```

Docker init

```shell
docker-compose -f ./docker-mysql/docker-mysql-compose.yaml up -d
```

DB access

```shell
docker-compose -f ./docker-mysql/docker-mysql-compose.yaml run cli
```