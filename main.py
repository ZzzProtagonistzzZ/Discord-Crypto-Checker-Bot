import requests 
import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import View

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
token = 'YOUR_BOT_TOKEN'


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user}:{bot.user.id}')

@bot.tree.command(name='check_price_usd', description='Check price of coin in USD')
async def check_price_usd(interaction: discord.Interaction, coin: str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    
    if response.status_code != 200:
        await interaction.response.send_message('ERROR could not fetch price', ephemeral=True)
    elif response.status_code == 200:
        data = response.json()
        price = data[coin.lower()]['usd']
        
        embed = discord.Embed(
            title = coin.upper(),
            color = 0x00FF00
        )
        
        embed.add_field(name='🟢Price', value=f'-- {price}')
    await interaction.response.send_message(embed=embed, ephemeral=True)
     
@bot.tree.command(name='check_price_eur', description='Check price of coin in EUR')
async def get_price_eur(interaction: discord.Interaction, coin: str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=eur"
    response = requests.get(url)
    
    if response.status_code != 200:
        await interaction.response.send_message('ERROR could not fetch price', ephemeral=True)
    elif response.status_code == 200:
        data = response.json()
        price = data[coin]['eur']

        embed = discord.Embed(
            title = coin.upper(),
            color = 0x00FF00
        )
        
        embed.add_field(name='🟢Price', value=f'-- {price}')
        await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.tree.command(name='check_price_gbp', description='Check price of coin in GBP')
async def check_price_gbp(interaction: discord.Interaction, coin:str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=gbp"
    response = requests.get(url)
    
    if response.status_code != 200:
        await interaction.response.send_message('ERROR could not fetch price')
    elif response.status_code == 200:
        data = response.json()
        price = data[coin]['gbp']
        
        embed = discord.Embed(
            title=coin.upper(),
            color= 0x00FF00
        )
        embed.add_field(name='🟢Price', value=f'-- {price}')
        await interaction.response.send_message(embed=embed, ephemeral=True)
        

bot.run(token)    
