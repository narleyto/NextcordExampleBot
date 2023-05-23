import nextcord
from nextcord.ext import commands


@commands.Cog.listener()
async def on_guild_join(guild:nextcord.Guild): 
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed = nextcord.Embed(
                title="Hi!",
                description="",
            )
            await channel.send(embed=embed)
        break
     
def setup(_bot):
    global bot
    bot = _bot
    return on_guild_join