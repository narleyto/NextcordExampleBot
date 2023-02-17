import nextcord
from nextcord.ext import commands
from nextcord import slash_command, Interaction

class Ping(commands.Cog, name="Bot"):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog "Ping Command" has been loaded.')

    @nextcord.slash_command(name="ping", description="ping")
    async def ping(self, interaction: nextcord.Interaction):
        
        embed = nextcord.Embed(
            title="Discord Bot",
            description=f"**Ping: `{round(self.bot.latency * 1000)}`ms**"
        )
        embed.set_footer(text="Discord Bot",icon_url=self.bot.user.display_avatar)
        await interaction.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Ping(bot))

