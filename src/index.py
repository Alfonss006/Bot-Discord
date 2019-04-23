
import discord
from discord.ext import commands
import requests
import re
#Bot para discord :D
bot = commands.Bot(command_prefix=':/', description= "este es el bot de warframe en teoria" )

@bot.command()
async def hola(ctx):
   await ctx.send('hey_muchachos_ustedes_escucharon_el_rempalago!!')

@bot.command()
#https://api.warframestat.us/pc/cetusCycle
async def cetus(ctx):
    embed = discord.Embed(title="Cetus")
    r = requests.get('https://api.warframestat.us/pc/cetusCycle')
    contenido= r.json() # diccionario
    tiempo = contenido['timeLeft']
    estado = contenido['isDay']
    embed.add_field(name="tiempo restante", value=tiempo)
    embed.set_thumbnail(
        url="https://vignette.wikia.nocookie.net/warframe/images/0/04/CetusWisp.png/revision/latest?cb=20171015035902")
    if estado=="true" :
      embed.add_field(name="Estado del ciclo ",  value=" Esta de dia bro :c")
    else:
      embed.add_field(name="Estado del ciclo ",  value=" Esta de noche bro :D")
    
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Warframe"))
    print('Rempalago online')
bot.run('NTcwMjYyMDcyNTE2OTM1NzIy.XL8oLg.IdlJCRBSE7CpokgpQ8cL7kSxN8c')
