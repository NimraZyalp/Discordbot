import discord
from discord import *
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import config
import random
import time
import json
from time import *
import praw
import asyncio

client = commands.Bot(command_prefix='wb ')
client.remove_command("help")

@client.event
async def on_ready():
    await client.wait_until_ready()
    guilds = len(list(client.guilds))
    await client.change_presence(activity=discord.Game(name=f'@me | Being a waifu in {guilds} servers!'))
    print("Bot is online!")

@client.event
async def on_guild_join(guilds):
    guilds = len(list(client.guilds))
    await client.change_presence(activity=discord.Game(f"@ me | Im in {guilds} servers"))
@client.event
async def on_guild_remove(guilds):
    guilds = len(list(client.guilds))
    await client.change_presence(activity=discord.Game(f"@ me | Being a waifu {guilds} servers"))

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour=discord.Colour.red(),
        title="ワイフゾーン"
    )
    embed.set_author(name="Command List", icon_url="https://cdn.discordapp.com/avatars/741070653985390603/3d7d754f68aa4855dc6a2445eed52dd9.png?size=128")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/741070653985390603/3d7d754f68aa4855dc6a2445eed52dd9.png?size=128")
    embed.add_field(name="‎‎‎", value="**Type ``wb help [command]`` for more info on a command!**\n"
                                                                                                 "\n⚠ Moderation - ``Kick``, ``Ban``, ``Warn``, ``Mute / Unmute``, ``Whois``\n"
                                                                                                 "\n**🖼️ Images** - ``Memes``, ``Dankmemes``, ``Waifu``\n"
                                                                                                 "\n**💎 Fun / Other** - ``Dad``, ``DM``, ``Question``, ``Fight``, ``Kill``, ``Ping``, ``Debugping``, ``Users``\n"
                                                                                                 "\n🔞 NSFW - ``Hentai``, ``Porn``\n"
                                                                                                 "\n[Add me to your server!](https://discord.com/oauth2/authorize?client_id=741070653985390603&permissions=8&scope=bot)"
                                                                                                 "\n[Join the WaifuZone Discord Server!](https://discord.gg/DfQa3Es)")
    embed.set_footer(text="Creator: 𝐈𝐜𝐡𝐢𝐠𝐨#0002")
    await ctx.send(embed=embed)

@client.command(pass_context=True, aliases=["ms"])
async def ping(ctx):
    await ctx.send(f'My ping: ``{round(client.latency * 1000)}`` ms')

@client.command(pass_context=True, aliases=["dp"])
async def debugping(ctx):
    await ctx.send(f'My debug ping: ``{(client.latency * 1000)}`` ms')

