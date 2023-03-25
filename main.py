import asyncio
import discord
from discordgpt.build_my_bot import CustomBot
from be_jaya_cfg import bot1_config
from be_clair_cfg import bot2_config

async def run_bot(bot):
    await bot.start(bot.discord_app_token)

async def main():
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False

    bot1 = CustomBot(**bot1_config


import asyncio
import bot1_config
import bot2_config
from custom_bot import CustomBot
from bot_commands import BotCommands
import discord

async def main():
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False

    bot1 = CustomBot(bot1_config.BOT_NAME, bot1_config.COMMAND_PREFIX, intents, bot1_config.DISCORD_APP_TOKEN, bot1_config.HELLO_CHANNEL_ID, "magenta")
    bot2 = CustomBot(bot2_config.BOT_NAME, bot2_config.COMMAND_PREFIX, intents, bot2_config.DISCORD_APP_TOKEN, bot2_config.HELLO_CHANNEL_ID, "cyan")

    BotCommands(bot1)
    BotCommands(bot2)

    await asyncio.g

