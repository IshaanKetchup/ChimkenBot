import csv
import discord
from discord.ext import commands
import asyncio
import random
from discord import Embed

class Joker(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Joker Cog Online')

    @commands.command(aliases = ['lol', 'lmao'])
    async def funny(self, ctx):
        file = open('jokes.csv', 'r')
        alljokes = file.readlines()
        n = random.randint(0, len(alljokes)-1)
        joke = alljokes[n].split(',')
        colour = discord.Color.random()
        emb = Embed(title= joke[0], colour = colour)
        sendjoke = await (ctx.reply(embed = emb))
        await asyncio.sleep(3)
        emb = Embed(title = joke[0], description= joke[1], colour = colour)
        emb.set_footer(text='hehehe')
        await sendjoke.edit(embed = emb)
        
def setup(bot):
    bot.add_cog(Joker(bot))
