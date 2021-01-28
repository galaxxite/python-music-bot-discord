from discord.ext import commands
import discord
from datetime import datetime
from .. import util


class Meta(commands.Cog):

    def __init__(self, bot, config):
        self.bot = bot
        self.start_time = datetime.now()
        self.config = config

    @commands.command()
    async def uptime(self, ctx):
        uptime_seconds = round(
            (datetime.now() - self.start_time).total_seconds())
        await ctx.send(f"Current Uptime: {util.format_seconds(uptime_seconds)}"
                       )
