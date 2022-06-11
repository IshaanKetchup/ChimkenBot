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
        sus  = PIL.Image.open('media//sus.jpg')
        asset = member.display_avatar

        data = BytesIO(await asset.read())
        pfp = PIL.Image.open(data)

        pfp = pfp.resize((251, 251))
        sus.paste(pfp, (175,100))

        sus.save("sussy.jpg")
        await ctx.send(file = discord.File("sussy.jpg"))

    @commands.command()
    async def gay(self, ctx, member: discord.Member):
        asset = member.display_avatar
        data = BytesIO(await asset.read())
        pfp = PIL.Image.open(data).convert('RGB')

        pride  = PIL.Image.open('media//pride.jpg').convert('RGB')
        pride = pride.resize(pfp.size)

        blended = PIL.Image.blend(pfp, pride, 0.5)
        blended.save('blended.jpg')

        await ctx.reply(file = discord.File("blended.jpg"))

    @commands.command()
    async def usa(self, ctx, member: discord.Member):
        asset = member.display_avatar
        data = BytesIO(await asset.read())
        pfp = PIL.Image.open(data).convert('RGB')

        merger  = PIL.Image.open('media//america.jpg').convert('RGB')
        merger = merger.resize(pfp.size)

        blended = PIL.Image.blend(pfp, merger, 0.25)
        blended.save('americablend.jpg')

        await ctx.reply(file = discord.File("americablend.jpg"))

    @commands.command()
    async def india(self, ctx, member: discord.Member):
        asset = member.display_avatar
        data = BytesIO(await asset.read())
        pfp = PIL.Image.open(data).convert('RGB')

        merger  = PIL.Image.open('media//india.png').convert('RGB')
        merger = merger.resize(pfp.size)

        blended = PIL.Image.blend(pfp, merger, 0.25)
        blended.save('indiablend.jpg')

        await ctx.reply(file = discord.File("indiablend.jpg"))

    @commands.command()
    async def sad(self, ctx, member: discord.Member):
        asset = member.display_avatar
        data = BytesIO(await asset.read())
        pfp = PIL.Image.open(data).convert('L')
        pfp.save('sad.jpg')

        await ctx.reply(file = discord.File("sad.jpg"))
           
    @commands.command()
    async def ww2(self, ctx, member: discord.Member):
        asset = member.display_avatar
        data = BytesIO(await asset.read())
        pfp = PIL.Image.open(data).convert('L')

        merger  = PIL.Image.open('media//ww2.jpg').convert('L')
        merger = merger.resize(pfp.size)

        blended = PIL.Image.blend(pfp, merger, 0.5)
        blended.save('ww2blend.jpg')

        await ctx.reply(file = discord.File("ww2blend.jpg"))


def setup(bot):
    bot.add_cog(Image(bot))
