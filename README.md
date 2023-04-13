# 🐤TwiChecker
![GitHub release (latest by date)](https://img.shields.io/github/v/release/nh-chitose/TwiChecker?display_name=tag)
![PyPI](https://img.shields.io/pypi/v/py-cord)
[![CodeQL](https://github.com/nh-chitose/TwiChecker/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/nh-chitose/TwiChecker/actions/workflows/github-code-scanning/codeql)
[![CI](https://github.com/nh-chitose/TwiChecker/actions/workflows/test.yml/badge.svg)](https://github.com/nh-chitose/TwiChecker/actions/workflows/test.yml)
![GitHub](https://img.shields.io/github/license/nh-chitose/TwiChecker)


ツイッターのプロフィールをスラッシュコマンドでDiscord上で簡単に取得できるボットです。

## 必要な権限
☑ メッセージを送信

☑ 埋め込みリンク

☑ アプリコマンドを使う

## 推奨環境
* Python v3.8以降
* Poetry v1.4.0以降

# 導入

```sh
# クローン
git clone https://github.com/nh-chitose/TwiChecker.git
# ディレクトリの移動
cd TwiChecker
# 依存関係のインストール
poetry install
```
`.env`ファイルの用意
```
DISCORD_TOKEN=(Discord Developer Portalで取得したトークン)
TWITTER_TOKEN=(Twitterで取得したベアラートークン)
```
```sh
# 実行
poetry run python3 index.py
```

# サポート
[サポートサーバ](https://discord.gg/CAP6JJPdaE)にて質問・バグの報告などを受け付けております。

またご自分でホストしなくても、上記サーバーから導入して頂けます。

# Change Log
2022/11/28 Release v1.0.0

2022/12/18 Update 埋め込みリンクの送信 v1.1.0
