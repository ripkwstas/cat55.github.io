import discord
import random
import aiofiles
import DiscordUtils
from discord.ext import commands

client = commands.Bot(command_prefix= '.', intents=discord.Intents.all())


@client.event
async def on_ready():
    game = discord.Game("SELECT DISCORD GAME STATUS")
    await client.change_presence(status=discord.Status.online, activity=game)
    print(f'{client.user} has connected to Discord!')

@client.command(pass_context = True)
async def clear(ctx, amount=100):
    if ctx.message.author.guild_permissions.administrator:
          await ctx.channel.purge(limit=amount)
    else:
      embed = discord.Embed(title = ":x_:Sorry, but you do not have permissions to perform this action!", color = discord.Colour.red())
      await ctx.send(embed=embed)

@client.command(pass_context = True) 
async def kick(ctx, member : discord.Member, * , reason=None): 
    if ctx.message.author.guild_permissions.administrator:
          await member.kick(reason=reason)
          embed = discord.Embed(description = f"**:white_check_mark:  {member.name}#{member.discriminator} has been successfully kicked!**")
          await ctx.send(embed=embed)
    else:
     embed = discord.Embed(title = ":x_:Sorry, but you do not have permissions to perform this action!", color = discord.Colour.red())
     await ctx.send(embed=embed)


@client.command(pass_context = True) 
async def ban(ctx, member : discord.Member, * , reason=None): 
    if ctx.message.author.guild_permissions.administrator:
          await member.ban(reason=reason)
          embed = discord.Embed(description = f"**:✅:   {member.name}#{member.discriminator} has been successfully banned!**")
          await ctx.send(embed=embed)
    else:
     embed = discord.Embed(title = ":x_:Sorry, but you do not have permissions to perform this action!", color = discord.Colour.red())
     await ctx.send(embed=embed)     

@client.command()
@commands.has_permissions(administrator=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = False)

    await ctx.send('𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗹𝗼𝗰𝗸𝗲𝗱 🔒')

@client.command()
@commands.has_permissions(administrator=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = True)

    await ctx.send('𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝘂𝗻𝗹𝗼𝗰𝗸𝗲𝗱 🔓')




@client.command(pass_context = True) 
async def unban(ctx, *, member): 
    if ctx.message.author.guild_permissions.administrator:
          banned_users = await ctx.guild.bans()
          member_name, member_discriminator = member.split('#')

          for ban_entry in banned_users:
              user = ban_entry.user

              if (user.name, user.discriminator) == (member_name, member_discriminator):
                  await ctx.guild.unban(user)
                  embed = discord.Embed(description = f"**:white_check_mark:  {member_name}#{member_discriminator} has been successfully unbanned!**")
                  await ctx.send(embed=embed)     
          return
    else:
          embed = discord.Embed(title = ":x_:Sorry, but you do not have permissions to perform this action!", color = discord.Colour.red())
          await ctx.send(embed=embed)   

@client.command()
async def eptlay(ctx):
    await ctx.send('skase kaneis den noiazete')


@client.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
     member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
    title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@client.command(case_insensitive=True)
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()

    await ctx.send(f"{text}")

client.run ('YOUR KEY HERE')
