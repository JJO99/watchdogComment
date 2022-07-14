from discord.ext import tasks
from pythonDIR import personalInfo, naver, articleID
import discord, analysemain, datetime

driver = naver.login()
경word = "m.site.naver.com", "bit.ly", "open.kakao.com", "제닉스입니다", "드디어", "여전히", "카톡", "초보자"
# pip install -r requirements.txt

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # start the task to run in the background
        self.my_background_task.start()
        self.now = str(datetime.datetime.now())

        global word

    async def on_ready(self):
        print('봇 로그인 성공')

    @tasks.loop(seconds=60)  # task runs every 60 seconds
    async def my_background_task(self):
        channel = self.get_channel(personalInfo.chanid())  # channel ID goes here

        color = discord.Color.from_rgb(31, 132, 255)

        embed1 = discord.Embed(title="감시봇", colour=color)
        embed1.set_author(name="DEVELOID BOT(ALPHA)")
        embed1.add_field(name="**확인 하는 중**", value="약 10초가량 소요됩니다.")
        await channel.send(embed=embed1, delete_after=10)
        print('Checking')

        embed2 = discord.Embed(title="감시봇", colour=color)
        embed2.set_author(name="DEVELOID BOT(ALPHA)")

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
            embed2.add_field(name="**확인 결과**", value=url, inline=False)
        else:
            url = "이상 게시글이 없습니다."
            embed2.add_field(name="**확인 결과**", value=url)

        time = "기준 시간: " + self.now
        embed2.set_footer(text=time)

        await channel.send(embed=embed2)

        print('Checked')

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in


client = MyClient()
client.run(personalInfo.token())