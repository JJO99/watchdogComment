from discord.ext import tasks
from pythonDIR import personalInfo, auto_login, make_embed
import discord
import datetime
print(datetime.datetime.now())
driver = auto_login.login()
print(datetime.datetime.now())
word = "m.site.naver.com", "bit.ly", "open.kakao.com", "카톡", "ㅅㅂ"
# pip install -r requirements.txt 설치시
# pip freeze > requirements.txt 저장시


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # start the task to run in the background
        self.my_background_task.start()

        global word

    async def on_ready(self):
        print('봇 로그인 성공')
        print(datetime.datetime.now())

    @tasks.loop(seconds=300)  # task runs every 60 seconds
    async def my_background_task(self):
        channel = self.get_channel(personalInfo.chanid())  # channel ID goes here
        color = discord.Color.from_rgb(31, 132, 255)

        embed1 = make_embed.start_embed(color)
        await channel.send(embed=embed1, delete_after=10)
        print('Checking')
        print(datetime.datetime.now())

        embed2 = make_embed.end_embed(color, driver, word)
        await channel.send(embed=embed2)
        print('Checked')
        print(datetime.datetime.now())

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in


client = MyClient()
client.run(personalInfo.token())