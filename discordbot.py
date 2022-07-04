import discord, main
from pythonDIR import personalInfo, naver
from discord.ext import tasks

client = discord.Client()
driver = naver.login()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$check'):
        await message.channel.send("*****체크하는 중*****")
        print('Checking')

        urllist,now = main.watch(driver)
        time = "기준시간: " + now
        if not urllist == "0":
            url = "@everyone 이상 게시글: " + urllist
        else:
            url = "이상 게시글이 없습니다."

        await message.channel.send(time)
        await message.channel.send(url)
        print('Checked')

@tasks.loop(seconds=1)
async def background_task(message):
    await message.channel.send('Hello!')

client.run(personalInfo.token())