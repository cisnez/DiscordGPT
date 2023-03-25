from discord.ext import commands

class BotCommands:
    def __init__(self, bot, commands_list):
        self.bot = bot

        self.commands_mapping = {
            'test': self.test,
            'hello': self.hello,
            'gpt': self.gpt
        }

        for command in commands_list:
            if command in self.commands_mapping:
                bot.add_command(commands.Command(self.commands_mapping[command], name=command))

    @commands.Cog.listener()
    async def test(self, ctx):
        print(f"{self.bot.name} received test command")
        await ctx.send(f"{self.bot.id} is working!")

    @commands.Cog.listener()
    async def hello(self, ctx):
        print(f"{self.bot.name} received hello command")
        await ctx.send(f"Hello, I am {self.bot.name}!")

    @commands.Cog.listener()
    async def hello(self, ctx):
        print(f"{self.bot.name} received gpt command")
        await ctx.send(f"Future interface for OpenAi GPT!")
