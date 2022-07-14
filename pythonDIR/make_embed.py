import discord
import datetime
import main_analysis
from pythonDIR import article_id_get


def start_embed(color):
    embed = discord.Embed(title="감시봇", colour=color)
    embed.set_author(name="DEVELOID BOT(ALPHA)")
    embed.add_field(name="**확인 하는 중**", value="약 10초가량 소요됩니다.")

    return embed


def end_embed(color, driver, word):
    now = str(datetime.datetime.now())
    embed = discord.Embed(title="감시봇", colour=color)
    embed.set_author(name="DEVELOID BOT(ALPHA)")

    article_id = list(set(articleID.recent_article_id_get() + articleID.all_article_id_get()))

    url_list = []
    for x in article_id:
        temp = analysemain.Analyse(driver, x, word)
        get = temp.one_total_check()
        url_list.append(get)

    while None in url_list:
        url_list.remove(None)

    if not len(url_list) == 0:
        url = "everyone 이상 게시글: " + str(url_list)
        embed.add_field(name="**확인 결과**", value=url, inline=False)
    else:
        url = "이상 게시글이 없습니다."
        embed.add_field(name="**확인 결과**", value=url)

    time = "기준 시간: " + now
    embed.set_footer(text=time)

    return embed