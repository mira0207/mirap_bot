import os
from discord.ext import commands
import discord
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("已上線")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(995592963839250464)
    await channel.send(f'{member} 加入了我們!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1002904222695702548)
    await channel.send(f'{member} 離開')


@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 1222532492158828654:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

        if payload.emoji.name == '🎮':
            role = discord.utils.get(guild.roles, name='大高玩')
        elif payload.emoji.name == '🌏':
            role = discord.utils.get(guild.roles, name='genshin')
        elif payload.emoji.name == '🔫':
            role = discord.utils.get(guild.roles, name='fps')
        elif payload.emoji.name == '🪓':
            role = discord.utils.get(guild.roles, name='minecraft')
        # elif payload.emoji.name == '🖥️':
        #     role = discord.utils.get(guild.roles, name='資工好朋友')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id,
                                        guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")


@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 1222532492158828654:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

        if payload.emoji.name == '🎮':
            role = discord.utils.get(guild.roles, name='大高玩')
        elif payload.emoji.name == '🌏':
            role = discord.utils.get(guild.roles, name='genshin')
        elif payload.emoji.name == '🔫':
            role = discord.utils.get(guild.roles, name='fps')
        elif payload.emoji.name == '🪓':
            role = discord.utils.get(guild.roles, name='minecraft')
        # elif payload.emoji.name == '🖥️':
        #     role = discord.utils.get(guild.roles, name='資工好朋友')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id,
                                        guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")


@bot.command()
async def react(ctx):
    embed = discord.Embed(
        title="身分組選擇",
        description=
        "🎮大高玩 [你是最棒的高玩，你將會看到所有遊戲頻道]\n\n🌏原神區 [你只會看到原神區的頻道]\n\n🔫fpa區 [你只會看到fps區的頻道]\n\n🪓MINECRAFT區 [你只會看到MINECRAFT區的頻道]",
        color=0xffffff)
    await ctx.send(embed=embed)
    message = "點擊表情符號領身分、再次點擊取消 :heart_decoration:"
    react_messasge = await ctx.send(message)
    await react_messasge.add_reaction(emoji='🎮')
    await react_messasge.add_reaction(emoji='🌏')
    await react_messasge.add_reaction(emoji='🔫')
    await react_messasge.add_reaction(emoji='🪓')


@bot.command()
async def fuck(ctx):
    message = "操 騷逼 操 叫爸爸"
    await ctx.send(message)


@bot.command()
async def servermessage(ctx):
    embed = discord.Embed(title="伺服器資訊",
                          description="\n\n IP: 125.229.252.99 \n\n ",
                          color=0xff0000)
    await ctx.send(embed=embed)


@bot.command()
async def close(ctx):
    if ctx.message.author.id == 422001149860904960:
        await ctx.send("機器人關閉中...")
        await bot.close()
    else:
        await ctx.send("抱歉，你沒有權限關閉機器人。")


keep_alive()
bot.run(
    'OTk1MzUyODc5ODE4ODY2NzI4.GA0Uub.q2I96ckRbvXTaHythXyK81cZJOSdWvlM_zJaQM')
