from datetime import datetime
import os

import dotenv
from pytz import timezone

from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

timezone = timezone("Europe/Helsinki")

default_contingent = "2/21"
default_duration = 347

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.command(name="aamuja", help="Toivottaa aamuja")
async def aamuja(ctx):
    await ctx.send("Aamuja!")


@bot.command(name="tj", help="Tänään jäljellä")
async def tj(ctx):
    tj = count_tj()
    await ctx.send(f"Tänään jäljellä: **{tj}** aamua")


@bot.command(name="ohi", help="Aamuja ohi")
async def ohi(ctx):
    tj = count_tj()
    ohi = 347-tj
    await ctx.send(f"Ohi on: **{ohi}** aamua")


@bot.command(name="lisätietoja", help="Yksityiskohtaisempaa tietoa")
async def lisatietoja(ctx, contingent: str = default_contingent, duration: int = default_duration):
    if not valid_contingent(contingent):
        await ctx.send("Virheellinen saapumiserä")
        return
    if not valid_duration(duration):
        await ctx.send("Virheellinen palvelusaika")
        return
    tj0 = datetime(2022, 6, 16, 10, 0, 0)
    tj0 = timezone.localize(tj0)
    now = datetime.now(tz=timezone)
    seconds = abs(now-tj0).total_seconds()
    minutes = seconds/60
    hours = minutes/60
    days = hours/24
    weeks = days/7
    months = days/30.437
    years = days/365
    ohi = duration-count_tj()
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


def valid_contingent(contingent):
    valid = ["1/21", "2/21"]
    return contingent in valid


def valid_duration(duration):
    valid = [165, 255, 347]
    return duration in valid


def count_tj():
    now = datetime.now(tz=timezone)
    tj0 = datetime(2022, 6, 16)
    tj0 = timezone.localize(tj0)
    tj = abs((now-tj0).days)
    return tj


bot.run(TOKEN)
