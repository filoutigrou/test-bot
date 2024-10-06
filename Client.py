import discord

token = "MTI5MjA5NTI5NDU0ODQ3NTk0NA.GxNavU.Bj4G7lYFCBxtnWyG82L5aSJi1GHgAAU_AGtmGA"

client = discord.Client(intents=discord.Intents.all())

client.run(token=token)
