import sqlite3
from discord.ext import commands
import discord
import random
from discord import Embed
import psycopg2
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select, Interaction
import os
import math


DATABASE_URL = os.environ['DATABASE_URL']

class BucksDB(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('BucksDB online')
    
    @commands.command()
    async def add_bucks(self, ctx):
        membercash = []

        if ctx.author.id == 572792089599803394:
            convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
            cursor = convar.cursor()

            for guild in self.bot.guilds:
                for member in guild.members:
                    membercash.append((member.id, 0, 'False'))
        
            membercash = list(set(membercash))
            await ctx.send('hello')
            
            for i in membercash:
                #await ctx.send(i)
                cursor.execute("INSERT INTO records VALUES {}".format(i))
                
            await ctx.send('Inserted')
            #convar.commit()
            await ctx.reply('New ChimkenBucks initialised') 
            print()
def setup(bot):
    bot.add_cog(BucksDB(bot))
