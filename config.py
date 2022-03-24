import discord,os,json,dotenv


dotenv.load_dotenv()
BOT_NAME = "Axle"
BOT_DESCRIPTION = "a bot for the Gen Z"
BOT_INTENTS = discord.Intents.all()
BOT_PREFIX = "-"
BOT_TOKEN = os.getenv("TOKEN")



def blacklisted():
    with open("blacklisted.json", "r")as fp:
        return json.load(fp)


def load_cogs(client):
    for folder in os.listder('./cogs'):
        if os.path.exists(os.path.join('./cogs', folder, '__init__.py')):
            client.load_extension(f'cogs.{folder}')
