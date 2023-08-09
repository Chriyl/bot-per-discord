import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.typing = True
intents.presences = True

load_dotenv(dotenv_path="credential.env")

TOKEN = os.environ.get("TOKEN")

client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print(f'Bot is ready. Logged in as {client.user.name}')

@client.command()
async def ping(ctx):
    await ctx.send("pong")

client.run(TOKEN)