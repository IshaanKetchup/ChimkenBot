from discord.ext import commands
import discord
import random
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from discord import Embed

class Google(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Google Cog Online')

    @commands.command(aliases = ['s'])
    async def search(self, ctx):
        squery = str(ctx.message.content)
        finst = ''
        for x in (squery.split()[1::]):
            if x != squery.split()[-1]:
                y = x + '+'
            else:
                y = x
            finst += y
        await ctx.reply('https://www.google.com/search?q='+ finst)
    
    
    
def setup(bot):
    bot.add_cog(Google(bot))            