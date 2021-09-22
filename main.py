import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = ">", case_insensitive = True, intents = intents)

@client.event
async def on_ready():
  print('Entramos como {0.user}' .format(client))

@client.command()
async def ola(ctx):
  await ctx.send(f'Olá, {ctx.author}')

@client.command()
async def dado(ctx, numero):
  variavel = random.randint(1,int(numero))
  await ctx.send(f'O número que saiu no dado é {variavel}')

@client.event
async def on_member_join(member):
  canalboasvindas = client.get_channel(825509137273061387)
  regras = client.get_channel(833350786242052126)
  
  mensagem = await canalboasvindas.send(f"<a:verified_blue:810139686940573697> Bem vindo {member.mention}! Leias as regras em {regras.mention}")

  await asyncio.sleep(60)

  await mensagem.delete()




client.run('ODI3MzQ3OTA5NzcwNjA4Njcw.YGZtyQ.k5B_Z7sbWoeWQxDMqDQTurcC8yk')
