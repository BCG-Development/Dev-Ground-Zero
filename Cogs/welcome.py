import os
import nextcord
from nextcord.ext import commands
from colorama import init, Fore, Style
from dotenv import load_dotenv
import json

init()

load_dotenv()

class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.welcome_channel_id = int(os.getenv('WELCOME_CHANNEL_ID'))
        self.rules_channel_id = int(os.getenv('RULES_CHANNEL_ID'))
        self.dgz_member_role_id = int(os.getenv('DGZ_MEMBER_ROLE_ID'))
        self.user_db_path = 'Databases/user_db.json'

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.GREEN}Welcome Cog is ready!{Style.RESET_ALL}')
        print(f'{Fore.BLUE}==============================={Style.RESET_ALL}')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Update user database on member join
        with open(self.user_db_path, 'r') as user_db_file:
            user_db = json.load(user_db_file)
        user_db[member.id] = {'name': member.name, 'discriminator': member.discriminator}

        with open(self.user_db_path, 'w') as user_db_file:
            json.dump(user_db, user_db_file, indent=4)
        print(f'{Fore.GREEN}Updated user database for member join: {member.name}#{member.discriminator}{Style.RESET_ALL}')

        # Welcome the new member and add the role
        welcome_channel = self.client.get_channel(self.welcome_channel_id)
        rules_channel = self.client.get_channel(self.rules_channel_id)
        dgz_member_role = member.guild.get_role(self.dgz_member_role_id)
        await member.add_roles(dgz_member_role)
        welcome_embed = nextcord.Embed(title=f'Welcome to the DevGroundZero Discord!',
                                       description=f'{member.mention} Please read the rules in {rules_channel.mention} and enjoy your stay!',
                                       color=nextcord.Color.dark_green())
        welcome_embed.add_field(name=f'You are member #{member.guild.member_count}', value=f'You joined {member.joined_at.strftime("%A, %B %d, %Y at %I:%M %p")}')
        welcome_embed.set_thumbnail(url=self.client.user.avatar.url)
        welcome_embed.set_footer(text=f'{member.guild.name}', icon_url=member.guild.icon.url)
        welcome_embed.timestamp = nextcord.utils.utcnow()
        await welcome_channel.send(embed=welcome_embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # Update user database on member remove
        with open(self.user_db_path, 'r') as user_db_file:
            user_db = json.load(user_db_file)

        if member.id in user_db:
            del user_db[member.id]

            with open(self.user_db_path, 'w') as user_db_file:
                json.dump(user_db, user_db_file, indent=4)
            print(f'{Fore.GREEN}Updated user database for member remove: {member.name}#{member.discriminator}{Style.RESET_ALL}')

def setup(client):
    client.add_cog(Welcome(client))
