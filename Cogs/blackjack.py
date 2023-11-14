import random
import os
from datetime import datetime
import nextcord
from nextcord.ext import commands, application_checks
from colorama import init, Fore, Style
from dotenv import load_dotenv

init()

load_dotenv()

class BlackJack(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.guild_id = int(os.getenv('GUILD_ID'))
        self.games_room_category_id = int(os.getenv('GAMES_ROOM_CATEGORY_ID'))
        self.channel = ModuleNotFoundError
        self.games = {}

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.GREEN}BlackJack Cog is ready!{Style.RESET_ALL}')
        print(f'{Fore.BLUE}==============================={Style.RESET_ALL}')       
          
def setup(client):
    client.add_cog(BlackJack(client))