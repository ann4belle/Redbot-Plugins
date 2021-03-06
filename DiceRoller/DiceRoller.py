from redbot.core import commands
from redbot.core.bot import Red
import requests

API = "https://kreativekorp.com/dX/"

class DiceRoller(commands.Cog):
    """Roll dice using kreativekorp dX API"""

    def __init__(self, bot: Red):
        self.bot: Red = bot

    @commands.command()
    async def roll(self, ctx, *, roll: str):
        if(roll == None):
            await ctx.reply('For syntax, see: <https://www.kreativekorp.com/dX/>')
            return
        r = requests.get(url = API, params = {'roll':roll, 'format':'json', 'optimize':'false', 'evaluate':'true', 'expound':'true'})
        if(r.status_code != 200):
            await ctx.reply('Something went wrong - please try again later.')
            await self.bot.send_to_owners(ctx.message.content + '\nHTTP ' + r.status_code + '\nResponse: ' + r.raw)
            return
        response = r.json()
        if(response[0]['type'] == 'error'):
            await ctx.reply('For syntax, see: <https://www.kreativekorp.com/dX/>')
            return
        msg = roll + ' = ' + str(response[-1]['return-value'])
        await ctx.reply(msg)
