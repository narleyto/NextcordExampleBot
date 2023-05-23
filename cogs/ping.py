import nextcord
from nextcord.ext import commands
from nextcord import slash_command, Interaction

class Ping(commands.Cog, name="Ping"):
    def __init__(self, bot):
        self.bot = bot
        
    @nextcord.slash_command(name="ping", description="ping command")
    async def ping(self, interaction: nextcord.Interaction):
        
        embed = nextcord.Embed(
            title="My Ping",
            description=f"**Ping: `{round(self.bot.latency * 1000)}`ms**"
        )
        embed.set_footer(text="ExampleBot",icon_url=self.bot.user.display_avatar)
        await interaction.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Ping(bot))

