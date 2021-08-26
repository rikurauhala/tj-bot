def valid(ctx, contingent, duration):
    return valid_contingent(ctx, contingent) and valid_duration(ctx, duration)


async def valid_contingent(ctx, contingent):
    """Validate contingent."""
    contingents = ["1/21", "2/21"]
    if contingent not in contingents:
        await ctx.send("Virheellinen saapumiserä")
        return False
    return True


async def valid_duration(ctx, duration):
    """Validate duration."""
    durations = [165, 255, 347]
    if duration not in durations:
        await ctx.send("Virheellinen palvelusaika")
        return False
    return True
