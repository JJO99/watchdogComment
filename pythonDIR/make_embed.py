import discord
from datetime import datetime, timedelta
import main_analysis
from pythonDIR import photo_get, personalInfo


version = "DEVELOID BOT v0.6.0(20221215)"
thumbnail_url_devel = personalInfo.devel_logo()
thumbnail_url_recycle = personalInfo.recycle_logo()
color = discord.Color.from_rgb(31, 132, 255)


def start_embed():
    origin_time = datetime.utcnow() + timedelta(hours=9)
    now = str(origin_time)
    
    embed = discord.Embed(title="ROBOT", colour=color)
    embed.set_thumbnail(url=thumbnail_url_recycle)
    embed.set_author(name=version)
    embed.add_field(name="**확인 하는 중**", value="최대 30초가량 소요됩니다.")
    time = "기준 시간: " + now
    embed.set_footer(text=time)

    return embed


def end_embed(driver, word, article_id):
    embed = discord.Embed(title="ROBOT", colour=color)
    embed.set_thumbnail(url=thumbnail_url_recycle)
    embed.set_author(name=version)

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
        embed.add_field(name="**★★주의★★**", value="실제 게시글에선 문제가 있을 수 있으니 꼭 모니터링 해주시기 바랍니다.")

    origin_time = datetime.utcnow() + timedelta(hours=9)
    now = str(origin_time)
    
    time = "기준 시간: " + now
    embed.set_footer(text=time)

    return embed


def photo_embed(driver, recent_id):
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
        embed = discord.Embed(title="베스트포토 긁어오기", colour=color)
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


def count_embed(count):
    embed = discord.Embed(title="ROBOT", colour=color)
    embed.set_author(name=version)
    embed.set_thumbnail(url=thumbnail_url_recycle)
    embed.add_field(name="작업이 완료되었습니다.", value="마지막 시동 이후 " + str(count) + "번째 작업이 완료되었습니다.", inline=False)
    embed.add_field(name="호출하기", value=personalInfo.discord_ninano())
    origin_time = datetime.utcnow() + timedelta(hours=9)
    now = str(origin_time)
    time = "기준 시간: " + now
    embed.set_footer(text=time)

    return embed


def sql_ready_embed():
    embed = discord.Embed(title="ROBOT", colour=color)
    embed.set_author(name=version)
    embed.set_thumbnail(url=thumbnail_url_recycle)
    embed.add_field(name="SQL 저장 중입니다.", value="게시글과 댓글을 서버에 저장합니다.", inline=False)
    origin_time = datetime.utcnow() + timedelta(hours=9)
    now = str(origin_time)
    time = "기준 시간: " + now
    embed.set_footer(text=time)

    return embed


def sql_finish_embed():
    embed = discord.Embed(title="ROBOT", colour=color)
    embed.set_author(name=version)
    embed.set_thumbnail(url=thumbnail_url_recycle)
    embed.add_field(name="SQL 저장을 끝냈습니다.", value="게시글과 댓글을 서버에 저장했습니다.", inline=False)
    origin_time = datetime.utcnow() + timedelta(hours=9)
    now = str(origin_time)
    time = "기준 시간: " + now
    embed.set_footer(text=time)

    return embed


def sql_search_start():
    embed = discord.Embed(title='ROBOT', colour=color)
    embed.set_author(name=version)
    embed.set_thumbnail(url=thumbnail_url_recycle)
    embed.add_field(name="SQL에 저장된 데이터 감시", value="사전에 저장한 금칙어가 포함된 게시글/댓글이 있는지 검사합니다.", inline=False)
    origin_time = datetime.utcnow() + timedelta(hours=9)
    now = str(origin_time)
    time = "기준 시간: " + now
    embed.set_footer(text=time)

    return embed


def sql_article_good():
    embed = discord.Embed(title='ROBOT', colour=color)
    embed.set_author(name=version)
    embed.set_thumbnail(url=thumbnail_url_recycle)
    embed.add_field(name="SQL에 저장된 댓글 데이터 검사 결과", value="게시글에 이상이 없습니다.", inline=False)
    origin_time = datetime.utcnow() + timedelta(hours=9)
    now = str(origin_time)
    time = "기준 시간: " + now
    embed.set_footer(text=time)

    return embed


def sql_comment_good():
    embed = discord.Embed(title='ROBOT', colour=color)
    embed.set_author(name=version)
    embed.set_thumbnail(url=thumbnail_url_recycle)
    embed.add_field(name="SQL에 저장된 댓글 데이터 검사 결과", value="댓글에 이상이 없습니다.", inline=False)
    origin_time = datetime.utcnow() + timedelta(hours=9)
    now = str(origin_time)
    time = "기준 시간: " + now
    embed.set_footer(text=time)

    return embed


def sql_article_bad():
    embed = discord.Embed(title='ROBOT', colour=color)
    embed.set_author(name=version)
    embed.set_thumbnail(url=thumbnail_url_recycle)
    embed.add_field(name="SQL에 저장된 게시글 데이터 검사 결과", value="금칙어가 포함된 것으로 보이는 게시글이 있습니다.", inline=False)
    embed.add_field(name="게시글 번호", value="카페를 참고하세요", inline=False)
    origin_time = datetime.utcnow() + timedelta(hours=9)
    now = str(origin_time)
    time = "기준 시간: " + now
    embed.set_footer(text=time)

    return embed


def sql_comment_bad():
    embed = discord.Embed(title='ROBOT', colour=color)
    embed.set_author(name=version)
    embed.set_thumbnail(url=thumbnail_url_recycle)
    embed.add_field(name="SQL에 저장된 댓글 데이터 검사 결과", value="금칙어가 포함된 것으로 보이는 댓글이 있습니다.", inline=False)
    embed.add_field(name="게시글 번호", value="카페를 참고하세요", inline=False)
    origin_time = datetime.utcnow() + timedelta(hours=9)
    now = str(origin_time)
    time = "기준 시간: " + now
    embed.set_footer(text=time)

    return embed