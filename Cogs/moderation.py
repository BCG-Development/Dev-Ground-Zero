import os
from datetime import datetime
import nextcord
from nextcord.ext import commands, application_checks
from colorama import init, Fore, Style
from dotenv import load_dotenv

init()

load_dotenv()

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.moderator_role_id = int(os.getenv('MODERATOR_ROLE_ID'))
        self.server_manager_role_id = int(os.getenv('SERVER_MANAGER_ROLE_ID'))
        self.muted_role_id = int(os.getenv('MUTED_ROLE_ID'))
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.GREEN}Moderation Cog is ready!{Style.RESET_ALL}')
        print(f'{Fore.BLUE}==============================={Style.RESET_ALL}')
                    
    @nextcord.slash_command(name='purge', description='Purge messages from a channel', guild_ids=[int(os.getenv('GUILD_ID'))])
    @application_checks.has_any_role('Server Moderator', 'Server Manager' )
    async def purge(self, interaction: nextcord.Interaction, amount: int):
        purge_embed = nextcord.Embed(title='Purge', description=f'Purged {amount} messages from {interaction.channel.mention}', color=nextcord.Color.dark_green())
        purge_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(embed=purge_embed, ephemeral=True, delete_after=5)
        
    @purge.error
    async def purge_error(self, interaction: nextcord.Interaction, error: application_checks.ApplicationMissingRole):
        purge_error_embed = nextcord.Embed(title='Error', description='You do not have permission to use this command!', color=nextcord.Color.dark_red())
        purge_error_embed.add_field(name='Required Role\'s:', value=f'<@&{self.moderator_role_id}> or <@&{self.server_manager_role_id}>', inline=False)
        purge_error_embed.add_field(name=str(error), value='Please contact a staff member.', inline=False)
        purge_error_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=purge_error_embed, ephemeral=True, delete_after=5)
        
    @nextcord.slash_command(name='kick', description='Kick a member from the server', guild_ids=[int(os.getenv('GUILD_ID'))])
    @application_checks.has_any_role('Server Moderator', 'Server Manager')
    async def kick(self, interaction: nextcord.Interaction, member: nextcord.Member, *, reason: str):
        kick_embed = nextcord.Embed(title='Kick', description=f'Kicked {member.mention} for {reason}', color=nextcord.Color.dark_green())
        kick_embed.set_thumbnail(url=self.client.user.avatar.url)
        await member.kick(reason=reason)
        await interaction.response.send_message(embed=kick_embed, ephemeral=True, delete_after=5)
        
    @kick.error
    async def kick_error(self, interaction: nextcord.Interaction, error: application_checks.ApplicationMissingRole):
        kick_error_embed = nextcord.Embed(title='Error', description='You do not have permission to use this command!', color=nextcord.Color.dark_red())
        kick_error_embed.add_field(name='Required Role\'s:', value=f'<@&{self.moderator_role_id}> or <@&{self.server_manager_role_id}>', inline=False)
        kick_error_embed.add_field(name=str(error), value='Please contact a staff member.', inline=False)
        kick_error_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=kick_error_embed, ephemeral=True, delete_after=5)
        
    @nextcord.slash_command(name='ban', description='Ban a member from the server', guild_ids=[int(os.getenv('GUILD_ID'))])
    @application_checks.has_any_role('Server Moderator', 'Server Manager')
    async def ban(self, interaction: nextcord.Interaction, member: nextcord.Member, *, reason: str):
        ban_embed = nextcord.Embed(title='Ban', description=f'Banned {member.mention} for {reason}', color=nextcord.Color.dark_green())
        ban_embed.set_thumbnail(url=self.client.user.avatar.url)
        await member.ban(reason=reason)
        await interaction.response.send_message(embed=ban_embed, ephemeral=True, delete_after=5)
        
    @ban.error
    async def ban_error(self, interaction: nextcord.Interaction, error: application_checks.ApplicationMissingRole):
        ban_error_embed = nextcord.Embed(title='Error', description='You do not have permission to use this command!', color=nextcord.Color.dark_red())
        ban_error_embed.add_field(name='Required Role\'s:', value=f'<@&{self.moderator_role_id}> or <@&{self.server_manager_role_id}>', inline=False)
        ban_error_embed.add_field(name=str(error), value='Please contact a staff member.', inline=False)
        ban_error_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=ban_error_embed, ephemeral=True, delete_after=5)
        
    @nextcord.slash_command(name='unban', description='Unban a member from the server', guild_ids=[int(os.getenv('GUILD_ID'))])
    @application_checks.has_any_role('Server Moderator', 'Server Manager')
    async def unban(self, interaction: nextcord.Interaction, member: nextcord.Member, *, reason: str):
        unban_embed = nextcord.Embed(title='Unban', description=f'Unbanned {member.mention} for {reason}', color=nextcord.Color.dark_green())
        unban_embed.set_thumbnail(url=self.client.user.avatar.url)
        await member.unban(reason=reason)
        await interaction.response.send_message(embed=unban_embed, ephemeral=True, delete_after=5)
        
    @unban.error
    async def unban_error(self, interaction: nextcord.Interaction, error: application_checks.ApplicationMissingRole):
        unban_error_embed = nextcord.Embed(title='Error', description='You do not have permission to use this command!', color=nextcord.Color.dark_red())
        unban_error_embed.add_field(name='Required Role\'s:', value=f'<@&{self.moderator_role_id}> or <@&{self.server_manager_role_id}>', inline=False)
        unban_error_embed.add_field(name=str(error), value='Please contact a staff member.', inline=False)
        unban_error_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=unban_error_embed, ephemeral=True, delete_after=5)
        
    @nextcord.slash_command(name='warn', description='Warn a member from the server', guild_ids=[int(os.getenv('GUILD_ID'))])
    @application_checks.has_any_role('Server Moderator', 'Server Manager')
    async def warn(self, interaction: nextcord.Interaction, member: nextcord.Member, *, reason: str):
        warn_embed = nextcord.Embed(title='Warn', description=f'Warned {member.mention} for {reason}', color=nextcord.Color.dark_green())
        warn_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=warn_embed, ephemeral=False, delete_after=5)
        
    @warn.error
    async def warn_error(self, interaction: nextcord.Interaction, error: application_checks.ApplicationMissingRole):
        warn_error_embed = nextcord.Embed(title='Error', description='You do not have permission to use this command!', color=nextcord.Color.dark_red())
        warn_error_embed.add_field(name='Required Role\'s:', value=f'<@&{self.moderator_role_id}> or <@&{self.server_manager_role_id}>', inline=False)
        warn_error_embed.add_field(name=str(error), value='Please contact a staff member.', inline=False)
        warn_error_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=warn_error_embed, ephemeral=True, delete_after=5)
        
    @nextcord.slash_command(name='warns', description='Check a member\'s warns', guild_ids=[int(os.getenv('GUILD_ID'))])
    @application_checks.has_any_role('Server Moderator', 'Server Manager')
    async def warns(self, interaction: nextcord.Interaction, member: nextcord.Member):
        warns_embed = nextcord.Embed(title='Warns', description=f'Warns for {member.mention}', color=nextcord.Color.dark_green())
        warns_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=warns_embed, ephemeral=True)
        
    @warns.error
    async def warns_error(self, interaction: nextcord.Interaction, error: application_checks.ApplicationMissingRole):
        warns_error_embed = nextcord.Embed(title='Error', description='You do not have permission to use this command!', color=nextcord.Color.dark_red())
        warns_error_embed.add_field(name='Required Role\'s:', value=f'<@&{self.moderator_role_id}> or <@&{self.server_manager_role_id}>', inline=False)
        warns_error_embed.add_field(name=str(error), value='Please contact a staff member.', inline=False)
        warns_error_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=warns_error_embed, ephemeral=True, delete_after=5)
        
def setup(client):
    client.add_cog(Moderation(client))