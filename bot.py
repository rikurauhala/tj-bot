from datetime import datetime
import os

import dotenv
from pytz import timezone

import discord
from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

timezone = timezone("Europe/Helsinki")

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
async def lisatietoja(ctx):
    se = "2/21"
    pa = 347
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
    ohi = pa-count_tj()
    percent = 100*(1-days/pa)
    details = f"```Saapumiserä: {se} \n" \
              f"Palvelusaika: {pa} \n\n" \
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


def count_tj():
    now = datetime.now(tz=timezone)
    tj0 = datetime(2022, 6, 16)
    tj0 = timezone.localize(tj0)
    tj = abs((now-tj0).days)
    return tj


bot.run(TOKEN)
