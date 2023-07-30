import discord
from discord.ext import commands
from discord.ext.pages import Paginator, Page
from discord import Embed
import sys
import os

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(intents = intents, case_insensitive = True, command_prefix = ">", help_command = None)


@bot.event
async def on_ready():
        print(f'Logged in as {bot.user}')
        print('Status Online')
        await bot.change_presence(status = discord.Status.online, activity = discord.Game('>help'))


@bot.command()
async def load(ctx, extension):
        bot.load_extension(f'cogs.{extension}', store = False)

@bot.command()
async def unload(ctx, extension):
        bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}', store = False)

for filename in os.listdir(r"cogs"):
        if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}', store = False)

        
bot.run(<DISCORD_TOKEN>) #Enter the token for your Discord bot here
def p(*args):
       sys.stdout.flush(args[0] % (len(args) > 1 and args[1:] or []))
