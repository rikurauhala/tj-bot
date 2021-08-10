from datetime import datetime
import os

import dotenv
from pytz import timezone

from discord.ext import commands

from tj import count_tj, get_tj0
from validation import valid

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

timezone = timezone("Europe/Helsinki")

default_contingent = "2/21"
default_duration = 347

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


@bot.command(name="tj", help="Tänään jäljellä")
async def tj(ctx, contingent: str = default_contingent, duration: int = default_duration):
    if not valid(ctx, contingent, duration):
        return
    tj = count_tj(contingent, duration)
    if tj > 0:
        await ctx.send(f"Tänään jäljellä: **{tj}** aamua")
    else:
        await ctx.send(f"Tänään jäljellä: **{tj}** aamua, ohi on!")


@bot.command(name="ohi", help="Aamuja ohi")
async def ohi(ctx, contingent: str = default_contingent, duration: int = default_duration):
    if not valid(ctx, contingent, duration):
        return
    tj = count_tj(contingent, duration)
    ohi = 347-tj
    await ctx.send(f"Ohi on: **{ohi}** aamua")


@bot.command(name="lisätietoja", help="Yksityiskohtaisempaa tietoa")
async def lisatietoja(ctx, contingent: str = default_contingent, duration: int = default_duration):
    if not valid(ctx, contingent, duration):
        return
    tj0 = get_tj0(contingent, duration)
    tj = count_tj(contingent, duration)
    if tj < 0:
        await ctx.send("Ohi on!")
        return
    now = datetime.now(tz=timezone)
    seconds = abs(now-tj0).total_seconds()
    minutes = seconds/60
    hours = minutes/60
    days = hours/24
    weeks = days/7
    months = days/30.437
    years = days/365
    ohi = duration-tj
    percent = 100*(1-days/duration)
    details = f"```Saapumiserä: {contingent} \n" \
              f"Palvelusaika: {duration} \n\n" \
              f"TÄNÄÄN JÄLJELLÄ \n" \
              f"- Vuosina: {years:.2f} \n" \
              f"- Kuukausina: {months:.2f} \n" \
              f"- Viikkoina: {weeks:.1f} \n" \
              f"- Päivinä: {days:.1f} \n" \
              f"- Tunteina: {hours:.0f} \n" \
              f"- Minuutteina: {minutes:.0f} \n" \
              f"- Sekunteina: {seconds:.0f} \n\n" \
              f"OHI ON \n" \
              f"- {ohi} aamua ({percent:.2f} %)```"
    await ctx.send(details)


bot.run(TOKEN)
