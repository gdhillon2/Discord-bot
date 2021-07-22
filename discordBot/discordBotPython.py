import discord
import random
import os

from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)

#events
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('compromised'))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

#clear messages
@client.command()
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount)

#loads cog
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

#unloads cog
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

#reloads cog
@client.command()
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')

#loads all py files like a cog
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODY3NDA1OTQ0NDQxNjY3NjE0.YPgovA.SmONP4vy-VIvanP7MG0nkEZJkgw')