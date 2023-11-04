import os
import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction
from colorama import init, Fore, Style
from dotenv import load_dotenv

init()

load_dotenv()

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.moderator_role_id = int(os.getenv('MODERATOR_ROLE_ID'))
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.GREEN}Moderation Cog is ready!{Style.RESET_ALL}')       
        
    @nextcord.slash_command(name='purge', description='Purge messages from a channel', guild_ids=[int(os.getenv('GUILD_ID'))])
    @application_checks.has_role('Server Moderator')
    async def purge(self, interaction: nextcord.Interaction, amount: int):
        purge_embed = nextcord.Embed(title='Purge', description=f'Purged {amount} messages from {interaction.channel.mention}', color=nextcord.Color.dark_green())
        purge_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(embed=purge_embed, ephemeral=True, delete_after=5)
        
    @purge.error
    async def purge_error(self, interaction: nextcord.Interaction, error: application_checks.ApplicationMissingRole):
        purge_error_embed = nextcord.Embed(title='Error', description='You do not have permission to use this command!', color=nextcord.Color.dark_red())
        purge_error_embed.add_field(name='Required Role:', value=f'<@&{self.moderator_role_id}>', inline=False)
        purge_error_embed.add_field(name=str(error), value='Please contact a staff member.', inline=False)
        purge_error_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=purge_error_embed, ephemeral=True, delete_after=5)        
        
def setup(client):
    client.add_cog(Moderation(client))