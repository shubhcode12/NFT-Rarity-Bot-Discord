import os
import discord
import urllib.request, json


from discord.ext.commands import Bot

bot = Bot(command_prefix='$')
# f = open('data.json')
# data = json.load(f)
#for i in data['collections']:
    #print(i['id'] +' | '+i['name']+' | ' + i['rank'])

#print(data["collections"][1]["name"])

client = discord.Client()

with urllib.request.urlopen("https://qzlsklfacc.medianetwork.cloud/nft_for_sale?collection=skeletoncrew") as url:
    parsed = json.loads(url.read().decode())
    print('welcome')


@bot.command()
async def ping(ctx):
    print("pong Called")
    await ctx.send('pong')

# purge channel all massages 
@bot.command(pass_context = True)
async def clear(ctx):
    await ctx.channel.purge()
    await ctx.send('Massaged Cleared ;)')


@bot.command()
async def rarity(ctx,id:int):
  embed = discord.Embed(color = discord.Colour.red())
  #await ctx.send('check started')
  for x in range(len(parsed)):
    #print(parsed[x]["id"])
    if parsed[x]["id"]==id:
      embed.set_image(url = parsed[x]["link_img"])
      await ctx.send(embed = embed)
      await ctx.send("NFT Name : "+parsed[x]["name"])
      await ctx.send("Attributes : "+parsed[x]["attributes"])
      
            
            
# @bot.command()
# async def rarity2(ctx, index:int):
#     embed = discord.Embed(color = discord.Colour.red())
#     embed.set_image(url = parsed[lastDigit(index)]["link_img"])
#     print(parsed[index]["name"])
#     await ctx.send(embed = embed)
#     await ctx.send(parsed[index]["name"] + ' Attributes : ' + parsed[index]["attributes"])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.content == '$test':
#         await message.channel.send('Testing 1 2 3')
#     await bot.process_commands(message)


#client.run(os.getenv('TOKEN'))
 
bot.run(os.getenv('TOKEN'))

