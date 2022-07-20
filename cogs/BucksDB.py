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
        DiscordComponents(bot)             

    @commands.Cog.listener()
    async def on_ready(self):
        print('BucksDB Cog Online')
    
    @commands.Cog.listener()
    async def on_server_join(self):
        membercash = []

        convar =  psycopg2.connect(DATABASE_URL, sslmode = 'require')
        cursor =  convar.cursor()

        for guild in self.bot.guilds:
            for member in guild.members:
                membercash.append((member.id, 0))
        
        membercash = list(set(membercash))
        
        for i in membercash:
            value = i
            cursor.execute("INSERT INTO records VALUES {}".format(value))
            


        convar.commit()   
        print('New ChimkenBucks initialised') 
        print()
        convar.close()

    @commands.Cog.listener()
    async def on_member_join(self, ctx, member : discord.Member):
        convar =  psycopg2.connect(DATABASE_URL, sslmode = 'require')
        cursor =  convar.cursor()
        membercash = []

        for guild in self.bot.guilds:
            for member in guild.members:
                membercash.append((member.id, 0, 'False'))
        
        membercash = list(set(membercash))
        
        for i in membercash:
            value = i
            cursor.execute("INSERT INTO records VALUES {}".format(value))
            


        convar.commit()
        print('New ChimkenBucks initialised') 
        print()
        convar.close()
     

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            time = error.retry_after
            if time < 86400:
                seconds = time % (24 * 3600)
                hour = seconds // 3600
                seconds %= 3600
                minutes = seconds // 60
                seconds %= 60
                    
                valst = "%d:%02d:%02d" % (hour, minutes, seconds)
            else:
                days = int(math.ceil(time//86400))
                valst = f'{days} days'
            
            emb = Embed(description='*LMAO slow it down bud!*', colour = discord.Colour.random())
            emb.add_field(name = 'This command is on cooldown for `{}`'.format(valst), value = '🤕')
            await ctx.reply(embed = emb)

    @commands.command()
    async def add_bucks(self, ctx):
        membercash = []

        if ctx.message.author.id == 572792089599803394:
            convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
            cursor = convar.cursor()

            for guild in self.bot.guilds:
                for member in guild.members:
                    membercash.append((member.id, 0, 'False'))

            
            membercash = list(set(membercash))
            await ctx.send('hello')
            
            for i in membercash:
                await ctx.send(i)
                #cursor.execute("INSERT INTO records VALUES {}".format(i))
                
            await ctx.send('Inserted')
            #convar.commit()
            await ctx.reply('New ChimkenBucks initialised') 
            print()
            convar.close()

    @commands.command()
    async def reset_bucks(self, ctx):
        if ctx.message.author.id == 572792089599803394:
            membercash = []

            convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
            cursor = convar.cursor()
            for guild in self.bot.guilds:
                for member in guild.members:
                    membercash.append((member.id, 0, 'False'))
            
            membercash = list(set(membercash))
        
        
       
            cursor.execute("DROP TABLE IF EXISTS records")
            table = """CREATE TABLE records(
                        User_ID bigint NOT NULL PRIMARY KEY,
                        ChimkenBucks bigint
                        );"""
            cursor.execute(table)
            
            for i in membercash:
                value = i
                cursor.execute("INSERT INTO records VALUES {}".format(value))
                

            convar.commit()
            print('ChimkenBucks reset')
            print()
            convar.close()


    @commands.command()
    async def updating(self, ctx):
        convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        cursor = convar.cursor()

        for guild in self.bot.guilds:
                for member in guild.members:
                    cursor.execute('''UPDATE records SET passive = 'False' WHERE User_ID ={}'''.format(member.id))
            
        convar.commit()
        convar.close()
        await ctx.reply('Changes made :)')

        '''THIS IS WHERE THE DISCORD USEABLE FUNCTIONS ACTUALLY BEGIN'''       
    
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
            emb.set_author(name = member, icon_url = member.avatar_url)
            emb.set_footer(text = f'Here is their cash money ❂')
            emb.set_thumbnail(url = url)
            await ctx.reply(embed = emb)
            convar.close()
            
        elif member is None:
            id = ctx.message.author.id
            cursor.execute("SELECT * FROM records WHERE User_ID ={}".format(id))
            posessions = cursor.fetchall()

            cash = list(posessions)[0][1]
            passive = list(posessions)[0][2]

            emb = Embed(title = 'Wallet', color = discord.Colour.random())
            emb.add_field(name = 'ChimkenBucks', value = f'{cash}❂')
            emb.add_field(name = 'Passive Mode', value = f'{passive}')
            emb.set_author(name= ctx.message.author, icon_url = ctx.author.avatar_url)  
            emb.set_footer(text = f'Here is your cash money ❂')
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
        emb.set_author(name = ctx.message.author, icon_url = ctx.author.avatar_url)

        await ctx.reply(embed = emb)
        id = ctx.author.id
        
        cursor.execute("""UPDATE records
                                SET ChimkenBucks = ChimkenBucks+{}
                                WHERE User_ID = {}""".format(cash, id))
        convar.commit()
        convar.close()
    
    @commands.command()
    #@commands.cooldown(rate = 1, per = 86400, type=commands.BucketType.user)
    async def daily(self,ctx):
        emb = Embed(description = 'This function is currently disabled because _SOME_ people exploited it -_-')
        emb.set_footer(text = 'I got "cheesed". Yk who you are :p')
        await ctx.reply(embed = emb)
        '''convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        cursor = convar.cursor()
            
        emb = Embed(description = f'You received 300❂!', colour = discord.Color.random())
        emb.set_footer(text = 'cha-ching!')
        emb.set_author(name = ctx.message.author, icon_url = ctx.author.avatar_url)

        await ctx.reply(embed = emb)
        id = ctx.author.id
        
        cursor.execute("""UPDATE records
                                SET ChimkenBucks = ChimkenBucks+300
                                WHERE User_ID = {}""".format(id))
        convar.commit()
        convar.close()'''

    @commands.command()
    #@commands.cooldown(rate = 1, per = 2592000, type=commands.BucketType.user)
    async def monthly(self,ctx):
        emb = Embed(description = 'This function is currently disabled because _SOME_ people exploited it -_-')
        emb.set_footer(text ='I got "cheesed". Yk who you are :p')

        await ctx.reply(embed = emb)
        '''convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        cursor = convar.cursor()
            
        emb = Embed(description = f'You received 1500❂!', colour = discord.Color.random())
        emb.set_footer(text = 'cha-ching!')
        emb.set_author(name = ctx.message.author, icon_url = ctx.author.avatar_url)

        await ctx.reply(embed = emb)
        id = ctx.author.id
        
        cursor.execute("""UPDATE records
                                SET ChimkenBucks = ChimkenBucks+1500
                                WHERE User_ID = {}""".format(id))
        convar.commit()
        convar.close()'''

    @commands.command()
    async def g100(self, ctx):
        id = ctx.author.id
        if id == 572792089599803394 or id == 969540347619328031:

            convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
            cursor = convar.cursor()
            cursor.execute("""UPDATE records
                                    SET ChimkenBucks = ChimkenBucks+100
                                    WHERE User_ID = {}""".format( id))
            convar.commit()
            convar.close()

    @commands.command(aliases = ['rob'])
    @commands.cooldown(rate = 1, per = 1800, type=commands.BucketType.user)
    async def steal(self,ctx, member : discord.Member):
        id = member.id
        robber = ctx.author.id

        convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        cursor = convar.cursor()

        cursor.execute('SELECT * FROM records WHERE User_ID = {}'.format(robber))
        robber_data = cursor.fetchall()

        robber_passive = robber_data[0][2]

        if robber_passive == 'False':

            if id != robber:
                convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
                cursor = convar.cursor()
                
                cursor.execute('SELECT * FROM records WHERE User_ID = {}'.format(id))
                data = cursor.fetchall()

                passive = data[0][2]
                cash = data[0][1]

                if passive == 'False':
                    if cash>100:
                        weight = random.randint(1,100)
                        if weight >= 1 and weight <=80:
                            steal = random.randint(1,(cash//8))
                        else:
                            steal = random.randint(1, (cash//4))
                        
                        emb = Embed(description = f'{ctx.author.mention} stole {steal}❂ from {member.mention} 😱🤑 ')
                        emb.set_footer(text = '💲🤑')
                        await ctx.reply(embed = emb)
                    
                        cursor.execute("""UPDATE records
                                        SET ChimkenBucks = ChimkenBucks-{}
                                        WHERE User_ID = {}""".format(steal, id))
                        convar.commit()

                        cursor.execute("""UPDATE records
                                        SET ChimkenBucks = ChimkenBucks+{}
                                        WHERE User_ID = {}""".format(steal, robber))
                        convar.commit() 
                        convar.close()

                    else:
                        emb = Embed(description =  f'Give {member.mention} a break. They have only {cash}❂', colour = discord.Colour.random())
                        emb.set_footer(text = 'lmao')
                        await ctx.reply(embed = emb)
                else:
                    emb = Embed(title  = '**BEWARE, THEIF**', description = f'{member.mention} is in  `Passive Mode`. You cannot steal from them ',colour = discord.Colour.random())
                    emb.set_footer(text = 'lmao')
                    await ctx.reply(embed = emb)
            else:
                emb = Embed(description = "You can't steal from yourself, silly" )
                emb.set_footer(text = 'xD')
                await ctx.reply(embed = emb)
        else:
            emb = Embed(description = f"You are in `Passive Mode`, silly! You can't steal from {member.mention}", colour = discord.Colour.random())
            emb.set_footer(text = 'xD')
            await ctx.reply(embed = emb)

        
    @commands.command()
    @commands.cooldown(rate = 1, per = 86400, type=commands.BucketType.user)
    async def passive(self, ctx, message):
        convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        cursor = convar.cursor()
        id = ctx.author.id
        
        if message.lower() == 'true':
           
            cursor.execute("SELECT * FROM records where User_ID = {}".format(id))
            data = cursor.fetchall()
            if data[0][2] == 'True':
                emb = Embed(description = 'You are already in `Passive Mode`.', colour = discord.Color.random())
                await ctx.reply(embed = emb)

            else:
                emb = Embed(description = 'You are now in `Passive Mode`.')
                await ctx.reply(embed = emb)

                cursor.execute('''UPDATE records 
                                SET passive = 'True' 
                                WHERE User_ID ={}'''.format(id))
                convar.commit()
                convar.close()


        elif message.lower() == 'false':
            cursor.execute("SELECT * FROM records where User_ID = {}".format(id))
            data = cursor.fetchall()

            if data[0][2] =='False':
                emb = Embed(description = 'You are currently not in `Passive Mode`.', colour = discord.Color.random())
                await ctx.reply(embed = emb)
            else:
                emb = Embed(description = 'You have left `Passive Mode`.')
                await ctx.reply(embed = emb)

                cursor.execute('''UPDATE records 
                                SET passive = 'False' 
                                WHERE User_ID ={}'''.format(id))
                convar.commit()
                convar.close()
        else:
            emb = Embed(title = 'I DONT UNDERSTAND WYM???')
            await ctx.reply(embed = emb)
    
    

    @commands.command()
    @commands.cooldown(rate = 1, per = 1800, type=commands.BucketType.user)
    async def give(self,ctx, member : discord.Member, message):
        receiver = member.id
        giver = ctx.author.id
        amount = int(message)

        emb = Embed(title = 'How noble!', description = f'You are about to give {amount}❂ to {member.mention}. Are you sure?.')

    #@commands.command       

def setup(bot):
    bot.add_cog(BucksDB(bot))    


