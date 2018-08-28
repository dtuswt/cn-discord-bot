import discord
from discord.ext.commands import Bot
from discord.ext import commands
from pathlib import Path
import sys

discord_client = discord.Client()
bot_prefix="/"
client = commands.Bot(command_prefix=bot_prefix)

def read_token():
    filename = "token.txt"
    tokenFile = Path(f'./{filename}')
    if tokenFile.exists() == False:
        print(f"Token file ({filename}) does not exist. Create it and populate it with the token for the Discord Bot and try again.", file=sys.stderr)
        sys.exit(-1)
    
    with open(tokenFile, "r") as tokenFile:
        return tokenFile.readline().replace("\n", "")

@client.event
async def on_ready():
    print("Bot is online")
    print(f"Name: {client.user.name}")
    print(f"ID: {client.user.id}")

    await client.change_presence(game=discord.Game(name="Development in VSCode"))

# @client.command(pass_context=True)
# async def test(ctx):
#     await client.send("Test!")
#     # await ctx.send(f"Hello, {ctx.author}. Send sent a message from {ctx.guild}!")

@client.command()
async def foo(ctx, arg):
    await ctx.send(arg)

if __name__ == "__main__":
    print("Using token from 'token.txt'")
    client.run(read_token())