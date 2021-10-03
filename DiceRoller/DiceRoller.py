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
        await ctx.reply(ctx.message.content)
        if(ctx.message == ''):
            await ctx.reply('For syntax, see: <https://www.kreativekorp.com/dX/>')
            return
        r = requests.get(url = API, params = {'roll':ctx.message, 'format':'json', 'optimize':'false', 'evaluate':'true', 'expound':'true'})
        await ctx.reply(r.text)
        if(r.status_code != 200):
            await ctx.reply('Something went wrong - please try again later.')
            await RedBase.send_to_owners(ctx.message + '\nHTTP ' + r.status_code + '\nResponse: ' + r.raw)
            return
        response = r.json()
        if(response[0]['type'] == 'error'):
            """TODO: Print error. Provide syntax?"""
            return
        msg = ctx.content + ' = ' + response[-1]['return-value']
        await ctx.reply(msg)
