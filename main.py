import logging
import os
import platform
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
from colorama import init, Fore, Style

# Initialize colorama for colored console output
init()

# Load environment variables from a .env file
load_dotenv()

# Create a Logs directory if it doesn't exist
if not os.path.exists("Logs"):
    os.makedirs("Logs")
    
# Configure logging to write log messages to a file
logging.basicConfig(filename='Logs/bot.log', level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')

# Define a custom bot class that inherits from commands.Bot
class DevGroundZeroBot(commands.Bot):
    def __init__(self):
        super().__init__(intents=nextcord.Intents.all(), help_command=None)
        self.guild_id = int(os.getenv('GUILD_ID'))
        
    async def on_ready(self):
        # Print bot information to the console when the bot is ready
        print(f'{Fore.GREEN}Logged in as: {self.user.name}#{self.user.discriminator}{Style.RESET_ALL}')
        logging.info(f'Logged in as: {self.user.name}#{self.user.discriminator}')
        print(f'{Fore.GREEN}Running on: {platform.system()} {platform.release()} ({platform.version()}){Style.RESET_ALL}')
        logging.info(f'Running on: {platform.system()} {platform.release()} ({platform.version()})')
        print(f'{Fore.GREEN}Python: {platform.python_version()}{Style.RESET_ALL}')
        logging.info(f'Python: {platform.python_version()}')
        print(f'{Fore.GREEN}Nextcord: {nextcord.__version__}{Style.RESET_ALL}')
        print(f'{Fore.GREEN}Bot is ready!{Style.RESET_ALL}')
        logging.info('Bot is ready!')
        print(f'{Fore.BLUE}==============================={Style.RESET_ALL}')
        
        # Get the update channel by ID and send an embed message
        channel = self.get_channel(int(os.getenv('UPDATE_CHANNEL_ID')))
        update_embed = nextcord.Embed(title='Bot is ready!',
                                      description=f'Logged in as: {self.user.name}#{self.user.discriminator}',
                                      color=nextcord.Color.dark_green())
        update_embed.add_field(name='Running on:', value=f'{platform.system()} {platform.release()} ({platform.version()})', inline=False)
        update_embed.add_field(name='Python:', value=f'{platform.python_version()}', inline=False)
        update_embed.add_field(name='Nextcord:', value=f'{nextcord.__version__}', inline=False)
        update_embed.set_footer(text=f'Latency: {round(self.latency * 1000)}ms')
        update_embed.set_image(url=self.user.avatar.url)
        await channel.send(embed=update_embed)
        
        # Set the bot's presence (activity)
        await self.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name='The DevGroundZero Discord!'))
        
        # Load all cogs from the Cogs directory
        for filename in os.listdir('./Cogs'):
            if filename.endswith('.py'):
                try:
                    self.load_extension(f'Cogs.{filename[:-3]}')
                    print(f'{Fore.GREEN}Loaded Extension: {filename[:-3]}{Style.RESET_ALL}')
                    print(f'{Fore.BLUE}==============================={Style.RESET_ALL}')
                    logging.info(f'Loaded Extension: {filename[:-3]}')
                except Exception as e:
                    print(f'{Fore.RED}Failed to load Extension: {filename[:-3]}{Style.RESET_ALL}')
                    logging.error(f'Failed to load Extension: {filename[:-3]}: {str(e)}')
        
client = DevGroundZeroBot()
client.run(os.getenv('BOT_TOKEN'))