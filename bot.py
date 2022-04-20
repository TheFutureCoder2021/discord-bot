import discord 
from discord.ext import commands 
from discord.ext.bridge import *

from config import *
import logging 

bot = commands.Bot(commands.when_mentioned_or(BOT_PREFIX),description=BOT_DESCRIPTION,intents=BOT_INTENTS)



@bot.event
async def on_ready():
    print(f"{bot.user.name} is Online\n{bot.user.id}\n------------------")



@bot.command(name="ping")
async def ping(ctx:commands.Context):
    await ctx.send("Pong!")
def main():
    logging.basicConfig(level=logging.INFO)
    bot.run(BOT_TOKEN)
    #load_cogs(client=bot)


if __name__ in "__main__":
    main()



