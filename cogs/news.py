import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import discord
from discord.ext import commands
import random
from discord import Embed

class News(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('News Cog Online')

    @commands.command()
    async def news(self, ctx):
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
        

def setup(bot):
    bot.add_cog(News(bot))
