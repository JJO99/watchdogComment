from discord.ext import tasks

from pythonDIR import personalInfo, auto_login, make_embed, get_sheet, article_id_get, go_to_sql
import discord
import main_analysis

photo_recent_id = "993372"
driver = auto_login.login()
print("DRIVER LOGIN")
loop_count = 0

# pip install -r requirements.txt 설치시, pip freeze > requirements.txt 저장시


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print('BOT LOGIN')

    async def bot_status(self, now):
        if now == 0:
            await client.change_presence(activity=discord.Game('가만히 숨쉬기'))
        elif now == 1:
            await client.change_presence(activity=discord.Game('게시글/댓글 검사'))
        elif now == 2:
            await client.change_presence(activity=discord.Game('베스트포토 검사'))
        elif now == 3:
            await client.change_presence(activity=discord.Game('댓글을 저장'))
        elif now == 4:
            await client.change_presence(activity=discord.Game('게시글을 저장'))

    @tasks.loop(seconds=1800)
    async def my_background_task(self):
        global loop_count
        loop_count = loop_count + 1

        global photo_recent_id

        word = get_sheet.main()

        channel = self.get_channel(personalInfo.chanid())  # channel ID goes here

        embed1 = make_embed.start_embed()
        await channel.send(embed=embed1, delete_after=30)
        print('CHECK START')
        await self.bot_status(1)

        article_id = list(set(article_id_get.recent_article_id_get() + article_id_get.all_article_id_get()))

        embed2 = make_embed.end_embed(driver, word, article_id)
        await channel.send(embed=embed2, delete_after=1730)
        print('CHECK FINISHED')

        await self.bot_status(2)
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

        #  save comment, article
        await self.bot_status(3)
        print('SAVE COMMENT')
        for x in article_id:
            temp = main_analysis.Analyse(driver, x, word)
            list_file = temp.comment_sql_Data()

            for y in list_file:
                go_to_sql.comment_insert(x, y[0], y[1], y[3], y[4], y[2])

        await self.bot_status(4)
        print('SAVE ARTICLE')
        for x in article_id:
            temp = main_analysis.Analyse(driver, x, word)
            y = temp.article_sql_Data()
            go_to_sql.article_insert(x, y[0][0], y[1], y[2], y[3])

        print(loop_count, "번째 루프 작업이 정상적으로 완료되었습니다.")
        embed4 = make_embed.count_embed(loop_count)
        await channel.send(embed=embed4, delete_after=600)
        await self.bot_status(0)


    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()


intents = discord.Intents.default()
client = MyClient(intents=intents)
client.run(personalInfo.token())