from discord.ext import tasks
from pythonDIR import personalInfo, auto_login, make_embed
import discord
import datetime

print(datetime.datetime.now())
driver = auto_login.login()
print(datetime.datetime.now())
word = "m.site.naver.com", "bit.ly", "open.kakao.com", "ㅅㅂ"
photo_recent_id = "0"


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

    @tasks.loop(seconds=600)
    async def my_background_task(self):
        global photo_recent_id
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

        embed3, recent_id = make_embed.photo_embed(color, driver, photo_recent_id)
        photo_recent_id = recent_id
        channel_photo = self.get_channel(personalInfo.chanid_photo())
        for x in embed3:
            await channel_photo.send(embed=x[0])
            if not len(x) == 1:
                for y in range(len(x)-1):
                    await channel_photo.send(x[y+1])
            else:
                pass
        print('Finished')
        print(datetime.datetime.now())

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in


client = MyClient()
client.run(personalInfo.token())
