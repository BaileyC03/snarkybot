import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '>')


@client.event
async def on_ready():
    print("Bot Is Ready..")

@client.event
async def on_member_join(member):
  print(f'{member} has joined the server.')
  await member.send("Welcome!")

@client.event
async def on_member_ban(member):
    print("Lmao cya bitch" ,member)
    await member.send(member, "has been banned for being an idiot")

@client.command()
async def ping(ctx):
    randomnum = random.randint(1,9)
    angrywords = ["skrub","cretin","swine","idiot","noob","very lovely person <3", "devilspawn","creature","whench","simp"]
    randomangry = angrywords[randomnum]
    ping1 =(client.latency)
    ping2 = (ping1*1000)
    ping3 = round(ping2)
    print("User has asked for ping.")
    print(ping3)
    print("Ping Request Finalised")
    await ctx.send(f' Please be quiet you {randomangry} (btw your ping is {ping3}ms)')
    

@client.command()
async def speech(ctx):
    await ctx.send("Hello! Are we having a chat? How are you doing?")

@client.command()
async def Hi(ctx):
    await ctx.send("Yo...")

@client.command()
async def How_are_you(ctx):
    await ctx.send("Pretty good thanks, you?")

@client.command()
async def This_shows_the_basic_functionality_of_the_bot(ctx):
    await ctx.send("I guess so, its currently hard coded aside from the latency one which is technically using random words?")

@client.command()
async def How_many_inputs_does_this_have?(ctx):
    await ctx.send("It currently has 5 inputs. This isn't the way I want to create the bot however so I am going to have to look at the documentation to try and figure out how this works - Bailey")

client.run('NzQwODg5ODY4NDQzNTgyNTg0.XyvldQ.1AIn50qKzmw_pktX2tKIPa8ETN4')

    
