@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(status = discord.Status.online , activity = discord.Game(next(status_loop)))

@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)