@client.command()
async def info(ctx):
    embed = discord.Embed(
        colour=discord.Colour.red(),
        title="WaifuZone Info"
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/741070653985390603/3d7d754f68aa4855dc6a2445eed52dd9.png?size=128")
    embed.add_field(name="‎‎‎‎", value="[Add me to your server!](https://discord.com/oauth2/authorize?client_id=741070653985390603&permissions=8&scope=bot)"
                                   "[Join the WaifuZone Discord Server!](https://discord.gg/DfQa3Es)"
                                   "\n[GitHub]("


@client.command(aliases=["meme"])
async def memes(ctx):
    reddit = praw.Reddit(client_id="$$$",
                         client_secret="$$$",
                         user_agent="$$$"
                         )
    reddit.read_only = True
    subreddit = reddit.subreddit('memes')
    pick_post = random.randint(1, 50)
    memes = reddit.subreddit("memes").hot()
    for i in range(0, pick_post):
        submission = next(x for x in memes if not x.stickied)
    embed = discord.Embed(
        colour=discord.Colour.red(),
        title=f"**{submission.title}**"
    )
    embed.set_image(url=submission.url)
    embed.set_footer(text=f"Creator: {submission.author}    👍 {submission.score} | 💬 {submission.num_comments}")
    await ctx.send(embed=embed)

@client.command(aliases=["dankmeme"])
async def dankmemes(ctx):
    reddit = praw.Reddit(client_id="$$$",
                         client_secret="$$$",
                         user_agent="$$$"
                         )
    reddit.read_only = True
    subreddit = reddit.subreddit('dankmemes')
    pick_post = random.randint(1, 50)
    memes = reddit.subreddit("dankmemes").hot()
    for i in range(0, pick_post):
        submission = next(x for x in memes if not x.stickied)
    embed = discord.Embed(
        colour=discord.Colour.red(),
        title=f"**{submission.title}**"
    )
    embed.set_image(url=submission.url)
    embed.set_footer(text=f"Creator: {submission.author}    👍 {submission.score} | 💬 {submission.num_comments}")
    await ctx.send(embed=embed)

@client.command(aliases=["animegirl"])
async def waifu(ctx):
    reddit = praw.Reddit(client_id="$$$",
                         client_secret="$$$",
                         user_agent="$$$"
                         )
    reddit.read_only = True
    subreddit = reddit.subreddit('waifu')
    pick_post = random.randint(1, 50)
    memes = reddit.subreddit("waifu").hot()
    for i in range(0, pick_post):
        submission = next(x for x in memes if not x.stickied)
    embed = discord.Embed(
        colour=discord.Colour.red(),
        title=f"**{submission.title}**"
    )
    embed.set_image(url=submission.url)
    embed.set_footer(text=f"Author: {submission.author}")
    await ctx.send(embed=embed)

@client.command(aliases=["porno", "sex"])
async def porn(ctx):
    reddit = praw.Reddit(client_id="$$$",
                         client_secret="$$$",
                         user_agent="$$$"
                         )
    reddit.read_only = True
    subreddit = reddit.subreddit('milfs')
    pick_post = random.randint(1, 50)
    memes = reddit.subreddit("milfs").hot()
    for i in range(0, pick_post):
        submission = next(x for x in memes if not x.stickied)
    embed = discord.Embed(
        colour=discord.Colour.red(),
        title=f"**{submission.title}**"
    )
    embed.set_image(url=submission.url)
    embed.set_footer(text=f"Author: {submission.author}")
    if ctx.channel.is_nsfw():
        await ctx.send(embed=embed)
    else:
        await ctx.send("You must be in an NSFW channel to use this command!")

@client.command()
async def hentai(ctx):
    reddit = praw.Reddit(client_id="$$$",
                         client_secret="$$$",
                         user_agent="$$$L"
                         )
    reddit.read_only = True
    subreddit = reddit.subreddit('hentai')
    pick_post = random.randint(1, 50)
    animegifs = reddit.subreddit("hentai").hot()
    for i in range(0, pick_post):
        submission = next(x for x in animegifs if not x.stickied)
    embed = discord.Embed(
        colour=discord.Colour.red(),
        title=f"**{submission.title}**"
    )
    embed.set_image(url=submission.url)
    embed.set_footer(text=f"Author: {submission.author}")
    if ctx.channel.is_nsfw():
        await ctx.send(embed=embed)
    else:
        await ctx.send("You must be in an NSFW channel to use this command!")

@client.command(aliases=["q"])
async def question(ctx, choice):
    questionList = ["No. ", "Yes. ", "Maybe ", "Idk ", "I'm not sure. ", "Positively. ", "Definitely. ", "Fuck no. ", "Are you retarded? No dumbass. "]
    await ctx.send(random.choice(questionList))

@question.error
async def questionerror(ctx, choice):
    await ctx.send("You have to ask a question dumbass.")

@client.command()
async def fight(ctx, user: discord.Member):
    fightOutcomes = [f"{ctx.author.mention} beat {user.mention} up until they tapped out of the fight!",
                     f"{user.mention} beat {ctx.author.mention} up until they tapped out of the fight!",
                     f"{ctx.author.mention} knocked {user.mention} out by using his quick maths.",
                     f"{user.mention} knocked {ctx.author.mention} out by using his quick maths."]
    if not member:
        await ctx.send("Please specify a person to fight!")
        return
    await ctx.send(f"{ctx.author.mention} is starting a fight with {user.mention}!")
    await asyncio.sleep(3)
    await ctx.send("The Fight has started! 🥊")
    await asyncio.sleep(5)
    await ctx.send(f"{random.choice(fightOutcomes)}")
    await asyncio.sleep(2)

@fight.error
async def fight_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a member to fight!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("I couldn't find that member! Please specify an actual member of the server!")

@client.command()
async def kill(ctx, user: discord.Member):
    killOutcomes = [f"{ctx.author.mention} failed to kill {user.mention}. He / She went to prison in result.",
                     f"{ctx.author.mention} killed {user.mention} with a knife. Epic!",
                     f"{ctx.author.mention}'s clumsy ass failed to kill {user.mention}. He / She is now on trial for murder.",
                     f"{ctx.author.mention} killed {user.mention} with an AR15. Epic!",
                    f"{ctx.author.mention} tried to stab {user.mention}, but {user.mention} took the knife and stabbed {ctx.author.mention}! Brutal!",
                    f"{user.mention} tried to stab {ctx.author.mention} in self defense, but it backfired and {ctx.author.mention} stabbed him in the face."]
    if not member:
        await ctx.send("Please specify a person to fight!")
        return
    await ctx.send(f"{ctx.author.mention} is attempting to assasinate {user.mention}!")
    await asyncio.sleep(10)
    await ctx.send(f"{ctx.author.mention} has broken into {user.mention}'s house!")
    await asyncio.sleep(10)
    await ctx.send(f"{ctx.author.mention} and {user.mention} are fighting!")
    await asyncio.sleep(10)
    await ctx.send(f"{random.choice(killOutcomes)}")

@client.command()
async def dm(ctx, user: discord.Member, *, reason=None):
    ch = ctx.channel
    await user.send(f"From {ctx.author.mention}: `{reason}` ")
    await ctx.send("I have sent the user a DM!")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.author.dm_channel
    waitfor = await client.wait_for('message', check=check)
    await ctx.send(f'{user.mention} has responded with ``{waitfor.content}``!')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member!")
        return
    if member.guild_permissions.ban_members == True:
        await ctx.send("I do not have permission to ban this member!")
        return
    await member.ban()
    await ctx.send(f"{member.mention} has been banned!")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You must have ``BAN_MEMBERS`` permissions to use this command!")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member!")
        return
    if member.guild_permissions.kick_members == True:
        await ctx.send("I do not have permission to kick this member!")
        return
    await member.ban()
    await ctx.send(f"{member.mention} has been kick!")


@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, reason):
   await ctx.send(f'{member.mention} has been warned! Reason: {reason}')

