import discord
import datetime
import main_analysis
from pythonDIR import article_id_get, photo_get


def start_embed(color):
    embed = discord.Embed(title="감시봇", colour=color)
    embed.set_author(name="DEVELOID BOT(ALPHA)")
    embed.add_field(name="**확인 하는 중**", value="약 10초가량 소요됩니다.")

    return embed


def end_embed(color, driver, word):
    now = str(datetime.datetime.now())
    embed = discord.Embed(title="감시봇", colour=color)
    embed.set_author(name="DEVELOID BOT(ALPHA)")

    article_id = list(set(article_id_get.recent_article_id_get() + article_id_get.all_article_id_get()))

    url_list = []
    for x in article_id:
        temp = main_analysis.Analyse(driver, x, word)
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


def photo_embed(color, driver, recent_id):
    list = photo_get.photo_get(recent_id, driver)
    embed_mte = []
    return_id = recent_id

    for k in list:
        if k[8] <= recent_id:
            return_id = recent_id
            continue
        else:
            return_id = k[8]
        embed_d = []
        embed = discord.Embed(title="베스트포토봇", colour=color)
        embed.set_author(name="DEVELOID BOT(ALPHA)")
        embed.add_field(name="**게시글 제목**", value=k[0], inline=True)
        embed.add_field(name="**사진 제목**", value=k[7], inline=True)
        embed.add_field(name="**작성자**", value=k[1], inline=True)
        embed.add_field(name="**촬영 장소**", value=k[2], inline=True)
        embed.add_field(name="**촬영 시간**", value=k[6], inline=True)
        embed.add_field(name="**링크**", value=k[5], inline=True)
        for x in range(len(k[3])):
            if x == 0:
                embed.add_field(name="**대표 사진**", value=embed.set_image(url=k[3][x]), inline=False)
            else:
                embed_d.append(k[3][x])
        embed.set_footer(text="게시글 작성 일시: " + k[4])
        embed_d.insert(0, embed)
        embed_mte.append(embed_d)

    return embed_mte, return_id

