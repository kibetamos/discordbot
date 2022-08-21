from multiprocessing.connection import Client
import discord

TOKEN = "MTAxMDg1OTcwOTI4MjEyMzkxOQ.Gc1h2v.baqah8ykNCEM8rwMgLb5Q_5GlufX3h7j5uBqbc"

#client = discord.Client()
client = discord.Client(intents=discord.Intents.default())

@client.event

async def on_ready():
    print("{0.user} is online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith("!hello") or message.content.startswith("/hello"):
        await message.channel.send("Hello from the other side of the world!")


client.run(TOKEN)







