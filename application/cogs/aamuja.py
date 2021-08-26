from discord.ext import commands


class Aamuja(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="aamuja", help="Toivottaa aamuja")
    async def aamuja(self, ctx):
        """Answer to being pinged by a user."""
        await ctx.send("Aamuja!")


def setup(bot):
    """Add cog to the bot."""
    bot.add_cog(Aamuja(bot))
