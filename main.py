# This example requires the 'message_content' intent.
#app id:1129674463118626898
#public_KEY:c59ab9a3073b6c84fdbbb8d9af8ee82816238f3135fea249d6db1882c62cbe9e

import discord 
import os
import openai


  
#you shold creat open ai api key
#discord bot token
openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("SECRET_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        
          print(f'Message from {message.author}: {message.content}')
          
          if self.user!= message.author:
              if self.user in message.mentions:
                channel=message.channel
                response = openai.Completion.create(
                  model="text-davinci-003",
                  prompt = message.content,
                  temperature=1,
                  max_tokens=256,
                  top_p=1,
                  frequency_penalty=0,
                  presence_penalty=0
                )
                channel = message.channel
                messageToSend = response.choices[0].text
                await channel.send(messageToSend)    
       
            
      

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
