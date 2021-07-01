from redbot.core import commands
from redbot.core import checks
from discord import Guild
from discord import Permissions

class Adminify(commands.Cog):

    @commands.command
    @checks.is_owner
    async def adminify(self, ctx, role_name):
        author = ctx.author
        ctx.send(ctx.Guild.name)