import discord
from discord.ext import commands , tasks
from itertools import cycle

client = commands.Bot(command_prefix = '!')
status_loop = cycle(['getting fucked by BBC', 'Sucking my own dick'])

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')




@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(status = discord.Status.online , activity = discord.Game(next(status_loop)))

@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used i.e. mtlb kuch bhii !!')

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete i.e. abe bhele pura history udane ka irada hai kya !!')


@client.command()
async def hello(ctx):
    await ctx.send("@everyone What's up!!")

@client.command(aliases = ['pong'])
async def ping(ctx, *, commen):
    await ctx.send(f'Ping is {round(client.latency * 1000)}ms')

@client.event
async def on_member_join(member):
    print(f'@{member} has joined the server to disturb everyone')

@client.event
async def on_member_remove(member):
    print(f'@{member} has left the server to let everybody live in peace')

@client.command()
async def kick(ctx, member : discord.Member, *, reason='idk'):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention} cuz he was a lauda')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all the values i.e. tere baap ka raj chal rha hai kya , pura info de')

@client.command()
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention} cuz he was a brutus')


@client.command()
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name , member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name , user.discriminator) == (member_name , member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention} cuz he went to haridwar to wash his faults')
            return






client.run('NzUzOTc2MDU1MzAzNTAzOTEz.X1uA6w.XGpRIw_tCjqGnnGpEJR5wJZ3l3s')
