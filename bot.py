import discord
from discord.ext import tasks, commands

import os
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1470049050693734563

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    hourly_message.start()

@tasks.loop(hours=1)
async def hourly_message():
    channel = bot.get_channel(1470049050693734563)
    if channel:
        await channel.send("bobio kusai")

bot.run(TOKEN)