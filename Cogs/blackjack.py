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

    @nextcord.slash_command(name='play-blackjack', description='Play a game of blackjack', guild_ids=[int(os.getenv('GUILD_ID'))])   
    async def play_blackjack(self, interaction: nextcord.Interaction):
        # Create a unique role name for the game and give permissions to the role - read_messages, send_messages, add_reactions
        role_name = f'BlackJack-{interaction.user.name}'
        role = await interaction.guild.create_role(name=role_name, permissions=nextcord.Permissions(read_messages=True, send_messages=True, add_reactions=True))
        overwrites = {
            interaction.guild.default_role: nextcord.PermissionOverwrite(read_messages=False),
            role: nextcord.PermissionOverwrite(read_messages=True, send_messages=True, add_reactions=True)
        }
        channel = await interaction.guild.create_text_channel(name=role_name, category=interaction.guild.get_channel(self.games_room_category_id), overwrites=overwrites)
        # Add the role to the user
        await interaction.user.add_roles(role)
        # Send a message to the channel
        await channel.send(f'{interaction.user.mention} has started a game of BlackJack!')
        # Send a message to the user
        await interaction.response.send_message(f'Game started in {channel.mention}!', ephemeral=True)        
          
def setup(client):
    client.add_cog(BlackJack(client))