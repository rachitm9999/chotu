@client.command()
async def avatar(ctx, *,  member : discord.Member=None):
    userAvatarUrl = member.avatar_url
    await ctx.send(userAvatarUrl)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid Command \n https://tenor.com/bbRqn.gif')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all the values i.e. tere baap ka raj chal rha hai kya , pura info de')

@client.event
async def on_member_join(member):
    print(f'@{member} has joined the server lets welcome that creature')
