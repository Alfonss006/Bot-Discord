
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
#C:\Users\Dhoser\Documents\asd
async def cetus(ctx):
    embed = discord.Embed(title="Cetus")
    r = requests.get('https://api.warframestat.us/pc/cetusCycle')
    contenido= r.json() # diccionario
    tiempo = contenido['timeLeft']
    estado = contenido['isDay']
    embed.add_field(name="tiempo restante", value=tiempo)
    if estado :
      embed.add_field(name="Estado del ciclo ",  value=" Esta de dia bro :c")
      embed.set_thumbnail(url="https://png2.kisspng.com/sh/0437f30297458a68691a636ba2c26a86/L0KzQYi4UsE3N5Y6eZGAYUO4c4q6UshiOmc2TZCCOEm3QYK6WME2OWQ5T6Y8NUS4RoaCTwBvbz==/5a35c9328a2615.7894113815134743545659.png")
    else:
      embed.add_field(name="Estado del ciclo ",  value=" Esta de noche bro :D")
      embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/865/PNG/512/Citycons_night_icon-icons.com_67936.png")
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Warframe"))
    print('Rempalago online')
bot.run('NTcwMjYyMDcyNTE2OTM1NzIy.XL8oLg.IdlJCRBSE7CpokgpQ8cL7kSxN8c')
