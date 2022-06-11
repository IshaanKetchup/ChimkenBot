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
async def servers(ctx):
        id = ctx.author.id
        channel = bot.get_channel(975378805889851482)
        if id == 572792089599803394 or id == 969540347619328031:
                guildcount = 0
                sno = 1
                gstr = ''
                for guild in bot.guilds:
                        gstr += f'{sno}. {guild.name} - {guild.id} \n'
                        sno += 1

                emb = Embed(description = f'{gstr}')

                await channel.send(embed = emb)

@bot.command()
async def load(ctx, extension):
        bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
        bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')

for filename in os.listdir(r"cogs"):
        if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')

        
bot.run(os.environ['DISCORD_TOKEN'])
def p(*args):
       sys.stdout.flush(args[0] % (len(args) > 1 and args[1:] or []))
