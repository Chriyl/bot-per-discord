import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import utils

intents = discord.Intents.default()
intents.typing = True
intents.presences = True

load_dotenv(dotenv_path=r"C:\Users\chris\OneDrive\Desktop\cred\credentials.env")
# questo é il path delle credenziali, le credenziali
# non vanno postate su github ne su git il bot le disattiva auto quindi vengono salvate in un file nel tuo pc e messo il file in fase di
# production e nel mio server in fase di deploy

TOKEN: str = os.environ.get("TOKEN") # qui prende il token come variabile d'ambiente
PATH_TEXT: str = os.environ.get("PATH_TEXT_FILE")



bot = commands.Bot(command_prefix="!", intents=intents) # specifici l'intenti del bot


@bot.event # questo é il messaggio che esce in console se il bot va online
async def on_ready() -> None:
    print(f'Bot is ready. Logged in as {bot.user.name}')



@bot.command() # questo é il ping del bot
async def ping(ctx)  -> None: # ctx é l'argomento di colui che ha mandato il messaggio ed é un oggetto quindi ha metodi e elementi
    await ctx.send("pong")

@bot.command()
async def chiSono(ctx) -> None:
    author: str = ctx.author.mention
    channel: str = ctx.channel
    await ctx.reply(f"sei {author} e stai scrivendo in {channel}")

@bot.command()
async def gatto(ctx) -> None:
    await ctx.send(file = utils.prendiFoto())

@bot.command()
async def frase(ctx, arg: str) -> None:

    frase: str = utils.prendiFrase(PATH_TEXT)
    frase = utils.formattaInsulto(frase, arg)
    await ctx.send(frase)

@bot.command()
async def Sorgente(ctx) -> None:
    ctx.send(r"https://github.com/Chriyl/bot-per-discord")


bot.run(TOKEN) # qui il bot runna