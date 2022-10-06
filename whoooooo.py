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






client.run('vierd encrpyted shit')
