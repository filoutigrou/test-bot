import discord
from discord.ext import commands

token = "MTI5MjA5NTI5NDU0ODQ3NTk0NA.GxNavU.Bj4G7lYFCBxtnWyG82L5aSJi1GHgAAU_AGtmGA"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.hybrid_command()
async def ping(ctx):
    await ctx.send("Pong !")

@bot.hybrid_command()
async def soustraire(ctx, a: int, b: int):
    await ctx.send(f"La difference entre {a} et {b} est {a - b}")

@bot.hybrid_command()
async def note(ctx, *, note: str):
    await ctx.send(f"note : {note} enregistrée !")

@bot.event
async def on_ready():
    await bot.tree.sync()

bot.run(token=token)