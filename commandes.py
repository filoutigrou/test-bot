import discord
from discord.ext import commands

token = "MTI5MjA5NTI5NDU0ODQ3NTk0NA.GxNavU.Bj4G7lYFCBxtnWyG82L5aSJi1GHgAAU_AGtmGA"
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command(name="Bonjour_monde", aliases=['hw', 'hello_word'])
async def hello (context):
   await context.send("Hello_world")


@bot.command()
async def decompte(context, delai: int):
    await context.send("Depart dans ...")
    for i in range(delai, 0, -1):
        await context.send(i)
    await context.send("C'est parti !")


@bot.command(
   description="Repète du texte qu'on lui dit",
   brief="Répète du texte",
   help="Encore plus d'aide"
)
async def repeter(context, *, message):
    await context.send(message)


if __name__ == '__main__':
    bot.run(token=token)