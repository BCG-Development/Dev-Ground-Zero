import os
import nextcord
from nextcord.ext import commands
from colorama import init, Fore, Style
from dotenv import load_dotenv

init()

load_dotenv()

class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.welcome_channel_id = int(os.getenv('WELCOME_CHANNEL_ID'))
        self.rules_channel_id = int(os.getenv('RULES_CHANNEL_ID'))
        self.dgz_member_role_id = int(os.getenv('DGZ_MEMBER_ROLE_ID'))
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Welcome the new member and add the role
        welcome_channel = self.client.get_channel(self.welcome_channel_id)
        rules_channel = self.client.get_channel(self.rules_channel_id)
        dgz_member_role = member.guild.get_role(self.dgz_member_role_id)
        await member.add_roles(dgz_member_role)
        welcome_embed = nextcord.Embed(title=f'Welcome to the DevGroundZero Discord, {member.name}!',
                                       description=f'Please read the rules in {rules_channel.mention} and enjoy your stay!',
                                       color=nextcord.Color.dark_green())
        welcome_embed.add_field(name='Member Count:', value=f'{member.guild.member_count}', inline=False)
        welcome_embed.set_thumbnail(url=member.avatar.url)
        await welcome_channel.send(embed=welcome_embed)
        
def setup(client):
    client.add_cog(Welcome(client))