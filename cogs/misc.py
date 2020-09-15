from discord.ext import commands
import discord
from utils.util import Embed


class Misc(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def suggest(self, ctx, *, suggestion: str):
        embed = Embed(ctx, description=suggestion).author().random_footer()
        msg = await self.bot.get_guild(self.bot.config["support_guild"]["id"]).get_channel(self.bot.config["support_guild"]["suggestion_channel"]).send(embed=embed)
        await msg.add_reaction("✅")
        await msg.add_reaction("❎")
        await ctx.send(f"{ctx.author.mention}, Suggestion logged!")

    @commands.command()
    async def help(self, ctx)
        author = ctx.message.author

        embed = discord.Embed(
            colour=discord.colour.blue(),
            title="**Help**"
            description="Commands for OmniReddit"
        )

        embed.set_image(url="https://cdn.discordapp.com/attachments/755128550813728815/755137589568078004/Screenshot_20200914_204646.jpg")
        embed.add_field(name="**Reddit Commands**")
        embed.add_field(name="search", value="Searches for a post")
        embed.add_field(name="subreddit", value="Shows the subreddit most recent posts")
        embed.add_field()
        embed.add_field(name="**Misc**")
        embed.add_field(name="Suggest", value="Sends a suggestion to a channel")

        await author.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
