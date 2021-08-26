from datetime import datetime

from pytz import timezone

from discord import Embed
from discord.ext import commands

from cogs.functions.tj import count_tj, get_tj0
from cogs.functions.validation import valid

timezone = timezone("Europe/Helsinki")

DEFAULT_CONTINGENT = "2/21"
DEFAULT_DURATION = 347

class Toiminnot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tj", help="Tänään jäljellä")
    async def tj(self, ctx, contingent=DEFAULT_CONTINGENT, duration=DEFAULT_DURATION):
        if not valid(ctx, contingent, duration):
            return
        tj = count_tj(contingent, duration)
        if tj > 0:
            await ctx.send(f"Tänään jäljellä: **{tj}** aamua")
        else:
            await ctx.send(f"Tänään jäljellä: **{tj}** aamua, ohi on!")

    @commands.command(name="ohi", help="Aamuja ohi")
    async def ohi(self, ctx, contingent=DEFAULT_CONTINGENT, duration=DEFAULT_DURATION):
        if not valid(ctx, contingent, duration):
            return
        tj = count_tj(contingent, duration)
        ohi = 347-tj
        await ctx.send(f"Ohi on: **{ohi}** aamua")

    @commands.command(name="lisätietoja", help="Yksityiskohtaisempaa tietoa")
    async def lisatietoja(self, ctx, contingent=DEFAULT_CONTINGENT, duration=DEFAULT_DURATION):
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
        description = f"Saapumiserä: {contingent} \n" \
                      f"Palvelusaika: {duration}"
        progress = f"{ohi} / {duration} ({percent:.2f} %)"
        left = f"• Vuosina: {years:.2f} \n" \
               f"• Kuukausina: {months:.2f} \n" \
               f"• Viikkoina: {weeks:.1f} \n" \
               f"• Päivinä: {days:.1f} \n" \
               f"• Tunteina: {hours:.0f} \n" \
               f"• Minuutteina: {minutes:.0f} \n" \
               f"• Sekunteina: {seconds:.0f}"
        details = Embed(title="Lisätietoja", description=description, color=0x3ca45c)
        details.add_field(name="Edistyminen", value=progress, inline=False)
        details.add_field(name="Tänään jäljellä", value=left)
        details.set_footer(text=now.strftime("%d.%m.%Y %H:%M:%S"))
        await ctx.send(embed=details)


def setup(bot):
    """Add cog to the bot."""
    bot.add_cog(Toiminnot(bot))
