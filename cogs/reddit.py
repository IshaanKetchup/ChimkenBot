import discord
from discord.ext import commands
from discord import Embed
import random
import asyncpraw
import os

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = asyncpraw.Reddit(
        client_id = 'YyWASgMLM1ijcLkZ-UcA7Q',
        client_secret = 'Y6bNJTEQjSv67rM2l2ms1JMsRLzymw',
        user_agent = 'Memes from r/Memes for Discord bot',
        username = 'EyeKay13',
        password = 'y8CUb:QUiR-2tTJ')
        
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Reddit Cog Online')
        
        

    @commands.command(aliases = ['memes','meemee', 'memey'])
    async def meme(self, ctx):
                
        subreddit = await self.reddit.subreddit('memes', fetch = True)
        posts = []
        hot = subreddit.hot(limit = 100)
        
        async for submission in hot:
            posts.append(submission)
            
        randompost = random.choice(posts)

        name = randompost.title
        url  = randompost.url
        go = "https://www.reddit.com" + randompost.permalink
        if hasattr(randompost, 'post_hint'):
            hint = randompost.post_hint
            if hint == 'hosted:video' or hint == 'rich:video':
                await ctx.reply(go)
            else:
                embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = go)
                embed.set_image(url = url)
                embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                embed.set_footer(text = 'nicc meme')
                await ctx.reply(embed = embed)
        
        else:
            embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = url)
            embed.set_image(url = url)
            embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            embed.set_footer(text = 'nicc meme')
            await ctx.reply(embed = embed)
        
    @commands.command(aliases = ['dank', 'dm'])
    async def dankmeme(self, ctx):
        
        
        subreddit = await self.reddit.subreddit('IndianDankMemes', fetch = True)
        posts = []
        hot = subreddit.hot(limit = 100)
        
        async for submission in hot:
            posts.append(submission)
            
        randompost = random.choice(posts)

        name = randompost.title
        url  = randompost.url
        go = "https://www.reddit.com" + randompost.permalink
        if hasattr(randompost, 'post_hint'):
            hint = randompost.post_hint
            if hint == 'hosted:video' or hint == 'rich:video':
                await ctx.reply(go)
            else:
                embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = go)
                embed.set_image(url = url)
                embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                embed.set_footer(text = 'dAnK')
                await ctx.reply(embed = embed)
        
        else:
            embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = url)
            embed.set_image(url = url)
            embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            embed.set_footer(text = 'dAnK')
            await ctx.reply(embed = embed)

    @commands.command(aliases =['cr', 'chem'])
    async def reaction(self, ctx):
                
        subreddit = await self.reddit.subreddit('ChemicalReactionGIFs', fetch = True)
        posts = []
        hot = subreddit.hot(limit = 100)
        
        async for submission in hot:
            posts.append(submission)
            
        randompost = random.choice(posts)

        name = randompost.title
        url  = randompost.url
        go = "https://www.reddit.com" + randompost.permalink
        if hasattr(randompost, 'post_hint'):
            hint = randompost.post_hint
            if hint == 'hosted:video' or hint == 'rich:video':
                await ctx.reply(go)
            else:
                embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = go)
                embed.set_image(url = url)
                embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                embed.set_footer(text = "thank god that didn't explode ")
                await ctx.reply(embed = embed)
        
        else:
            embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = url)
            embed.set_image(url = url)
            embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            embed.set_footer(text = "thank god that didn't explode ")
            await ctx.reply(embed = embed)

    @commands.command(aliases = ['f'])
    async def fact(self, ctx):
                
        subreddit = await self.reddit.subreddit('funfacts', fetch = True)
        posts = []
        hot = subreddit.hot(limit = 100)
        
        async for submission in hot:
            posts.append(submission)
            
        randompost = random.choice(posts)

        name = randompost.title
        url  = randompost.url
        go = "https://www.reddit.com" + randompost.permalink
        if hasattr(randompost, 'post_hint'):
            hint = randompost.post_hint
            if hint == 'hosted:video' or hint == 'rich:video':
                await ctx.reply(go)
            else:
                embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = go)
                embed.set_image(url = url)
                embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                embed.set_footer(text = 'ok')
                await ctx.reply(embed = embed)
        
        else:
            embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = url)
            embed.set_image(url = url)
            embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            embed.set_footer(text = 'ok')
            await ctx.reply(embed = embed)

    @commands.command(aliases = ['perfecttiming', 'pt'])
    async def wowpics(self, ctx):
                
        subreddit = await self.reddit.subreddit('PerfectTiming', fetch = True)
        posts = []
        hot = subreddit.hot(limit = 100)
        
        async for submission in hot:
            posts.append(submission)
            
        randompost = random.choice(posts)

        name = randompost.title
        url  = randompost.url
        go = "https://www.reddit.com" + randompost.permalink
        if hasattr(randompost, 'post_hint'):
            hint = randompost.post_hint
            if hint == 'hosted:video' or hint == 'rich:video':
                await ctx.reply(go)
            else:
                embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = go)
                embed.set_image(url = url)
                embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                embed.set_footer(text = 'wow.')
                await ctx.reply(embed = embed)
        
        else:
            embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = url)
            embed.set_image(url = url)
            embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            embed.set_footer(text = 'wow.')
            await ctx.reply(embed = embed)

    @commands.command(aliases = ['dog', 'doggo', 'woof'])
    async def doggie(self, ctx):
               
        subreddit = await self.reddit.subreddit('dogpictures', fetch = True)
        posts = []
        hot = subreddit.hot(limit = 100)
        
        async for submission in hot:
            posts.append(submission)
            
        randompost = random.choice(posts)

        name = randompost.title
        url  = randompost.url
        go = "https://www.reddit.com" + randompost.permalink
        if hasattr(randompost, 'post_hint'):
            hint = randompost.post_hint
            if hint == 'hosted:video' or hint == 'rich:video':
                await ctx.reply(go)
            else:
                embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = go)
                embed.set_image(url = url)
                embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                embed.set_footer(text = 'ruff ruff🐶')
                await ctx.reply(embed = embed)
        
        else:
            embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = url)
            embed.set_image(url = url)
            embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            embed.set_footer(text = 'ruff ruff🐶')
            await ctx.reply(embed = embed)

    @commands.command(aliases = ['cat', 'meow', 'pspsps', 'catto'])
    async def kitty(self, ctx):
                
        subreddit = await self.reddit.subreddit('catpictures', fetch = True)
        posts = []
        hot = subreddit.hot(limit = 100)
        
        async for submission in hot:
            posts.append(submission)
            
        randompost = random.choice(posts)

        name = randompost.title
        url  = randompost.url
        go = "https://www.reddit.com" + randompost.permalink
        if hasattr(randompost, 'post_hint'):
            hint = randompost.post_hint
            if hint == 'hosted:video' or hint == 'rich:video':
                await ctx.reply(go)
            else:
                embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = go)
                embed.set_image(url = url)
                embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                embed.set_footer(text = 'MEOWWWWW🐱')
                await ctx.reply(embed = embed)
        
        else:
            embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = url)
            embed.set_image(url = url)
            embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            embed.set_footer(text = 'MEOWWWWW🐱')
            await ctx.reply(embed = embed)

    @commands.command(aliases = ['duck', 'ducko', 'quack'])
    async def duckie(self, ctx):
        
                
        subreddit = await self.reddit.subreddit('duck', fetch = True)
        posts = []
        hot = subreddit.hot(limit = 100)
        
        async for submission in hot:
            posts.append(submission)
            
        randompost = random.choice(posts)

        name = randompost.title
        url  = randompost.url
        go = "https://www.reddit.com" + randompost.permalink
        if hasattr(randompost, 'post_hint'):
            hint = randompost.post_hint
            if hint == 'hosted:video' or hint == 'rich:video':
                await ctx.reply(go)
            else:
                embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = go)
                embed.set_image(url = url)
                embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                embed.set_footer(text = 'OH 🦆')
                await ctx.reply(embed = embed)
        
        else:
            embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = url)
            embed.set_image(url = url)
            embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            embed.set_footer(text = 'OH 🦆')
            await ctx.reply(embed = embed)

    @commands.command()
    async def aww(self, ctx):
                
        subreddit = await self.reddit.subreddit('aww', fetch = True)
        posts = []
        hot = subreddit.hot(limit = 100)
        
        async for submission in hot:
            posts.append(submission)
            
        randompost = random.choice(posts)

        name = randompost.title
        url  = randompost.url
        go = "https://www.reddit.com" + randompost.permalink
        if hasattr(randompost, 'post_hint'):
            hint = randompost.post_hint
            if hint == 'hosted:video' or hint == 'rich:video':
                await ctx.reply(go)
            else:
                embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = go)
                embed.set_image(url = url)
                embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                embed.set_footer(text = 'OMG AWW')
                await ctx.reply(embed = embed)
        
        else:
            embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = url)
            embed.set_image(url = url)
            embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            embed.set_footer(text = 'OMG AWW')
            await ctx.reply(embed = embed)
    
    @commands.command()
    async def reddit(self, ctx, message):
        
        class NSFWView(discord.ui.View): 
            
            @discord.ui.button(label="Show NSFW", style=discord.ButtonStyle.primary, row = 0, custom_id='show') 
            async def button1_callback(self, button, interaction):
                emb2= Embed(title = f'|| {name} ||', colour = discord.Colour.random())
                emb2.add_field(name = '**POSSIBLE NSFW.** Open at your own discretion', value = f'||{url}||')
                emb2.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                emb2.set_footer(text = 'Here you go')
                
                await interaction.response.send_message(embed = emb2, ephemeral = True)

            async def on_timeout(self):
                for child in self.children:
                    child.disabled = True
                await self.message.edit(view = self)



        subreddit = await self.reddit.subreddit(message, fetch = True)
        posts = []
        hot = subreddit.hot(limit = 200)
        
        async for submission in hot:
            posts.append(submission)
            
        randompost = random.choice(posts)

        name = randompost.title
        url = randompost.url
        go = "https://www.reddit.com" + randompost.permalink

        if randompost.over_18:
            emb1 = Embed(title = '**This post may be NSFW😱**')
            NSFWView.message = await ctx.reply(embed = emb1, view = NSFWView(timeout = 10))
        else:
            if hasattr(randompost, 'post_hint'):
                hint = randompost.post_hint
                if hint == 'hosted:video' or hint == 'rich:video':
                    await ctx.reply(go)
                else:
                    embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = go)
                    embed.set_image(url = url)
                    embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                    embed.set_footer(text = 'Here you go')
                    await ctx.reply(embed = embed)
            
            else:
                embed = Embed(title = f'{name}', colour = discord.Colour.random(), url = go)
                embed.set_image(url = url)
                embed.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
                embed.set_footer(text = 'Here you go')
                await ctx.reply(embed = embed)   


def setup(bot):
    bot.add_cog(Reddit(bot))
