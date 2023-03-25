import os
import yaml
import discord
from discord.ext import commands
from oaiapi import OAI817
from discordgpt.add_commands import BotCommands

class BU1LDaB07(commands.Bot):
    def __init__(self, config_path, *args, **kwargs):
        with open(config_path) as config_file:
            self.config = yaml.safe_load(config_file)

        super().__init__(command_prefix=self.config["key_trigger"], *args, **kwargs)
        self.build_a_bot_bit_by_bit = OAI817(self.config)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"We're serving looks and sass as {self.user.name} (ID: {self.user.id})")

        target_channel = self.get_channel(self.config["hello_channel_id"])

        if target_channel:
            await target_channel.send("I'm home! Did you miss me?!")
        else:
            print(f"Could not find channel with ID {self.config['hello_channel_id']}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.process_commands(message)

    def add_commands(self, commands_list):
        BotCommands(self, self.config["color"], commands_list)

# This is a common Python idiom to differentiate between running a script as the main program and importing it as a module.
if __name__ == "__main__":
    bot = BU1LDaB07("config/bot_config.yaml")
    bot.add_commands(["test", "hello", "gpt"])  # Example usage of the add_commands method
    bot.run(bot.config["discord_token"])
# If the file is being imported as a module in another script, this block of code won't be executed.
