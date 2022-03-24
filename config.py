import discord,os,json,dotenv


dotenv.load_dotenv()
BOT_NAME = "Axle"
BOT_DESCRIPTION = "a bot for the Gen Z"
BOT_INTENTS = discord.Intents.all()
BOT_PREFIX = "-"
BOT_TOKEN = os.getenv("TOKEN")



def blacklisted():
    with open("./blacklisted.json", "r")as fp:
        return json.load(fp)