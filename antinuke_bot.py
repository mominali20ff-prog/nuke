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
    await ctx.send("⚙️ Creating channels...")

    message = '''
👋 Welcome to the server!

📜 Read the rules.
💬 Be respectful.
🎉 Enjoy your stay!
'''

    for i in range(1, 51):
        channel = await ctx.guild.create_text_channel(f"general-{i}")
        await channel.send(message)

    await ctx.send("✅ Finished creating 50 channels.")

bot.run(TOKEN)
