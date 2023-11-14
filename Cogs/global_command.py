import random
import os
from datetime import datetime
import nextcord
from nextcord.ext import commands, application_checks
from colorama import init, Fore, Style
from dotenv import load_dotenv

init()

load_dotenv()

class GlobalCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.global_channel_id = int(os.getenv('UPDATE_CHANNEL_ID'))
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.GREEN}GlobalCommand Cog is ready!{Style.RESET_ALL}')
        print(f'{Fore.BLUE}==============================={Style.RESET_ALL}')
        
    @nextcord.slash_command(name='global', description='Send a global message to all servers.')
    @application_checks.is_owner()
    async def global_(self, interaction: nextcord.Interaction, *, message: str):
        global_embed = nextcord.Embed(title='Global Message', description=f'{message}', color=nextcord.Color.dark_green())
        global_embed.set_thumbnail(url=self.client.user.avatar.url)
        global_embed.set_footer(text=f'{interaction.user}', icon_url=interaction.user.avatar.url)
        global_embed.timestamp = nextcord.utils.utcnow()
        await interaction.response.send_message(embed=global_embed, ephemeral=True, delete_after=5)
        
def setup(client):
    client.add_cog(GlobalCommand(client))