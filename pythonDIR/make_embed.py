import discord
from datetime import datetime, timedelta
import main_analysis
from pythonDIR import article_id_get, photo_get

version = "DEVELOID BOT(ALPHA) v0.1.3(20220903)"

def start_embed(color):
    embed = discord.Embed(title="감시봇", colour=color)
    embed.set_author(name=version)
    embed.add_field(name="**확인 하는 중**", value="약 30초가량 소요됩니다.")

    return embed


def end_embed(color, driver, word):
    origin_time = datetime.utcnow() + timedelta(hours=9)
    now = str(origin_time)

    embed = discord.Embed(title="감시봇", colour=color)
    embed.set_author(name=version)

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
        embed.add_field(name="**확인 결과**", value=url, inline=False)
        embed.add_field(name="**★★주의★★**", value="아직 알파버전인 관계로 이상이 없다고 뜨더라도 실제 게시글에선 문제가 있을 수 있으니 꼭 모니터링 해주시기 바랍니다.")

    time = "기준 시간: " + now
    embed.set_footer(text=time)

    return embed


def photo_embed(color, driver, recent_id):
    get_list = photo_get.photo_get(recent_id, driver)
    embed_mte = []
    return_id = recent_id

    for k in get_list:
        if k[8] <= recent_id:
            return_id = recent_id
            continue
        else:
            return_id = k[8]
        
        for x in range(len(k)):
            if k[x] == "":
                k[x] = "(양식에 맞게 작성되지 않음)"
            else:
                continue
        
        embed_d = []
        embed = discord.Embed(title="베스트포토봇", colour=color)
        embed.set_author(name=version)
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

