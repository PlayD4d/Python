import random
import discord
from discord.ext import commands
import yfinance as yf

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.command()
async def info(ctx, ticker_symbol: str):
    tData = yf.Ticker(ticker_symbol.upper())
    print(tData.info.keys())
    content = tData.info['symbol'] \
    + ' rPrice: ' + str(tData.info['regularMarketPrice']) \
    + ' rOpen: ' + str(tData.info['regularMarketOpen']) \
    + ' rPClose: ' + str(tData.info['regularMarketPreviousClose'])
    await ctx.send(content)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    await bot.process_commands(message)

bot.run('SECRET_TOKEN')
