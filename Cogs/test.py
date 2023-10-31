import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from colorama import init, Fore, Style

# Initialize colorama for colored console output
init()

# Test Cog
class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.BLUE}Ping Cog is ready!{Style.RESET_ALL}')
        
    @nextcord.slash_command(name='ping', description='Check the bots ping.')
    async def ping(self, interaction: Interaction):
        ping_embed = nextcord.Embed(title='Bots Ping')
        ping_embed.add_field(name='My Latency is:', value=f"{round(self.client.latency * 1000)}ms")
        await interaction.response.send_message(embed=ping_embed)
        
def setup(client):
    client.add_cog(Ping(client))