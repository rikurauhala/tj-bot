from discord.ext import commands


class Aamuja(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="aamuja", help="Toivottaa aamuja")
    async def aamuja(self, ctx):
        await ctx.send("Aamuja!")


def setup(bot):
    bot.add_cog(Aamuja(bot))
