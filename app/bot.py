# This example requires the 'message_content' intent.

import discord
from tokens import discord_token

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
async def register(message, prefix):
    #save user details to database if not already existing
        #get user id, league username, and store
    split_message = message.content.split()
    if not len(split_message) == 2:
        await message.channel.send("Incorrect number of arguments")
        return
    else:
        id_discord = message.author.id
        id_league = message.content.split()[1]
        await message.channel.send(f'<@{id_discord}> has been linked to the account {id_league}')
    #return id


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    prefix = '$'

    if( len(message.content) > 0 and message.content[0] == prefix):
        if message.author == client.user:
            return

        if message.content.startswith(f'{prefix}hello'):
            await message.channel.send('Hello!')
        
        if(message.content.startswith(f'{prefix}connect')):
            # await message.channel.send(register(message,prefix))
            await register(message,prefix)

client.run(discord_token)
