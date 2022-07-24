from discord.ext import commands
import discord

class Google(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Google Cog Online')

    @commands.command(aliases = ['s'])
    async def search(self, ctx):
        squery = str(ctx.message.content)
        finst = ''
        for x in (squery.split()[1::]):
            if x != squery.split()[-1]:
                y = x + '+'
            else:
                y = x
            finst += y
        await ctx.reply('https://www.google.com/search?q='+ finst)
    
    @commands.command(aliases = ['yt'])
    async def youtube(self, ctx):
        squery = str(ctx.message.content)
        finst = ''
        for x in (squery.split()[1::]):
            if x != squery.split()[-1]:
                y = x + '+'
            else:
                y = x
            finst += y
        await ctx.reply('https://www.youtube.com/results?search_query='+ finst)
    
    
    
    
def setup(bot):
    bot.add_cog(Google(bot))            
