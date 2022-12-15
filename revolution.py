
from pythonDIR import personalInfo, auto_login, make_embed, get_sheet, article_id_get
import discord
import main_analysis, sql_control
import asyncio

photo_recent_id = "994563"
driver = auto_login.login()
print("DRIVER LOGIN")
loop_count = 0
# TODO: 스크랩 게시글의 글과 댓글을 불러오게 작업하기.


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('BOT LOGIN')

    async def bot_status(self, now):
        if now == 0:
            await client.change_presence(activity=discord.Game('가만히 숨쉬기'))
        elif now == 1:
            await client.change_presence(activity=discord.Game('SQL에 저장'))
        elif now == 2:
            await client.change_presence(activity=discord.Game('게시글 분석'))
        elif now == 3:
            await client.change_presence(activity=discord.Game('댓글 분석'))
        elif now == 4:
            await client.change_presence(activity=discord.Game('베스트포토 긁어오기'))

    async def my_background_task(self):
        await self.wait_until_ready()
        # ------------------------------------------------------------------------------------------ #
        # 1. 루프 카운트, 최근 베스트포토 게시글 번호 글로벌로 호출. 금칙어를 시트에서 불러옴. 표시할 채널을 가져옴.
        global loop_count
        loop_count = loop_count + 1
        global photo_recent_id
        word = get_sheet.main()
        channel = self.get_channel(personalInfo.chanid())
        log_channel = self.get_channel(personalInfo.log_chanid())
        print('SETUP READY')
        # ------------------------------------------------------------------------------------------ #
        # 2. article ID를 가져오고, 크롤링하고, MySQL 서버에 저장
        await self.bot_status(1)
        embed1 = make_embed.sql_ready_embed()
        await log_channel.send(embed=embed1)
        print('SQL SAVE START')

        article_id = list(set(article_id_get.recent_article_id_get() + article_id_get.all_article_id_get()))
        for x in article_id:
            temp = main_analysis.Analyse(driver, x, word)
            list_value_a = temp.article_sql_Data()
            list_value_c = temp.comment_sql_Data()

            sql_control.article_insert(list_value_a, x)

            if list_value_c is None:
                continue
            else:
                for y in list_value_c:
                    sql_control.comment_insert(y, x)

        embed2 = make_embed.sql_finish_embed()
        await log_channel.send(embed=embed2)
        print('SQL SAVE FINISHED')
        # ------------------------------------------------------------------------------------------ #
        # 3. 게시글의 금칙어 위반 여부를 검사하고 결과를 표시함.
        await self.bot_status(2)
        embeda = make_embed.sql_search_start()
        await channel.send(embed=embeda)

        result1 = sql_control.search_sql_article(word)
        if result1 is None:
            embed3 = make_embed.sql_article_good()
            await channel.send(embed=embed3)
        else:
            for x in result1:
                print(x)
        # ------------------------------------------------------------------------------------------ #
        # 4. 댓글의 금칙어 위반 여부를 검사하고 결과를 표시함.
        await self.bot_status(3)
        result2 = sql_control.search_sql_comment(word)
        if result2 is None:
            embed4 = make_embed.sql_comment_good()
            await channel.send(embed=embed4)
        else:
            for x in result2:
                print(x)
        # ------------------------------------------------------------------------------------------ #
        # 5. 베스트포토의 게시글을 가져오고 결과를 표시함.
        await self.bot_status(4)
        print('PHOTO START')
        embed3, recent_id = make_embed.photo_embed(driver, photo_recent_id)
        photo_recent_id = recent_id
        channel_photo = self.get_channel(personalInfo.chanid_photo())
        for x in embed3:
            await channel_photo.send(embed=x[0])
            if not len(x) == 1:
                for y in range(len(x) - 1):
                    await channel_photo.send(x[y + 1])
            else:
                pass
        print('PHOTO FINISHED')
        # ------------------------------------------------------------------------------------------ #
        # 6. 로그 채널에 루프 작업이 완료되었음을 표시함.
        print(loop_count, "번째 루프 작업이 정상적으로 완료되었습니다.")
        embed4 = make_embed.count_embed(loop_count)
        await channel.send(embed=embed4, delete_after=600)
        await self.bot_status(0)

        while not self.is_closed():
            await asyncio.sleep(1800)


intents = discord.Intents.default()
client = MyClient(intents=intents)
client.run(personalInfo.token())
