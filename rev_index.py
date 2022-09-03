from discord.ext import tasks
from pythonDIR import personalInfo, auto_login, make_embed
import discord

driver = auto_login.login()
print("DRIVER LOGIN")


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_background_task.start()
        self.word = "m.site.naver.com", "bit.ly", "open.kakao.com", "이팀장", "카톡", "ㅋr톡", "bltly.link", "vo.la", "news.ycombinator.com"

    async def on_ready(self):
        print('BOT LOGIN')

    @tasks.loop(seconds=1800)
    async def my_background_task(self):
        global photo_recent_id

        channel = self.get_channel(personalInfo.chanid())  # channel ID goes here
        color = discord.Color.from_rgb(31, 132, 255)

        embed1 = make_embed.start_embed(color)
        await channel.send(embed=embed1, delete_after=30)
        print('CHECK START')

        embed2 = make_embed.end_embed(color, driver, self.word)
        await channel.send(embed=embed2)
        print('CHECK FINISHED')

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in


client = MyClient()
client.run(personalInfo.token())
