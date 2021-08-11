from datetime import datetime

from pytz import timezone

from discord.ext import commands

timezone = timezone("Europe/Helsinki")


def count_tj(contingent, duration):
    now = datetime.now(tz=timezone)
    tj0 = get_tj0(contingent, duration)
    tj = -1*(now-tj0).days
    return tj


def get_tj0(contingent, duration):
    tj0 = None
    if contingent == "1/21":
        if duration == 165:
            tj0 = datetime(2021, 6, 17)
        elif duration == 255:
            tj0 = datetime(2021, 9, 15)
        else:
            tj0 = datetime(2021, 12, 16)
    elif contingent == "2/21":
        if duration == 165:
            tj0 = datetime(2021, 12, 16)
        elif duration == 255:
            tj0 = datetime(2022, 3, 16)
        else:
            tj0 = datetime(2022, 6, 16)
    tj0 = timezone.localize(tj0)
    return tj0