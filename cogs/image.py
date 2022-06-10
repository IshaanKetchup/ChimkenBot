from discord.ext import commands
import discord
from discord import Embed
import random
import PIL.Image
from io import BytesIO


class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Image Cog Online')
    
    @commands.command()
    async def sus(self, ctx, member: discord.Member):
        sus  = PIL.Image.open('sus.jpg')
        asset = member.display_avatar

        data = BytesIO(await asset.read())
        pfp = PIL.Image.open(data)

        pfp = pfp.resize((251, 251))
        sus.paste(pfp, (175,100))

        sus.save("sussy.jpg")
        emb = Embed(description= f'{member.mention} kinda sus', colour= discord.Color.random())
        await ctx.reply(file = discord.File("sussy.jpg"))

    @commands.command()
    async def gay(self, ctx, member: discord.Member):
        pride  = PIL.Image.open('pride.jpg')
        pride.putalpha(100)
        pride.save('pride2.jpg')

        '''asset = member.display_avatar

        pride2 = PIL.Image.open('pride2.jpg')

        data = BytesIO(await asset.read())
        pfp = PIL.Image.open(data)

        pfp = pfp.resize((250, 250))
        pfp.paste(pride2, (120,120))

        pfp.save("pride.jpg")

        await ctx.send(file = discord.File("pride.jpg"))'''

        
        

def setup(bot):
    bot.add_cog(Image(bot))
