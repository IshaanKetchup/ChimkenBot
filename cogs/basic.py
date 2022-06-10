from discord.ext import commands
import discord
import random

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.count = {}
        
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Basic Cog Online')
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        self.count[guild.id] = 0
    
    '''@commands.command()
    async def add_var(self, ctx):
        for guild in self.bot.guilds:
            self.count[guild.id] = 0'''

    @commands.command(aliases = ['greet', 'hi'])
    async def hello(self, ctx):
        file = open('greetings.txt', 'r')
        greets = file.readlines()
        n = random.randint(0, len(greets)-1)
        x = greets[n]
        file.close()
        await ctx.reply(x)    
    
    @commands.command()
    async def rick(self, ctx):
            await ctx.reply("'*NEVER GONNA GIVE YOU UP*")
            await ctx.reply("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    @commands.command()
    async def inc(self, ctx):
            guild = ctx.author.guild
            self.count[guild.id] += 1

    @commands.command()
    async def dec(self,ctx):
            guild = ctx.author.guild
            self.count[guild.id] -=  1

    @commands.command()
    async def showc(self, ctx):
            guild = ctx.author.guild
            await ctx.reply('Count: {}'.format(self.count[guild.id]))

    @commands.command()
    async def reset(self, ctx):
            guild = ctx.author.guild
            self.count[guild.id] = 0
    
    @commands.command()
    async def slap(self, ctx, member : discord.Member ):
        file = open('slap.txt', 'r')
        gifs = file.readlines()
        n = random.randint(0, len(gifs)-1)
        url = gifs[n]
        file.close()
        emb = discord.Embed(title='WHACK', description = f"{ctx.author.mention} slapped {member.mention} ", url = url, color=discord.Colour.random())
        emb.set_image(url = url)
        emb.set_footer(text= 'get wrekd')
        await ctx.reply(embed = emb)
    
    @commands.command()
    async def roast(self, ctx, member : discord.Member ):
        file = open('roasts.txt', 'r')
        roasts = file.readlines()
        n = random.randint(0, len(roasts)-1)
        x = roasts[n]
        file.close()
        await ctx.reply(x)
    
        
def setup(bot):
    bot.add_cog(Basic(bot))
