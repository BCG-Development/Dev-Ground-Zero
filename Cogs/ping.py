import os
import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction
from colorama import init, Fore, Style
from dotenv import load_dotenv

init()

load_dotenv()

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.guild_id = int(os.getenv('GUILD_ID'))
        self.dgz_member_role_id = int(os.getenv('DGZ_MEMBER_ROLE_ID'))
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.GREEN}Ping Cog is ready!{Style.RESET_ALL}')
        
    @nextcord.slash_command(name='ping', description='Check the bot\'s ping.')
    @application_checks.has_role('DGZ Members')
    async def ping(self, interaction: Interaction):
        ping_embed = nextcord.Embed(title='Bot\'s Ping', color=nextcord.Color.dark_green())
        ping_embed.add_field(name='My Latency is:', value=f"{round(self.client.latency * 1000)}ms")
        ping_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=ping_embed, ephemeral=True)
        
    @ping.error
    async def ping_error(self, interaction: Interaction, error: application_checks.ApplicationMissingAnyRole):
        ping_error_embed = nextcord.Embed(title='Error!', description='You do not have the required role to use this command.', color=nextcord.Color.dark_red())
        ping_error_embed.add_field(name='Required Role:', value=f'<@&{self.dgz_member_role_id}>', inline=False)
        ping_error_embed.add_field(name=str(error), value='Please contact a staff member.', inline=False)
        ping_error_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=ping_error_embed, ephemeral=True)
        
def setup(client):
    client.add_cog(Ping(client))
