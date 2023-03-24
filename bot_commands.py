from discord.ext import commands

class BotCommands:
    def __init__(self, bot, color, commands_list):
        self.bot = bot
        self.color = color

        for command in commands_list:
            if command == 'test':
                bot.add_command(commands.Command(self.test, name='test'))
            elif command == 'hello':
                bot.add_command(commands.Command(self.hello, name='hello'))

    async def test(self, ctx):
        print(f"{self.bot.name} received test command")
        await ctx.send(f"{self.bot.name} is working!")

    async def hello(self, ctx):
        print(f"{self.bot.name} received hello command")
        await ctx.send(f"Hello, I am {self.bot.name}!")


from discord.ext import commands

class BotCommands:
    def __init__(self, bot, color, commands_list):
        self.bot = bot
        self.color = color

        for command in commands_list:
            if command == 'test':
                bot.add_command(commands.Command(self.test, name='test'))
            elif command == 'hello':
                bot.add_command(commands.Command(self.hello, name='hello'))

    async def test(self, ctx):
        print(f"{self.bot.name} received test command")
        await ctx.send(f"{self.bot.name} is working!")

    async def hello(self, ctx):
        print(f"{self.bot.name} received hello command")
        await ctx.send(f"Hello, I am {self.bot.name}!")


from discord.ext import commands

class BotCommands:
    def __init__(self, bot):
        self.bot = bot

        bot.add_command(commands.Command(self.test, name='test'))
        bot.add_command(commands.Command(self.hello, name='hello'))

    async def test(self, ctx):
        print(f"{self.bot.name} received test command")
        await ctx.send(f"{self.bot.name} is working!")

    async def hello(self, ctx):
        print(f"{self.bot.name} received hello command")
        await ctx.send(f"Hello, I am {self.bot.name}!")
