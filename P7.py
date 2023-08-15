#IMPORTS
import discord
from discord.ext import commands

#BOT PREFIX
bot = commands.Bot(command_prefix='.', self_bot=True)

#LOCATING TOKEN
with open('token.txt', 'r') as f:
    token = f.read().strip()

#COMMANDS
@bot.event
async def on_ready():
    print('P7 IS RUNNING...')

@bot.command()
async def ping(ctx):
    ping = round(bot.latency * 1000)
    response = f'Pong! {ping}ms'
    await ctx.message.edit(response)

@bot.command()
async def pfp(ctx, user: discord.User):
    avatar_url = user.avatar.url
    await ctx.message.edit(avatar_url)

@bot.command()
async def info(ctx, user: discord.User):
    user_id = user.id
    username = user.name
    tag = user.discriminator
    created_at = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
    response = f'User ID: {user_id}\nUsername: {username+"#"+tag}\nAccount Creation Date: {created_at}'
    await ctx.message.edit(response)

#RUN BOT
bot.run(token)