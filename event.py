import discord

token = "MTI5MjA5NTI5NDU0ODQ3NTk0NA.GxNavU.Bj4G7lYFCBxtnWyG82L5aSJi1GHgAAU_AGtmGA"

client = discord.Client(intents=discord.Intents.all())

@client.event 
async def on_message(message: discord.Message):
    if message.author.bot:
     return
    elif message.content.lower().startswith("bonjour"):
     await message.channel.send("Bonjour !")


@client.event 
async def on_message_delete(message: discord.Message):
     await message.channel.send(f"{message.author.name} a supprimé {message.content}")


@client.event 
async def on_message_edit(before: discord.Message, after: discord.Message):
     await after.channel.send(f"{before.content} est devenu {after.content}")

@client.event
async def on_ready():
     print("Le bot est pret !")

client.run(token=token)