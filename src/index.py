
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=':/', description= "este es el bot de warframe en teoria" )

@bot.command()
async def hola(ctx):
   await ctx.send('hey_muchachos_ustedes_escucharon_el_rempalago!!')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Warframe"))
    print('Rempalago online')
bot.run('NTcwMjYyMDcyNTE2OTM1NzIy.XL8oLg.IdlJCRBSE7CpokgpQ8cL7kSxN8c')