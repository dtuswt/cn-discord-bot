import discord
from discord.ext.commands import Bot
from discord.ext import commands
from pathlib import Path
import sys, signal

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
    print("Changed status.")

@client.event
async def on_command_error(error, ctx):
    print("ERROR:", error)

@client.command(pass_context=True)
async def inside(ctx, *args):
    if len(args) < 1:
        await client.say("Wrong use of the commmand. Try `/inside connect` or `/inside connect s123456` instead.")

    cmd = args[0].lower()

    if cmd == "connect":
        await connect(ctx, args[1:])
    else:
        await client.say(f"Unknown command '{cmd}'.'")

async def connect(ctx, args):
    if len(args) == 1:
        studyno = get_study_no(args[0])
        if studyno == None:
            await client.say(f"The given study number ({args[0]}) is invalid. Try agian.")
            return
        await client.say(f"Using study number '{studyno}' and username {ctx.message.author}.'")
    elif len(args) == 0:
        await client.say(f"Will connect you to the server with username: {ctx.message.author}.")

def get_study_no(s):
    if len(s) == 7 and s[1:].isdigit():
        if s.lower()[0] != 's':
            return None
        return s
    elif len(s) == 6 and s.isdigit():
        return  f"s{int(s)}"
    else:
        return None

def signal_handler(sig, frame):
    client.close()
    exit(0)

if __name__ == "__main__":
    print("Using token from 'token.txt'")
    client.run(read_token())
