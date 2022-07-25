import discord
from discord.ext import commands
import random
from discord import Embed
from gnewsclient import gnewsclient as gn

class News(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('News Cog Online')


    @commands.command()
    async def news(self, ctx, message = None):
        if message is None:
            client = gn.NewsClient()
            topics = client.topics
            newsn = random.choice(client.get_news())
            linkn = newsn['link']
            titlen = newsn['title']
            embed = Embed(title = titlen, url = linkn, colour = discord.Colour.random())
            embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            embed.set_footer(text = f"Here's a random headline")
            await ctx.reply(embed = embed)

        else: 
            nstr = message.title()
            client = gn.NewsClient(topic = nstr)
            topics = client.topics
            if nstr in topics:
                newsn = random.choice(client.get_news())
                linkn = newsn['link']
                titlen = newsn['title']
                embed = Embed(title = titlen, url = linkn, colour = discord.Colour.random())
                embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                embed.set_footer(text = f"Here's a random {nstr} headline")
                await ctx.reply(embed = embed)

            else:
                embed = Embed(title = 'Google News', url = 'https://news.google.com/',description='Your topic was invalid! Try again, from this list:', colour = 0xFFFFFF)
                for topic in topics:
                    if topic == 'Top Stories':
                        continue
                    else:
                        embed.add_field(name = topic, value = 'ㅤ')

                await ctx.reply(embed = embed)

def setup(bot):
    bot.add_cog(News(bot))
