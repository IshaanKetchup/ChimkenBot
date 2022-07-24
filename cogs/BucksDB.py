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
    def __init__(self, bot, ):
        self.bot = bot
    
        def checkrec():
            convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
            cursor = convar.cursor()

            cursor.execute('SELECT * FROM records')
            records = cursor.fetchall()
            convar.close()
            users = []
            for i in records:
                users.append(i[0])

            return users

        self.users = checkrec()

        

    @commands.Cog.listener()
    async def on_ready(self):
        print('BucksDB online')

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
    async def viewall(self, ctx):
        id = ctx.author.id
        channel = self.bot.get_channel(975378805889851482)
        if id == 572792089599803394 or id == 969540347619328031:
            convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
            cursor = convar.cursor()

            cursor.execute("select * from records")        
            x = cursor.fetchall()
            userstr = ''
            for i in x:
                name = self.bot.get_user(i[0])
                userstr += f'{name} -- {i[1]} -- {i[2]} \n'

            emb = Embed(description= userstr)
            await ctx.send(embed = emb)
            convar.close()

       

    @commands.command()
    async def start(self, ctx):
        users = self.users
        id = ctx.author.id

        if id in users:
            emb = Embed(description = 'You already have a ChimkenRecord, silly!')
            await ctx.reply(embed = emb)
        
        else:
            member = ctx.author
            convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
            cursor = convar.cursor()

            values = (member.id, 0, 'False', member)
            cursor.execute(f'''INSERT INTO records values {values}''')
            convar.commit()
            convar.close()
            emb = Embed(description = 'Welcome to ChimkenBucks! Your record has been initialised.')
            await ctx.reply(embed = emb)
    
    @commands.command(aliases = ['bal', 'money','wallet'])
    async def cash(self, ctx, member: discord.Member = None):
        users = self.users
        if ctx.author.id in users:
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
                emb.add_field(name = 'ChimkenBucks', value = f'❂{cash}')
                emb.add_field(name = 'Passive Mode', value = f'{passive}')
                emb.set_author(name = member, icon_url = member.avatar)
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
                emb.add_field(name = 'ChimkenBucks', value = f'❂{cash}')
                emb.add_field(name = 'Passive Mode', value = f'{passive}')
                emb.set_author(name = member, icon_url = ctx.author.avatar)
                emb.set_footer(text = f'Here are the ❂')
                emb.set_thumbnail(url = url)
                await ctx.reply(embed = emb)
                convar.close()
        else:
            emb = Embed(title = 'Welcome to ChimkenBucks!', description = 'You don\'t have a record. Type `>start` to begin!.')
            await ctx.reply(embed = emb)

    
    @commands.command(aliases = ['earn', 'job'])
    @commands.cooldown(rate = 1, per = 30, type=commands.BucketType.user)
    async def work(self,ctx):
        users = self.users
        if ctx.author.id in users:
            convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
            cursor = convar.cursor()
            weight = random.randint(1,100)
            if weight >= 1 and weight <=80:
                cash = random.randint(1,50)
            else:
                cash = random.randint(50, 100)
                
            emb = Embed(description = f'You earned ❂{cash}!', colour = discord.Color.random())
            emb.set_footer(text = 'cha-ching!')
            emb.set_author(name = ctx.message.author, icon_url = ctx.author.avatar)

            await ctx.reply(embed = emb)
            id = ctx.author.id
            
            cursor.execute("""UPDATE records
                                    SET ChimkenBucks = ChimkenBucks+{}
                                    WHERE User_ID = {}""".format(cash, id))
            convar.commit()
            convar.close()
        else:
            emb = Embed(title = 'Welcome to ChimkenBucks!', description = 'You don\'t have a record. Type `>start` to begin!.')
            await ctx.reply(embed = emb)

    @commands.command()
    @commands.cooldown(rate = 1, per = 1800, type=commands.BucketType.user)
    async def steal(self,ctx, member : discord.Member = None):
        users = self.users

        if ctx.author.id in users:
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
                                    
                                    emb = Embed(description = f'{ctx.author.mention} stole ❂{steal} from {member.mention} 😱🤑 ')
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
                                    emb = Embed(description =  f'Give {member.mention} a break. They have only ❂{cash}', colour = discord.Colour.random())
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
        else:
            emb = Embed(title = 'Welcome to ChimkenBucks!', description = 'You don\'t have a record. Type `>start` to begin!.')
            await ctx.reply(embed = emb)


    @commands.command()
    @commands.cooldown(rate = 1, per = 86400, type=commands.BucketType.user)
    async def passive(self, ctx, message):
        users = self.users
        if ctx.author.id in users:
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
        else:
            emb = Embed(title = 'Welcome to ChimkenBucks!', description = 'You don\'t have a record. Type `>start` to begin!.')
            await ctx.reply(embed = emb)

    @commands.command()
    @commands.cooldown(rate = 1, per = 30, type=commands.BucketType.user)
    async def give(self,ctx, member : discord.Member, message = None):
        users = self.users
        if ctx.author.id in users:
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
                    button2 = [x for x in self.children if x.custom_id == 'No'][0]

                    button.disabled = True
                    button2.disabled = True

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
                    emb2 = Embed(description = f'{member.mention} has been given ❂{amount} by {ctx.author.mention}!')
                    await interaction.response.edit_message(embed = emb2, view = self)

                @discord.ui.button(label = 'No', style = discord.ButtonStyle.danger, row = 0, custom_id= 'No')
                async def button2_callback(self, button, interaction):
                    button1 = [x for x in self.children if x.custom_id == 'Yes'][0]


                    button1.disabled = True
                    button.disabled = True

                    emb2 = Embed(description = f'Okay, transaction cancelled. ')
                    await interaction.response.edit_message(embed = emb2, view = self)

            emb = Embed(title = 'How noble!', description = f'You are about to give ❂{amount} to {member.mention}. Are you sure?')

            await ctx.reply(embed = emb, view = Confirmation(ctx))
    
        else:
            emb = Embed(title = 'Welcome to ChimkenBucks!', description = 'You don\'t have a record. Type `>start` to begin!.')
            await ctx.reply(embed = emb)

    @commands.command()
    async def leaderboards(self, ctx):
            convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
            cursor = convar.cursor()

            cursor.execute("""SELECT * FROM records Order by ChimkenBucks desc LIMIT 10""")
            recs = cursor.fetchall()
            userstr = ''
            rank = 1
            for i in recs:
                name = self.bot.get_user(i[0])
                cash = i[1]
                value = '{:,}'.format(cash)
                userstr += f'{rank}. `❂{value}` - {name} \n'
                rank += 1

            emb = Embed(title = '**Global Leaderboards**', description= userstr, colour = 0xFFD700)
            emb.set_thumbnail(url = self.bot.user.display_avatar)
            emb.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            emb.set_footer(text = 'OMG Legends')
            await ctx.send(embed = emb)
            convar.close()

    @commands.command()
    async def gamble(self, ctx, message):
        #if message is not None:

        id = ctx.author.id
        bet = int(message.lstrip())
        convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        cursor = convar.cursor()

        cursor.execute(f'''UPDATE records
                          SET ChimkenBucks = ChimkenBucks - {bet}
                          WHERE User_ID = {id}''')


        class Guess(discord.ui.View):
            def __init__(self, ctx):
                super().__init__(timeout = 10)
                self.ctx = ctx
                
            async def on_timeout(self):
                for child in self.children:
                    child.disabled = True
                await message.edit(view = self)
            async def interaction_check(self, interaction):
                if interaction.user != self.ctx.author:
                    embED = discord.Embed(description= 'Hey! Those buttons aren\'t for you >:(', color= discord.Color.random())
                    await interaction.response.send_message(embed = embED, ephemeral= True)
                    return False
                else:
                    return True

            @discord.ui.button(label = '1', style = discord.ButtonStyle.primary, row = 0, custom_id= '1')
            async def button1_callback(self, button, interaction):
                
                button2 = [x for x in self.children if x.custom_id == '2'][0]
                button3 = [x for x in self.children if x.custom_id == '3'][0]
                button4 = [x for x in self.children if x.custom_id == '4'][0]
                button5 = [x for x in self.children if x.custom_id == '5'][0]
                button6 = [x for x in self.children if x.custom_id == '6'][0]
                guess = 1
                difference = guess - number
                if difference <0:
                    difference = 0-difference

                button.disabled = True
                button2.disabled = True
                button3.disabled = True
                button4.disabled = True
                button5.disabled = True
                button6.disabled = True
                
                if difference == 0:
                    convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
                    cursor = convar.cursor()
                    
                    win = 2*bet
                    cursor.execute(f'''UPDATE records
                                    SET ChimkenBucks = ChimkenBucks + {win}
                                    WHERE User_ID = {id}''')
                                
                    emb = discord.Embed(description= f'You guessed it right! You get ❂{win}')
                    emb.set_footer(text = 'GG')
                    await interaction.response.edit_message(embed = emb, view = self)
                    
                elif difference == 1 :
                    win = bet
                    cursor.execute(f'''UPDATE records
                                    SET ChimkenBucks = ChimkenBucks + {win}
                                    WHERE User_ID = {id}''')
                    
                    emb = discord.Embed(description= 'So close! You get your money back! (❂{win})')
                    emb.set_footer(text = f'You missed by {difference}')
                    await interaction.response.edit_message(embed = emb, view = self)
                else:
                    emb = discord.Embed(description= 'You lose!')
                    emb.set_footer(text = f'You missed by {difference}')
                    await interaction.response.edit_message(embed = emb, view = self)

            @discord.ui.button(label = '2', style = discord.ButtonStyle.primary, row = 0, custom_id= '2')
            async def button2_callback(self, button, interaction):
                button1 = [x for x in self.children if x.custom_id == '1'][0]

                button3 = [x for x in self.children if x.custom_id == '3'][0]
                button4 = [x for x in self.children if x.custom_id == '4'][0]
                button5 = [x for x in self.children if x.custom_id == '5'][0]
                button6 = [x for x in self.children if x.custom_id == '6'][0]
                guess = 2
                difference = guess - number
                if difference <0:
                    difference = 0-difference

                button1.disabled = True
                button.disabled = True
                button3.disabled = True
                button4.disabled = True
                button5.disabled = True
                button6.disabled = True
                
                if difference == 0:
                    convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
                    cursor = convar.cursor()
                    
                    win = 2*bet
                    cursor.execute(f'''UPDATE records
                                    SET ChimkenBucks = ChimkenBucks + {win}
                                    WHERE User_ID = {id}''')
                                
                    emb = discord.Embed(description= f'You guessed it right! You get ❂{win}')
                    emb.set_footer(text = 'GG')
                    await interaction.response.edit_message(embed = emb, view = self)
                    
                elif difference == 1 :
                    win = bet
                    cursor.execute(f'''UPDATE records
                                    SET ChimkenBucks = ChimkenBucks + {win}
                                    WHERE User_ID = {id}''')
                    
                    emb = discord.Embed(description= 'So close! You get your money back! (❂{win})')
                    emb.set_footer(text = f'You missed by {difference}')
                    await interaction.response.edit_message(embed = emb, view = self)
                else:
                    emb = discord.Embed(description= 'You lose!')
                    emb.set_footer(text = f'You missed by {difference}')
                    await interaction.response.edit_message(embed = emb, view = self)

            @discord.ui.button(label = '3', style = discord.ButtonStyle.primary, row = 0, custom_id= '3')   
            async def button3_callback(self, button, interaction):
                button1 = [x for x in self.children if x.custom_id == '1'][0]
                button2 = [x for x in self.children if x.custom_id == '2'][0]
                
                button4 = [x for x in self.children if x.custom_id == '4'][0]
                button5 = [x for x in self.children if x.custom_id == '5'][0]
                button6 = [x for x in self.children if x.custom_id == '6'][0]
                guess = 3
                difference = guess - number
                if difference <0:
                    difference = 0-difference

                button1.disabled = True
                button2.disabled = True
                button.disabled = True
                button4.disabled = True
                button5.disabled = True
                button6.disabled = True
                
                if difference == 0:
                    convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
                    cursor = convar.cursor()
                    
                    win = 2*bet
                    cursor.execute(f'''UPDATE records
                                    SET ChimkenBucks = ChimkenBucks + {win}
                                    WHERE User_ID = {id}''')
                                
                    emb = discord.Embed(description= f'You guessed it right! You get ❂{win}')
                    emb.set_footer(text = 'GG')
                    await interaction.response.edit_message(embed = emb, view = self)
                    
                elif difference == 1 :
                    win = bet
                    cursor.execute(f'''UPDATE records
                                    SET ChimkenBucks = ChimkenBucks + {win}
                                    WHERE User_ID = {id}''')
                    
                    emb = discord.Embed(description= 'So close! You get your money back! (❂{win})')
                    emb.set_footer(text = f'You missed by {difference}')
                    await interaction.response.edit_message(embed = emb, view = self)
                else:
                    emb = discord.Embed(description= 'You lose!')
                    emb.set_footer(text = f'You missed by {difference}')
                    await interaction.response.edit_message(embed = emb, view = self)

            @discord.ui.button(label = '4', style = discord.ButtonStyle.primary, row = 1, custom_id= '4')
            async def button4_callback(self, button, interaction):
                button1 = [x for x in self.children if x.custom_id == '1'][0]
                button2 = [x for x in self.children if x.custom_id == '2'][0]
                button3 = [x for x in self.children if x.custom_id == '3'][0]
                
                button5 = [x for x in self.children if x.custom_id == '5'][0]
                button6 = [x for x in self.children if x.custom_id == '6'][0]
                guess = 4
                difference = guess - number
                if difference <0:
                    difference = 0-difference

                button1.disabled = True
                button2.disabled = True
                button.disabled = True
                button.disabled = True
                button5.disabled = True
                button6.disabled = True
                
                if difference == 0:
                    convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
                    cursor = convar.cursor()
                    
                    win = 2*bet
                    cursor.execute(f'''UPDATE records
                                    SET ChimkenBucks = ChimkenBucks + {win}
                                    WHERE User_ID = {id}''')
                                
                    emb = discord.Embed(description= f'You guessed it right! You get ❂{win}')
                    emb.set_footer(text = 'GG')
                    await interaction.response.edit_message(embed = emb, view = self)
                    
                elif difference == 1 :
                    win = bet
                    cursor.execute(f'''UPDATE records
                                    SET ChimkenBucks = ChimkenBucks + {win}
                                    WHERE User_ID = {id}''')
                    
                    emb = discord.Embed(description= 'So close! You get your money back! (❂{win})')
                    emb.set_footer(text = f'You missed by {difference}')
                    await interaction.response.edit_message(embed = emb, view = self)
                else:
                    emb = discord.Embed(description= 'You lose!')
                    emb.set_footer(text = f'You missed by {difference}')
                    await interaction.response.edit_message(embed = emb, view = self)

            @discord.ui.button(label = '5', style = discord.ButtonStyle.primary, row = 1, custom_id= '5')  
            async def button5_callback(self, button, interaction):
                button1 = [x for x in self.children if x.custom_id == '1'][0]
                button2 = [x for x in self.children if x.custom_id == '2'][0]
                button3 = [x for x in self.children if x.custom_id == '3'][0]
                button4 = [x for x in self.children if x.custom_id == '4'][0]
                
                button6 = [x for x in self.children if x.custom_id == '6'][0]
                guess = 5
                difference = guess - number
                if difference <0:
                    difference = 0-difference

                button1.disabled = True
                button2.disabled = True
                button.disabled = True
                button4.disabled = True
                button.disabled = True
                button6.disabled = True
                
                if difference == 0:
                    convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
                    cursor = convar.cursor()
                    
                    win = 2*bet
                    cursor.execute(f'''UPDATE records
                                    SET ChimkenBucks = ChimkenBucks + {win}
                                    WHERE User_ID = {id}''')
                                
                    emb = discord.Embed(description= f'You guessed it right! You get ❂{win}')
                    emb.set_footer(text = 'GG')
                    await interaction.response.edit_message(embed = emb, view = self)
                    
                elif difference == 1 :
                    win = bet
                    cursor.execute(f'''UPDATE records
                                    SET ChimkenBucks = ChimkenBucks + {win}
                                    WHERE User_ID = {id}''')
                    
                    emb = discord.Embed(description= 'So close! You get your money back! (❂{win})')
                    emb.set_footer(text = f'You missed by {difference}')
                    await interaction.response.edit_message(embed = emb, view = self)
                else:
                    emb = discord.Embed(description= 'You lose!')
                    emb.set_footer(text = f'You missed by {difference}')
                    await interaction.response.edit_message(embed = emb, view = self)

            @discord.ui.button(label = '6', style = discord.ButtonStyle.primary, row = 1, custom_id= '6')   
            async def button6_callback(self, button, interaction):
                button1 = [x for x in self.children if x.custom_id == '1'][0]
                button2 = [x for x in self.children if x.custom_id == '2'][0]
                button3 = [x for x in self.children if x.custom_id == '3'][0]
                button4 = [x for x in self.children if x.custom_id == '4'][0]
                button5 = [x for x in self.children if x.custom_id == '5'][0]
                
                guess = 6
                difference = guess - number
                if difference <0:
                    difference = 0-difference

                button1.disabled = True
                button2.disabled = True
                button.disabled = True
                button4.disabled = True
                button5.disabled = True
                button.disabled = True
                
                if difference == 0:
                    convar = psycopg2.connect(DATABASE_URL, sslmode = 'require')
                    cursor = convar.cursor()
                    
                    win = 2*bet
                    cursor.execute(f'''UPDATE records
                                    SET ChimkenBucks = ChimkenBucks + {win}
                                    WHERE User_ID = {id}''')
                                
                    emb = discord.Embed(description= f'You guessed it right! You get ❂{win}')
                    emb.set_footer(text = 'GG')
                    await interaction.response.edit_message(embed = emb, view = self)
                    
                elif difference == 1 :
                    win = bet
                    cursor.execute(f'''UPDATE records
                                    SET ChimkenBucks = ChimkenBucks + {win}
                                    WHERE User_ID = {id}''')
                    
                    emb = discord.Embed(description= 'So close! You get your money back! (❂{win})')
                    emb.set_footer(text = f'You missed by {difference}')
                    await interaction.response.edit_message(embed = emb, view = self)
                else:
                    emb = discord.Embed(description= 'You lose!')
                    emb.set_footer(text = f'You missed by {difference}')
                    await interaction.response.edit_message(embed = emb, view = self)

        emb = discord.Embed(description= 'Guess a number')
        message = await ctx.send(embed = emb, view = Guess(ctx))

        number = random.randint(1,6)




def setup(bot):
    bot.add_cog(BucksDB(bot))
