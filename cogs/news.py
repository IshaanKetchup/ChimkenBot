import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
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
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()

            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            urllist = []
            for news in news_list:
                urllist.append(news)

            newsn = random.choice(urllist)
            
            titlen = newsn.title.text
            linkn = newsn.link.text
            embed = Embed(title = titlen, url = linkn, colour = discord.Colour.random())
            embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            embed.set_footer(text = "Here's a random headline")
            await ctx.reply(embed = embed)
            
        else:
            client = gn.NewsClient(topic = message)
            topics = client.topics

            if message in topics:
                client = gn.NewsClient(topic = message)
                newsn = random.choice(client.get_news())
                linkn = newsn['link']
                titlen = newsn['title']
                embed = Embed(title = titlen, url = linkn, colour = discord.Colour.random())
                embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                embed.set_footer(text = "Here's a random headline")
                await ctx.reply(embed = embed)

            else:
                embed = Embed(title = 'Google News', url = 'https://news.google.com/',description='Your topic was invalid! Try again, from this list:', colour = 0xFFFFFF)
                for topic in topics:
                    embed.add_field(name = topic, value = 'ㅤ')

                await ctx.reply(embed = embed)
        

def setup(bot):
    bot.add_cog(News(bot))
