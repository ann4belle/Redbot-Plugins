from redbot.core import commands
from redbot.core.bot import RedBase
import requests

API = "https://kreativekorp.com/dX/"

class DiceRoller(commands.Cog):
    """Roll dice using kreativekorp dX API"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx):
        if(ctx.args == []):
            await ctx.reply('For syntax, see: <https://www.kreativekorp.com/dX/>')
            return
        r = requests.get(url = API, params = {'roll':' '.join(str(e) for e in ctx.args), 'format':'json', 'optimize':'false', 'evaluate':'true', 'expound':'true'})
        if(r.status_code != 200):
            await ctx.reply('Something went wrong - please try again later.')
            await RedBase.send_to_owners(ctx.message + '\nHTTP ' + r.status_code + '\nResponse: ' + r.raw)
            return
        response = r.json()
        if(response[0]['type'] == 'error'):
            await ctx.reply('For syntax, see: <https://www.kreativekorp.com/dX/>')
            return
        msg = ' '.join(str(e) for e in ctx.args) + ' = ' + response[-1]['return-value']
        await ctx.reply(msg)
