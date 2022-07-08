from discord.ext import tasks
from pythonDIR import personalInfo, naver

import discord, main

driver = naver.login()

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.counter = 0

        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print('봇 로그인 성공')

    @tasks.loop(seconds=60) # task runs every 60 seconds
    async def my_background_task(self):
        channel = self.get_channel(994834466906324993) # channel ID goes here

        color = discord.Color.from_rgb(31, 132, 255)

        embed1 = discord.Embed(title="감시봇",colour=color)
        embed1.set_author(name="DEVELOID BOT(ALPHA)")
        embed1.add_field(name="**확인 하는 중**", value="약 2초가량 소요됩니다.")
        await channel.send(embed=embed1, delete_after=3)
        print('Checking')

        urllist, now = main.watch(driver)
        time = "기준시간: " + now
        if not urllist == "0":
            url = "everyone 이상 게시글: " + urllist
        else:
            url = "이상 게시글이 없습니다."

        embed2 = discord.Embed(title="감시봇", colour=color)
        embed2.set_author(name="DEVELOID BOT(ALPHA)")
        embed2.add_field(name="**확인 결과**", value=url)
        embed2.set_footer(text=time)
        await channel.send(embed=embed2)

        print('Checked')

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready() # wait until the bot logs in

client = MyClient()
client.run(personalInfo.token())