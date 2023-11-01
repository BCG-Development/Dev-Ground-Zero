import os
import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction
from colorama import init, Fore, Style
from dotenv import load_dotenv

init()

load_dotenv()

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.guild_id = int(os.getenv('GUILD_ID'))
        self.owner_role_id = int(os.getenv('OWNER_ROLE_ID'))
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.GREEN}Owner Cog is ready!{Style.RESET_ALL}')
        
def setup(client):
    client.add_cog(Owner(client))