@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You must have ``KICK_MEMBERS`` permissions to use this command!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a member to warn!")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You must have ``KICK_MEMBERS`` permissions to use this command!")

@client.command(aliases=["clean", "purge"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Cleared ``{amount}`` messages!')

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You must have ``MANAGE_MESSAGES`` permissions to use this command!')

@client.command(aliases = ["users"])
async def usersss(ctx):
    mem = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
    await ctx.send(f"Number of users in the server:   ``{str(mem)}``")

@client.command(aliases=["whois", "user", "ui", "who"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role.mention for role in member.roles[1:]]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title="User Info")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="Name:", value=member)
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Status:", value=member.status)
    embed.add_field(name="Activity:", value=member.activity)
    embed.add_field(name="Bot?", value=member.bot)

    embed.add_field(name="Roles:", value="@everyone, " + ", ".join([role for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention if member.top_role != "@everyone" else "None")
    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a %#d %B %Y, %I:%M %p UTC"))
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@client.event
async def on_message(message):
    message.content = message.content.lower().replace  (' ', ' ')
    await client.process_commands(message)
    if message.content == "<@!741070653985390603>":
        await message.channel.send('My prefix is ``wb``\n Type ``wb help`` for the list of my commands!')

    if message.content.startswith('im '):  # Checking if it starts with `im [input]`
        strsplit = message.content.split("im ")  # Getting [input]
        strsplit2 = ''.join(strsplit)  # Joining the split 0 and " "
        if strsplit2 == "dad":
            await message.channel.send(f"You aren't dad, don't be silly!")
            return
        if strsplit2 == "mom":
            await message.channel.send("Hi honey, I'm dad!")
            return
        await message.channel.send(f"Hi {strsplit2}, I'm dad!")

    elif message.content.startswith("i'm "):  # Checking if it starts with `im [input]`
        strsplit = message.content.split("i'm ")  # Getting [input]
        strsplit2 = ''.join(strsplit)  # Joining the split 0 and " "

        if strsplit2 == "dad":
            await message.channel.send(f"No you aren't, don't be silly!")
            return
        if strsplit2 == "mom":
            await message.channel.send("Hi honey, I'm dad!")
            return
        await message.channel.send(f"Hi {strsplit2}, I'm dad!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found! For a list of all commands, type ``wb help``")

client.run("$$$")
