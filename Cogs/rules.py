import os
import nextcord
from nextcord.ext import commands, application_checks
from colorama import init, Fore, Style
from dotenv import load_dotenv

init()

load_dotenv()

rules_text = """

Welcome to Dev Ground Zero, your hub for learning and development in the world of coding. To ensure a positive and productive community, please adhere to the following rules:

🤝 **Respect Each Other**
   - Treat fellow members with respect, kindness, and patience.
   - Avoid offensive language, personal attacks, and discrimination based on any personal attributes.

🚀 **Stay on Topic**
   - Keep discussions and questions related to coding, programming languages, tools, and tech-related subjects.
   - Use appropriate channels for different topics. If unsure, ask a moderator for guidance.

🚫 **No Spam or Self-Promotion**
   - Refrain from excessive self-promotion, advertising, or spamming.
   - Share your projects, but ensure they are relevant and don't overwhelm the channel.

📌 **Use Appropriate Channels**
   - Post in the correct channels to maintain organized discussions.
   - Seek guidance from moderators if you're uncertain about where your topic belongs.

📝 **No Plagiarism**
   - Do not share or request copyrighted or plagiarized content.
   - Always give credit to original sources when sharing information or code.

👔 **Keep It SFW**
   - This is a safe-for-work server. Refrain from sharing explicit or NSFW content, including text, images, or links.

📚 **No Cheating or Academic Dishonesty**
   - Do not engage in or promote cheating, plagiarism, or any form of academic dishonesty.
   - Encourage learning through honest effort and collaboration.

❓ **Ask Thoughtful Questions**
   - When seeking help, provide context, error messages, and code snippets.
   - Avoid asking overly broad or vague questions.

🚫 **No Hate Speech or Trolling**
   - Hate speech, trolling, or disruptive behavior will not be tolerated.
   - Constructive criticism is welcome, but avoid hurtful or malicious intent.

🔒 **Respect Privacy**
   - Protect your privacy and the privacy of others.
   - Do not share personal information, including real names, addresses, or private details.

Violation of these rules may result in warnings, mutes, or bans, depending on the severity of the offense. Our aim is to create a supportive community for learning and growth in the coding world. Let's collaborate and grow together! 🚀

[Dev Ground Zero Discord](https://discord.gg/VXgVNpcR)
"""

class Rules(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.owner_role_id = int(os.getenv('OWNER_ROLE_ID'))
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.GREEN}Rules Cog is ready!{Style.RESET_ALL}')
        print(f'{Fore.BLUE}==============================={Style.RESET_ALL}')
        
    @nextcord.slash_command(name='rules', description='Display the rules of the server', guild_ids=[int(os.getenv('GUILD_ID'))])
    @application_checks.has_role('Owner')
    async def send_rules(self, interaction: nextcord.Interaction):
        rules_embed = nextcord.Embed(title='📜 **Dev Ground Zero Discord Rules**', description=rules_text, color=nextcord.Color.dark_green())
        rules_embed.set_image(url='https://cdn.discordapp.com/attachments/1170491625299005492/1171018473535705118/R.png?ex=655b26f0&is=6548b1f0&hm=dc2897221061b7da3c14dd1a2f8a6b2bad4b45da60b035f64e2515ea07c07676&')
        await interaction.response.send_message(embed=rules_embed, ephemeral=False)
        
    @send_rules.error
    async def send_rules_error(self, interaction: nextcord.Interaction, error: application_checks.ApplicationMissingRole):
        send_rules_error_embed = nextcord.Embed(title='Error', description='You do not have permission to use this command!', color=nextcord.Color.dark_red())
        send_rules_error_embed.add_field(name='Required Role:', value=f'<@&{self.owner_role_id}>', inline=False)
        send_rules_error_embed.add_field(name=str(error), value='Please contact a staff member.', inline=False)
        send_rules_error_embed.set_thumbnail(url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=send_rules_error_embed, ephemeral=True, delete_after=5)

def setup(client):
    client.add_cog(Rules(client))