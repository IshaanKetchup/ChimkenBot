from discord.ext import commands
import discord
from discord import Embed
import random

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        


    @commands.Cog.listener()
    async def on_ready(self):
        print('Help Cog Online')

    @commands.command()
    async def help(self, ctx):

        class HelpView(discord.ui.View): 
            global pg
            pg = 1

            def __init__(self,ctx):
                super().__init__(timeout=10)
                self.ctx = ctx

            async def interaction_check(self, interaction):
                if interaction.user != self.ctx.author:
                    embED = Embed(description= 'Hey! Those buttons aren\'t for you >:(', color= discord.Color.random())
                    await interaction.response.send_message(embed = embED, ephemeral= True)
                    return False
                else:
                    return True

            @discord.ui.button(label = '<<', style = discord.ButtonStyle.primary, row = 0, custom_id= 'left', disabled = True)
            async def button1_callback(self, button, interaction):
                
                button2 = [x for x in self.children if x.custom_id == 'right'][0]
                global pg
                pg -= 1
                if pg == 1:
                    button.disabled = True
                    button2.disabled = False
                    emb = emb1
                elif pg == 2:
                    button.disabled = False
                    button2.disabled = False
                    emb = emb2
                elif pg == 3:
                    button.disabled = False
                    button2.disabled = False
                    emb = emb3
                elif pg == 4:
                    button.disabled = False
                    button2.disabled = True
                    emb = emb4
                await interaction.response.edit_message(embed = emb, view = self)
            
            @discord.ui.button(label=">>", style=discord.ButtonStyle.primary, row = 0, custom_id= 'right') 
            async def button2_callback(self, button, interaction):
                button1 = [x for x in self.children if x.custom_id == 'left'][0]
                global pg
                pg += 1

                if pg == 1:
                    button.disabled = False
                    button1.disabled = True
                    emb = emb1
                elif pg == 2:
                    button.disabled = False
                    button1.disabled = False
                    emb = emb5
                elif pg == 3:
                    button.disabled = False
                    button1.disabled = False
                    emb = emb3
                elif pg == 4:
                    button.disabled = True
                    button1.disabled = False
                    emb = emb4
                await interaction.response.edit_message(embed = emb, view = self)
                
            async def on_timeout(self):
                for child in self.children:
                    child.disabled = True
                await self.message.edit(view = self)
                        
        emb1 = discord.Embed(title = '**REDDIT COMMANDS**', color = discord.Color.random())
        emb1.add_field(name = "Memes", value = '>meme', inline= True)
        emb1.add_field(name = "IndianDankMemes", value = '>dankmeme', inline= True)
        emb1.add_field(name = "ChemicalReactionGifs", value = '>reaction', inline= True)
        emb1.add_field(name = "Facts", value = '>fact', inline= True)
        emb1.add_field(name = "PerfectTiming", value = '>wowpics', inline= True)
        emb1.add_field(name = "Cute Dogs", value = '>doggie', inline= True)
        emb1.add_field(name = "Cute Cats", value = '>kitty', inline= True)
        emb1.add_field(name = "Cute Ducks", value = '>duckie', inline= True)
        emb1.add_field(name = "Aww", value = '>aww', inline= True)
        emb1.add_field(name = 'Choose subreddit', value = '>reddit (name of subreddit)', inline = True)
        emb1.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
        emb1.set_thumbnail(url = self.bot.user.display_avatar)

        emb2 = discord.Embed(title = "**Currency Commands**", color = discord.Color.random())
        emb2.add_field(name = 'Work', value = '>work')
        emb2.add_field(name = 'Steal', value = '>steal @user')
        emb2.add_field(name = 'Gamble', value = '>gamble (amount)')
        emb2.add_field(name = 'Passive Mode', value = '>passive (true/false)')
        #emb2.add_field(name = 'Daily', value = '>daily')
        #emb2.add_field(name = 'Monthly', value = '>monthly')
        emb2.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
        emb2.set_thumbnail(url = self.bot.user.display_avatar)

        emb3 = discord.Embed(title = '**SASS COMMANDS**', color = discord.Color.random())
        emb3.add_field(name = "Roast Someone", value = '>roast @user', inline= True)
        emb3.add_field(name = "Slap Someone", value = '>slap @user', inline= True)
        emb3.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
        emb3.set_thumbnail(url = self.bot.user.display_avatar)

        emb4 = discord.Embed(title = '**OTHER COMMANDS**', color = discord.Color.random())
        emb4.add_field(name = "Sus", value = ">sus @user", inline = True)
        emb4.add_field(name = "Jokes", value = ">funny", inline= True)        
        emb4.add_field(name = "News", value ='>news', inline = True)
        emb4.add_field(name = "Google search", value = ">search (search query)", inline= True)
        emb4.add_field(name = "Hello", value = '>hello', inline= True)
        emb4.add_field(name = "Rick", value = '>rick', inline= True)
        emb4.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
        emb4.set_thumbnail(url = self.bot.user.display_avatar)
        
        emb5 = discord.Embed(title = '**IMAGE COMMANDS**', color = discord.Color.random())
        emb5.add_field(name = "Sus", value = ">sus @user", inline = True)
        emb5.add_field(name = "Gay", value = ">gay @user", inline = True)        
        emb5.add_field(name = "WW2", value = ">ww2 @user", inline = True)
        emb5.add_field(name = "USA", value = ">usa @user", inline = True)
        emb5.add_field(name = "India", value = ">india @user", inline = True)
        emb5.add_field(name = "sad", value = ">sad @user", inline = True)    
        emb5.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
        emb5.set_thumbnail(url = self.bot.user.display_avatar)

    
        HelpView.message = await ctx.send(embed = emb1, view = HelpView(ctx))
            


def setup(bot):
    bot.add_cog(Help(bot))

