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
                cursor.execute("INSERT INTO records VALUES {}".format(i))
                
            await ctx.send('Inserted')
            await ctx.reply('New ChimkenBucks initialised') 
            print()
    
    @commands.command(aliases = ['bal', 'money','wallet'])
    async def cash(self, ctx, member: discord.Member = None):
        convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        cursor = convar.cursor()
        file = open('money.txt', 'r')
        gifs = file.readlines()
        n = random.randint(0, len(gifs)-1)
        url = gifs[n]
        file.close()
        if member is not None:
            id = member.id
            cursor.execute("SELECT * FROM records WHERE User_ID ={}".format(id))
            posessions = cursor.fetchall()

            cash = list(posessions)[0][1]
            passive = list(posessions)[0][2]
            cursor.execute("SELECT * FROM records WHERE User_ID ={}".format(id))
            posessions = cursor.fetchall()

            cash = list(posessions)[0][1]
            passive = list(posessions)[0][2]

            emb = Embed(title = 'Wallet', color = discord.Colour.random())
            emb.add_field(name = 'ChimkenBucks', value = f'{cash}❂')
            emb.add_field(name = 'Passive Mode', value = f'{passive}')
            emb.set_author(name = member, icon_url = ctx.author.avatar)
            emb.set_footer(text = f'Here are the ❂')
            emb.set_thumbnail(url = url)
            await ctx.reply(embed = emb)
            convar.close()
        else:
            member = ctx.author
            id = ctx.author.id
            cursor.execute("SELECT * FROM records WHERE User_ID ={}".format(id))
            posessions = cursor.fetchall()

            cash = list(posessions)[0][1]
            passive = list(posessions)[0][2]
            cursor.execute("SELECT * FROM records WHERE User_ID ={}".format(id))
            posessions = cursor.fetchall()

            cash = list(posessions)[0][1]
            passive = list(posessions)[0][2]

            emb = Embed(title = 'Wallet', color = discord.Colour.random())
            emb.add_field(name = 'ChimkenBucks', value = f'{cash}❂')
            emb.add_field(name = 'Passive Mode', value = f'{passive}')
            emb.set_author(name = member, icon_url = ctx.author.avatar)
            emb.set_footer(text = f'Here are the ❂')
            emb.set_thumbnail(url = url)
            await ctx.reply(embed = emb)
            convar.close()
    
    @commands.command(aliases = ['earn', 'job'])
    @commands.cooldown(rate = 1, per = 30, type=commands.BucketType.user)
    async def work(self,ctx):
        convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        cursor = convar.cursor()
        weight = random.randint(1,100)
        if weight >= 1 and weight <=80:
            cash = random.randint(1,50)
        else:
            cash = random.randint(50, 100)
            
        emb = Embed(description = f'You earned {cash}❂!', colour = discord.Color.random())
        emb.set_footer(text = 'cha-ching!')
        emb.set_author(name = ctx.message.author, icon_url = ctx.author.avatar)

        await ctx.reply(embed = emb)
        id = ctx.author.id
        
        cursor.execute("""UPDATE records
                                SET ChimkenBucks = ChimkenBucks+{}
                                WHERE User_ID = {}""".format(cash, id))
        convar.commit()
        convar.close()
    

        
def setup(bot):
    bot.add_cog(BucksDB(bot))
