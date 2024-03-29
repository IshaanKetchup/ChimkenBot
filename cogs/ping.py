from lib2to3.pgen2 import pgen
from re import X
import discord
from discord.ext import commands
from discord import Embed

import asyncio

class Ping(commands.Cog, name = "Ping"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ping Cog Online')

    @commands.command()
    async def announce(self, ctx, *message):
        id = ctx.author.id
        if id == 572792089599803394 or id == 969540347619328031:
            channel = self.bot.get_channel(int(message[0]))
            notif = ''
            
            for i in message:
                if i != message[0]:
                    notif+=i +' '

            await channel.send(f'{notif}')
        
    
    @commands.command()
    async def pag(self, ctx):
        pg = '1' 
        await ctx.send(f'{type(pg)}')
        
    @commands.command()
    async def button(self, ctx):
        
        class View(discord.ui.View):      
            global pg
            pg = 0
            
            @discord.ui.button(label="⬅", style=discord.ButtonStyle.primary, row = 0) 
            async def button1_callback(self, button, interaction):
                global pg
                await interaction.response.edit_message(view = self)
                pg += 1

            @discord.ui.button(label = '➡', style = discord.ButtonStyle.primary, row = 0)
            async def button2_callback(self, button, interaction):
                global pg
                self.pg = '-'
                await interaction.response.send_message(f'{pg}', view = View())


        await ctx.send(f"hi", view=View())

        
def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))
        


