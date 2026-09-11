from contextlib import nullcontext
from discord.ext.commands import cog
import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# Load the secret token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# set up specific intents
intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f"Logged in as {bot.user}")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)

deal_days = []

bogo_queues = {}

#commands
@bot.tree.command(name="bogo", description="Pairs two people for BOGO day pass deal.")
async def bogo(interaction: discord.Interaction):
  global bogo_queues
  #need to make sure we don't pair people up across servers
  server_id = interaction.guild_id
  waiting_user = bogo_queues.get(server_id)
  if waiting_user is None:
    bogo_queues[server_id] = interaction.user
    await interaction.response.send_message(f"{interaction.user.mention} is in the BOGO queue! Waiting for a second person.")
  else:
    if waiting_user.id == interaction.user.id:
      await interaction.response.send_message(f"{interaction.user.mention} is already in the BOGO queue waiting for someone else!")
      return
    await interaction.response.send_message(f"Paired {interaction.user.mention} with {waiting_user.mention}. Happy climbing!")
    bogo_queues[server_id] = None

if TOKEN is not None:
  bot.run(TOKEN)