import time
import discord
from discord.ext import commands

token = "MTI5MjA5NTI5NDU0ODQ3NTk0NA.GxNavU.Bj4G7lYFCBxtnWyG82L5aSJi1GHgAAU_AGtmGA"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.tree.command()
async def mutiplication(interation: discord.Interaction, a: int, b: int):
    await interation.response.send_message(f"{a} x {b} = {a * b}")

@bot.tree.command()
async def repete(interaction: discord.Interaction, nombre: int, message: str):
    await interaction.response.send_message(message)
    for _ in range(1, nombre):
        await interaction.followup.send(message)

@bot.tree.command()
async def attends(interation: discord.Interaction, secondes: int):
    await interation.response.defer()
    time.sleep(secondes)
    await interation.followup.send("J'ai fini !")

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commande(s) synchronisée(s)")
    except Exception as e:
        print (e)

def main():
    bot.run(token=token)

if __name__ == '__main__':
    main()