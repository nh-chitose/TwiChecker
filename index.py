import os
from datetime import datetime

import discord
import requests
from dotenv import load_dotenv

load_dotenv()
client = discord.Bot()

# Checker関数の定義
def checker(id):
  api_url = "https://api.twitter.com/2/users/by/username/" + id
  # Twitterのベアラートークン
  tToken = os.getenv("TWITTER_TOKEN")
  # 取得する情報を指定
  params = {
    "user.fields": "name,description,profile_image_url,protected,created_at"
  }
  # ヘッダーにトークンをセット
  headers = {
    "Authorization": "Bearer " + tToken
  }
  # リクエストを投げる
  response = requests.get(api_url, params = params, headers = headers, timeout = 5000)
  # パースしてみる
  try:
    user = response.json()["data"]
  # キーエラーの場合空の辞書を返す
  except KeyError:
    user = {}
  # 取得したユーザ辞書を戻り値にセット
  return user

# ボットがオンラインになったときの動作を指定
@client.event
async def on_ready():
  # コンソールにユーザ名とIDを出力
  print("Logged in as")
  print(client.user.name)
  print(client.user.id)
  print("------")
  print("Bot is ready!")
  # 参加しているサーバ数を調べる
  count = len(client.guilds)
  # プレイ中にサーバ数をセット
  await client.change_presence(activity=discord.Game(name="on " + str(count)+" servers", type=1))

# スラッシュコマンドの定義
@client.slash_command(description="Twitter IDが有効かどうかチェックします。")
async def twicheck(
  ctx: discord.ApplicationContext,
  id: discord.Option(str, description="確認したいIDを入力してください。", required=True, min_length=1, max_length=15)
):
  # 変数mをこのスコープで使うために空で定義
  m = ""
  # checker関数の戻り値にデータがある場合の条件分岐
  if checker(id):
  # checker関数の戻り値を変数userに格納
    user = checker(id)
    # 返信の内容(ID、ユーザ名)を代入
    embed = discord.Embed(
      title=user["name"],
      description=user["description"],
      color=2105893,
      timestamp=datetime.strptime((user["created_at"]), "%Y-%m-%dT%H:%M:%S.%f%z"))     
    embed.set_author(name=user["username"])
    embed.set_thumbnail(url=user["profile_image_url"])

      # 鍵垢がTRUEの場合
    if user['protected']:
          # エンベッドのリストにフッターを追加
      embed.set_footer(text="🔐")
    await ctx.respond(embed=embed)
  # checker関数の戻り値が空の辞書の場合
  else:
    # エラーメッセージを代入
    m = "指定された`" + id + "`というTwitter IDは存在しません。"
    await ctx.respond(m)

dToken = os.getenv("DISCORD_TOKEN")
try: 
  client.run(dToken)
except TypeError:
  print("Invalid Discord Token.")
