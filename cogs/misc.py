import discord
from discord.ext import commands


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('.help for commands'))
        print('Bot is ready.')

    @commands.Cog.listener()
    async def on_command_error(self, context, error):
        if isinstance(error, commands.CommandNotFound):
            await context.send('Invalid command.')
        else:
            await context.send(f'{error}')

    @commands.command(aliases=['latency'], name='ping', help='To test latency')
    async def ping(self, context):
        await context.send(f'{round(self.client.latency * 1000)}ms')

    @commands.command(name='-.', help=".-.")
    async def emote1(self, context):
        await context.send('.-.')

    @commands.command(name='_.', help="._.")
    async def emote2(self, context):
        await context.send('._.')


def setup(client):
    client.add_cog(Misc(client))
