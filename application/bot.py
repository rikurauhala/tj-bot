from datetime import datetime
import os

import dotenv
from pytz import timezone

from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

description = "tj-bot kertoo montako aamua on tänään jäljellä"
bot = commands.Bot(command_prefix="!", description=description)

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        cog = file[:-3]
        bot.load_extension(f"cogs.{cog}")
        print(f"Loaded '{cog}'")


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


bot.run(TOKEN)
