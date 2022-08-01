import discord
from discord.ext import  commands


class BrainPain(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('BrainPain Cog Online')

    @commands.command()
    async def track(self, ctx, member: discord.Member = None):
        if member != None:
            user = member
        else:
            user = ctx.author

        spotify_result = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
        try:
            if spotify_result is None:
                emb = discord.Embed(description= f'{user.name} is not listening to any music')
            else:
                song = spotify_result.title
                url = spotify_result.track_url
                artlist = spotify_result.artists
                artist = ''
                
                for i in artlist:
                    artist += i + ', '
                artist = artist[:-2:]
                thumbnail = spotify_result.album_cover_url
                emb = discord.Embed(title = f'{song}',description= f'{user.name} is listening to {song}, by {artist}', url= url, color= 0xFFFFFF)
                emb.set_image(url = thumbnail)
                emb.set_thumbnail(url = "https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_CMYK_White.png")
            emb.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            await ctx.send(embed = emb)
        except RuntimeError:
            pass

    @commands.command()
    async def wyd(self, ctx, member: discord.Member = None):
        if member != None:
            user = member
            game = next((activity for activity in user.activities if isinstance(activity, discord.Game)), None)
            spotify_result = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
            emb = discord.Embed(title = f'{user.name}\'s Activities', color = 0xFFFFFF )
            try:
                if spotify_result is None:
                    emb.add_field(name = 'Spotify', value= f'{user.name} is not listening to any music')
                else:
                    song = spotify_result.title
                    artlist = spotify_result.artists
                    artist = ''
                    
                    for i in artlist:
                        artist += i + ', '
                    artist = artist[:-2:]
                    emb.add_field(name = 'Spotify', value = f'{user.name} is listening to {song}, by {artist}', inline = True)

                if game is None:
                    emb.add_field(name = 'Game', value= f'{user.name} is not playing any game')
                else:
                    gname = game.name
                    emb.add_field(name = 'Game', value = f'{user.name} is playing {gname}', inline = True)

            except RuntimeError:
                pass
            emb.set_author(name= ctx.message.author, icon_url = ctx.author.avatar)
            emb.set_thumbnail(url = self.bot.user.display_avatar)
            
            
        else:
            emb = discord.Embed(description= 'Ping someone to find out what they\'re doing')

        await ctx.send(embed = emb)        


def setup(bot):
    bot.add_cog(BrainPain(bot))
