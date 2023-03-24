from discord.ext import commands
from bot_commands import BotCommands

class CustomBot(commands.Bot):
    def __init__(self, name, command_prefix, intents, discord_app_token, hello_channel_id, color):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.name = name
        self.discord_app_token = discord_app_token
        self.target_channel_id = hello_channel_id
        self.color = color

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.process_commands(message)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"We have logged in as {self.user}")

        target_channel = self.get_channel(self.target_channel_id)

        if target_channel:
            await target_channel.send("I'm home! Did you miss me?!")
        else:
            print(f"Could not find channel with ID {self.target_channel_id}")

    def add_commands(self, commands_list):
        BotCommands(self, self.color, commands_list)



import discord
from discord.ext import commands
from bot_commands import BotCommands

class CustomBot(commands.Bot):
    def __init__(self, name, command_prefix, intents, discord_app_token, hello_channel_id, color):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.name = name
        self.discord_app_token = discord_app_token
        self.target_channel_id = hello_channel_id
        self.color = color

    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.process_commands(message)

    async def on_ready(self):
        print(f"We have logged in as {self.user}")

        target_channel = self.get_channel(self.target_channel_id)

        if target_channel:
            await target_channel.send("I'm home! Did you miss me?!")
        else:
            print(f"Could not find channel with ID {self.target_channel_id}")

    def add_commands(self, commands_list):
        BotCommands(self, self.color, commands_list)



import discord
from discord.ext import commands

class CustomBot(commands.Bot):
    def __init__(self, name, command_prefix, intents, discord_app_token, hello_channel_id, color):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.name = name
        self.discord_app_token = discord_app_token
        self.target_channel_id = hello_channel_id
        self.color = color

    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.process_commands(message)

    async def on_ready(self):
        print(f"We have logged in as {self.user}")

        target_channel = self.get_channel(self.target_channel_id)

        if target_channel:
            await target_channel.send("I'm home! Did you miss me?!")
        else:
            print(f"Could not find channel with ID {self.target_channel_id}")
