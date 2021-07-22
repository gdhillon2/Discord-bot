from discord.ext import commands
import requests

class FoxAPI(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fox(self, ctx):
        response = requests.get("https://randomfox.ca/floof")
        fox = response.json()
        await ctx.send(fox['image'])


def setup(client):
    client.add_cog(FoxAPI(client))