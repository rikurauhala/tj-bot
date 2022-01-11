from datetime import datetime

from pytz import timezone

timezone = timezone("Europe/Helsinki")


def count_tj(contingent, duration):
    """Count tj based on contingent and duration."""
    now = datetime.now(tz=timezone)
    tj0 = get_tj0(contingent, duration)
    tj = -1*(now-tj0).days
    return tj


def get_tj0(contingent, duration):
    """Get tj0 date based on contingent and duration."""
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
    elif contingent == "1/22":
        if duration == 165:
            tj0 = datetime(2022, 6, 16)
        elif duration == 255:
            tj0 = datetime(2022, 9, 14)
        else:
            tj0 = datetime(2022, 12, 15)
    tj0 = timezone.localize(tj0)
    return tj0
