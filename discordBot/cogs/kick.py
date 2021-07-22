import discord
from discord.ext import commands

class Kick(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)
        await ctx.send(f'kicked {member.mention}')

def setup(client):
    client.add_cog(Kick(client))