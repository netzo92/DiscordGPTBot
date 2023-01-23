import json
import os
import openai
import discord
discord.Bot

discord_token = None
with open("tokens.json", "r") as f:
  tokens = json.load(f)
  openai.api_key = tokens["openai"]
  discord_token = tokens["discord"]







intents = discord.Intents.default()
intents.message_content = (
    True  # < This may give you `read-only` warning, just ignore it.
)
# This intent requires "Message Content Intent" to be enabled at https://discord.com/developers


bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print("Ready!")


@bot.event
async def on_message(message: discord.Message):
    # Make sure we won't be replying to ourselves.
    if message.author.id == bot.user.id:
        return

    if message.content.startswith("!gpt"):
        print(message.author.id)
        print(message.content.split("!gpt")[-1])
        if message.author.id in (317242570231250944, 327809806574551040): #change these IDs to whichever users you want to authorize to use up your OpenAPI tokens
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=message.content.split("!gpt")[-1],
                temperature=0,
                max_tokens=60,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            await message.reply(response["choices"][0]["text"], mention_author=True)
        else:
            await message.reply("Sorry, right now only Met has authorization to use this command", mention_author=True)


bot.run(discord_token)

