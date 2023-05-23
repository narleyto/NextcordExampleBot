import nextcord
from nextcord.ext import commands

from dotenv.main import load_dotenv
import os

from utils.terminal import error, loaded_cog

bot = commands.Bot(command_prefix='.', intents=nextcord.Intents.all())


@bot.event
async def on_ready():
    for command_file in os.listdir('./cogs'):
        if command_file.endswith('.py'):
            loaded_cog(cogname=command_file)
    #activity
    await bot.change_presence(activity = nextcord.Activity(type=nextcord.ActivityType.playing, name=f"ExampleBot"))
    
#command handler           
for command_file in os.listdir('./cogs'):
    if command_file.endswith('.py'):
        try:
            bot.load_extension(f"cogs.{command_file[:-3]}")
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            error(f"Failed to load command {command_file}: {exception}")
#event handler     
for file in os.listdir("events"):
    if file.endswith(".py"):
        exec("from events import " + file.replace(".py", "") + " as event")
        try:
            bot.add_listener(event.setup(bot))
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            error(f"Failed to load event {file}: {exception}")
            
if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv("DISCORD_TOKEN"))