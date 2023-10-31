import asyncio
import os
import platform
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
from colorama import init, Fore, Style

init()

load_dotenv()

class DevGroundZeroBot(commands.Bot):
    def __init__(self):
        super().__init__(intents=nextcord.Intents.all(), help_command=None)
        self.guild_id = int(os.getenv('GUILD_ID'))
        
    async def on_ready(self):
        # Print bot information to the console when the bot is ready
        print(f'{Fore.GREEN}Logged in as: {self.user.name}#{self.user.discriminator}{Style.RESET_ALL}')
        print(f'{Fore.GREEN}Running on: {platform.system()} {platform.release()} ({platform.version()}){Style.RESET_ALL}')
        print(f'{Fore.GREEN}Python: {platform.python_version()}{Style.RESET_ALL}')
        print(f'{Fore.GREEN}Nextcord: {nextcord.__version__}{Style.RESET_ALL}')
        print(f'{Fore.GREEN}Bot is ready!{Style.RESET_ALL}')
        print(f'{Fore.BLUE}==============================={Style.RESET_ALL}')
        
        channel = self.get_channel(int(os.getenv('UPDATE_CHANNEL')))
        update_embed = nextcord.Embed(title='Bot is ready!',
                                      description=f'Logged in as: {self.user.name}#{self.user.discriminator}',
                                      color=nextcord.Color.dark_green())
        update_embed.add_field(name='Running on:', value=f'{platform.system()} {platform.release()} ({platform.version()})', inline=False)
        update_embed.add_field(name='Python:', value=f'{platform.python_version()}', inline=False)
        update_embed.add_field(name='Nextcord:', value=f'{nextcord.__version__}', inline=False)
        update_embed.set_footer(text=f'Latency: {round(self.latency * 1000)}ms')
        update_embed.set_image(url=self.user.avatar.url)
        await channel.send(embed=update_embed)
        
        await self.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name='The DevGroundZero Discord!'))
        
        
    async def run_bot(self):
        await self.start(os.getenv('BOT_TOKEN'))
        await self.connect()
        
if __name__ == '__main__':
    # Create an instance of the DevGroundZero class
    client = DevGroundZeroBot()
    
    # Run the bot asynchronously using asyncio
    asyncio.run(client.run_bot())