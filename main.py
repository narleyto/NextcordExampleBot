import nextcord
from nextcord.ext import commands

from dotenv.main import load_dotenv
import os


bot = commands.Bot(command_prefix='.', intents=nextcord.Intents.all())

#Activity
@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nCurrent Prefix : .\n-----")    
    #activity
    await bot.change_presence(activity = nextcord.Activity(type=nextcord.ActivityType.playing, name=f"https://discord.gg/gobelsube"))
    

            
for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f"cogs.{fn[:-3]}")
            
 
load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))