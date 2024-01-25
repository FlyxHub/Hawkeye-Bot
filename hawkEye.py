import discord
from discord.ext import commands
import math 

with open('token.txt', 'r') as tokenFile:
    token = tokenFile.read()

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot started. Logged in as {bot.user}.')

@bot.listen('on_message') #Invite URL scanner
async def onInvite(message):
    bannedLinks = ['discord.gg/', 'discord.com/invite/']
    logChannel = discord.utils.get(message.guild.channels, id=1199888600876204042) #Channel where logs will be posted
    promoChannel = discord.utils.get(message.guild.channels, id=1029802661853274144) #Channel where invites are allowed

    if message.channel is not promoChannel:
        for link in bannedLinks:
            if link in message.content:
                embed = discord.Embed(title=f'Invite posted in {message.channel.mention}')
                embed.set_thumbnail(url=message.author.display_avatar.url)
                embed.add_field(name='Invite posted by:', value=message.author.mention, inline=False)
                embed.add_field(name='Message:', value=f'"{message.content}"', inline=False)
                embed.set_footer(text=f'Sender UID: {message.author.id}')
                await logChannel.send(embed=embed)
                print('Invite logged.')
                await message.delete()
                print('Invite deleted.')
                await message.author.send(f'I see you posted an invite in **{message.guild.name}**. Invites are not allowed outside of the dedicated self-promo channel.')
                print('Invite poster warned.')
                return

@bot.command() #Purge command
@commands.has_permissions(manage_messages=True)
async def purge(ctx, count:int):
    await ctx.channel.purge(limit=count+1) #Add +1 to account for the command invokation
    await ctx.send(f'Purged {count} messages.')
    return
@purge.error #Purge error handler
async def purgeError(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Whoops! Looks like you're missing the `Manage Messages` permission required to run that command.")
        return
    elif isinstance(error, commands.BadArgument):
        await ctx.send(f'There was an error with your argument.')
        return
    else:
        await ctx.send(f'There was an error running that command, please try again.')
        return
    
@bot.command() #Kick command
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, reason:str=None):
    if not reason:
        reason = f'No reason provided. Kicked by {ctx.author.display_name}.'
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked from the server with reason: `{reason}`.')
    return
@kick.error #Kick error handler
async def kickError(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Whoops! Looks like didn't specify a member to kick. Try again with their user ID, their username, or ping them!")
        return
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Whoops! Looks like you're missing the `Kick Members` permission required to run that command.")
        return
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send(f"Uh oh! I don't have permission to kick that user.")
        return
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(f"I couldn't find that member. Make sure they're still here or try pinging them instead!")
        return
    else:
        await ctx.send(f'There was an error running that command, please try again.')
        return

@bot.command() #Ban command
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, reason:str=None):
    if not reason:
        reason=f'No reason provided. Banned by {ctx.author.display_name}.'
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned from the server with reason: `{reason}`.')
    return
@ban.error #Ban error handler
async def banError(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Whoops! Looks like didn't specify a member to ban. Try again with their user ID, their username, or ping them!")
        return
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Whoops! Looks like you're missing the `ban Members` permission required to run that command.")
        return
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send(f"Uh oh! I don't have permission to ban that user.")
        return
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(f"I couldn't find that member. Make sure they're still here or try pinging them instead!")
        return
    else:
        await ctx.send(f'There was an error running that command, please try again.')
        return

@bot.command() #Ping command
async def ping(ctx):
    latency = math.trunc(bot.latency*1000)
    await ctx.send(f":ping_pong: Pong! Bot latency: **{latency}MS**")
    return

bot.run(token)

#Hawkeye Bot written by Jake Hochstatter - CLDE 2022-2024
