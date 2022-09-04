from discord.ext import tasks
from pythonDIR import personalInfo, auto_login, make_embed, get_sheet
import discord

photo_recent_id = "993372"
driver = auto_login.login()
print("DRIVER LOGIN")


# pip install -r requirements.txt 설치시, pip freeze > requirements.txt 저장시


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

    @tasks.loop(seconds=1800)
    async def my_background_task(self):
        global photo_recent_id

        word = get_sheet.main()

        channel = self.get_channel(personalInfo.chanid())  # channel ID goes here
        color = discord.Color.from_rgb(31, 132, 255)

        embed1 = make_embed.start_embed(color)
        await channel.send(embed=embed1, delete_after=30)
        print('CHECK START')
        await self.bot_status(1)

        embed2 = make_embed.end_embed(color, driver, word)
        await channel.send(embed=embed2, delete_after=1790)
        print('CHECK FINISHED')

        await self.bot_status(2)
        print('PHOTO START')
        embed3, recent_id = make_embed.photo_embed(color, driver, photo_recent_id)
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
        await self.bot_status(0)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in


client = MyClient()
client.run(personalInfo.token())
