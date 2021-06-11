import discord, dotenv, os
from datetime import date, datetime
from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

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

@bot.command(name="lisätietoja", help="Yksityiskohtaisempaa tietoa")
async def lisatietoja(ctx):
    se = "I/21"
    pa = 347
    tj0 = datetime(2021, 12, 16)
    now = datetime.now()
    days = count_tj()
    seconds = abs(now-tj0).total_seconds()
    hours = seconds//3600
    minutes = seconds//60
    details = f"```Saapumiserä: {se} \n" \
              f"Palvelusaika: {pa} \n\n" \
              f"TÄNÄÄN JÄLJELLÄ \n" \
              f"Päivinä: {days} \n" \
              f"Tunteina: {hours:.0f} \n" \
              f"Minuutteina: {minutes:.0f} \n" \
              f"Sekunteina: {seconds:.0f}```"
    await ctx.send(details)

def count_tj():
    today = date.today()
    tj0 = date(2021, 12, 16)
    tj = abs((today-tj0).days)
    return tj

bot.run(TOKEN)