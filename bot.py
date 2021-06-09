import discord, dotenv, os
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

bot.run(TOKEN)