import discord, dotenv, os
from datetime import date
from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command(name="aamuja", help="Huutelee aamuja")
async def aamuja(ctx):
    await ctx.send("Aamuja!")

@bot.command(name="tj", help="Tänään jäljellä")
async def tj(ctx):
    today = date.today()
    # Saapumiserä I/21
    tj0 = date(2021, 12, 16)
    tj = abs((today-tj0).days)
    await ctx.send(f"Tänään jäljellä: **{tj}** aamua")

bot.run(TOKEN)