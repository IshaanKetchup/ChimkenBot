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
        asset = member.display_avatar
        data = BytesIO(await asset.read())
        pfp = PIL.Image.open(data).convert('RGB')

        pride  = PIL.Image.open('pride.jpg').convert('RGB')
        pride = pride.resize(pfp.size)

        blended = PIL.Image.blend(pfp, pride, 0.4)
        blended.save('blended.jpg')
        await ctx.reply(file = discord.File("blended.jpg"))

        
        

def setup(bot):
    bot.add_cog(Image(bot))
