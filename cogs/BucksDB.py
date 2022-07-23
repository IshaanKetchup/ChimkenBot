import sqlite3
from discord.ext import commands
import discord
import random
from discord import Embed
import psycopg2
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

    @commands.command()
    @commands.cooldown(rate = 1, per = 1800, type=commands.BucketType.user)
    async def steal(self,ctx, member : discord.Member = None):
        if member is not None:
            id = member.id
            robber = ctx.author.id

            if id != robber:

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
            else:
                emb = Embed(description= 'You can\'t steal from *yourself*!')
                emb.set_footer(text = 'Mention someone else to steal from them')
                await ctx.reply(embed = emb)
        else:
            emb = Embed(description= 'You can\'t steal from *no one*!')
            emb.set_footer(text = 'Mention someone to steal from them')
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
    @commands.cooldown(rate = 1, per = 30, type=commands.BucketType.user)
    async def give(self,ctx, member : discord.Member, message = None):

        amount = int(message)

        class Confirmation(discord.ui.View):

            def __init__(self, ctx):
                super().__init__(timeout = 10)
                self.ctx = ctx
                
            async def on_timeout(self):
                for child in self.children:
                    child.disabled = True
                await self.message.edit(view = self)

            async def interaction_check(self, interaction):
                if interaction.user != self.ctx.author:
                    embED = Embed(description= 'Hey! Those buttons aren\'t for you >:(', color= discord.Color.random())
                    await interaction.response.send_message(embed = embED, ephemeral= True)
                    return False
                else:
                    return True
            
            @discord.ui.button(label = 'Yes', style = discord.ButtonStyle.success, row = 0, custom_id= 'Yes')
            async def button1_callback(self, button, interaction):
                button2 = [x for x in self.children if x.custom_id == 'No']
                receiver = member.id
                giver = ctx.author.id
                amount = int(message)

                convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
                cursor = convar.cursor()
                
                cursor.execute("""UPDATE records
                                SET ChimkenBucks = ChimkenBucks+{}
                                WHERE User_ID = {}""".format(amount, receiver))
                
                cursor.execute("""UPDATE records
                                SET ChimkenBucks = ChimkenBucks-{}
                                WHERE User_ID = {}""".format(amount, giver))
                convar.commit()
                emb2 = Embed(description = f'{member.mention} has been given {amount}❂ by {ctx.author.mention}!')
                await interaction.response.edit_message(embed = emb2, view = self)

            @discord.ui.button(label = 'No', style = discord.ButtonStyle.danger, row = 0, custom_id= 'No')
            async def button2_callback(self, button, interaction):
                button1 = [x for x in self.children if x.custom_id == 'Yes']

                emb2 = Embed(description = f'Okay, transaction cancelled. ')
                await interaction.response.edit_message(embed = emb2, view = self)

        emb = Embed(title = 'How noble!', description = f'You are about to give {amount}❂ to {member.mention}. Are you sure?')

        await ctx.send(embed = emb, view = Confirmation(ctx))

def setup(bot):
    bot.add_cog(BucksDB(bot))
