from discord.ext import commands
import requests
import json
import os
from requests.models import Response

class GrandExchange(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ge(self, ctx, *, itemname):
        with open('cogs/runescape-item-id.json') as f:
            data = json.load(f)
        
        inputid = data[itemname]

        response = requests.get(f'https://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={inputid}')

        data = response.json()
        data.get('price')

        await ctx.send(data["item"]["current"]["price"])

def setup(client):
    client.add_cog(GrandExchange(client))