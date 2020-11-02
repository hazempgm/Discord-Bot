import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = "!")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')


# @client.event
# async def on_ready(ctx):
#     await ctx.send("Willkommen in die Rechnerarchitektur .")

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server .')

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command(aliases = ['nam', 'namm', 'zebb', 'zboub', 'dick', 'penis', '3asba'])
async def zeb(ctx):
    await ctx.send(zboub[random.randint(0, len(zboub))])


client.run("NzAwNjA1NzU1NDcxOTUzOTQw.XplYsw.vKX7s6hCUJMCfeAT4sw2xEQRszk")
