import keep_alive
import discord
import os
import requests
import json


client = discord.Client()


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.load(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0] ['a']
  return(quote)


@client.event
async def on_ready():
  print('We Have Logged In As {0.user}'.format(client))

  
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!developer'):
    await message.channel.send('https://github.com/FuegoDev')
  if message.content.startswith('!moo'):
    await message.channel.send('moo, moo')
  if message.content.startswith('!grass'):
    await message.channel.send('*monch cronch*')
  if message.content.startswith('!mooo'):
    await message.channel.send('Stfu Annoying Ass Hoe')
  if message.content.startswith('!help'):
    await message.channel.send('@everyone `The Person Is A Fucking pussy and needs help`')
  if message.content.startswith('!commands'):
    await message.channel.send('`!moo, !mooo, !grass, !robocow`')
  if message.content.startswith('chicken'):
    await message.channel.send('https://youtu.be/YHj1jbmnMCE')
  if message.content.startswith('!ape'):
    await message.channel.send('https://www.youtube.com/watch?v=GhxqIITtTtU')
  if message.content.startswith('!robocow'):
    await message.channel.send('https://www.google.com/search?q=robot+cow&rlz=1C1CHBF_enUS917US917&tbm=isch&source=iu&ictx=1&fir=jjYTGVTr3noWvM%252CbsQNgs2dHmexvM%252C_&vet=1&usg=AI4_-kRdxDpndamwrPbP0yb9wjMVzm4UNw&sa=X&ved=2ahUKEwiXzefb2MzuAhWJ4J4KHcQ1A_4Q9QF6BAgJEAE&biw=1920&bih=947#imgrc=jjYTGVTr3noWvM')
  






keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))