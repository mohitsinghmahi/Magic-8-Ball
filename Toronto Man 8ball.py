import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['yoo dis kids on something no kizzy',
                 'bro you bless? why da fuck would you think thats true 😂',
                 'Lowkey not lmao',
                 'Bruh what drugs are you on?',
                 'cro ur trippin',
                 'youre a wasteyute if you think thats true' ]
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
    

client.run('TOKEN')
