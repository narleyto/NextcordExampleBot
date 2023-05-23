from datetime import datetime
from colorama import Fore

white = Fore.WHITE
red = Fore.RED
green = Fore.GREEN

def error(error_code):
    time = datetime.now().strftime("%H:%M:%S")
    print(f"{white}[{time}] " + red + f"[ERROR] " + white + error_code)
    
def loaded_cog(cogname):
    print(f"{white}[COGS] {green}{cogname} loaded" + white)
    