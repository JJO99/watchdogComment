from discord.ext import tasks
from pythonDIR import personalInfo, naver, articleID, make_embed
import discord, analysemain, datetime

driver = naver.login()
word = "m.site.naver.com", "bit.ly", "open.kakao.com", "제닉스입니다", "드디어", "여전히", "카톡", "초보자", "오늘", "신청합니다"
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

    @tasks.loop(seconds=1800)  # task runs every 60 seconds
    async def my_background_task(self):
        channel = self.get_channel(personalInfo.chanid())  # channel ID goes here
        color = discord.Color.from_rgb(31, 132, 255)

        embed1 = make_embed.start_embed(color)
        await channel.send(embed=embed1, delete_after=10)
        print('Checking')

        embed2 = make_embed.end_embed(color, driver, word, self.now)
        await channel.send(embed=embed2)
        print('Checked')

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in


client = MyClient()
client.run(personalInfo.token())