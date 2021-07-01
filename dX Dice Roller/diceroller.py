from redbot.core import commands

class DiceRoller(commands.Cog):
    """Dice Roller using KreativeKorp dX API"""

    @commands.command()
    async def roll(self, ctx):
        """Sends dice roll command to dX and displays results"""
        await ctx.send("Test")