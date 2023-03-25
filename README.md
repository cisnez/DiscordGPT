# DiscordGPT

## Description
A Discord bot using Discord API and OpenAI API to provide conversational functionality.

## Files
DiscordGPT/  
│  
├─ config/  
│   ├─ bot_config.yaml  
│   └─ tokens.py  
│  
├─ discordgpt/  
│   ├─ __init__.py  
│   ├─ build_my_bot.py  
│   ├─ add_commands.py  
│   └─ models/  
│       └─ __init__.py  
│  
└─ tests/  
    └─ __init__.py  

## Usage
1. Clone the repository to your local machine.
2. Install the required packages using `pip install -r requirements.txt`.
3. Configure your bot by creating a `be_whatever.yaml` file based on the `bot_config.yaml` template.
4. Create file config/keys.py with your OpenAi API Key
5. Create file config/tokens.py with your Discord Developer-Application-Bot-Token
6. Run the bot using `python main.py`.

## Note about Discord's Bot class.
Here are the built-in properties and attributes specifically for`discord.ext.commands.Bot`:

`command_prefix`: A string, a list of strings, or a callable that returns a string or list of strings. It defines the prefix(es) for the bot's commands. For example, if the command prefix is "!", users can invoke a command called hello by sending a message like !hello.

`description`: A string that provides a short description of the bot. It's displayed in the default help command provided by the bot.

`pm_help`: A boolean that indicates whether the help command should be sent as a private message when called in a server channel. Default is False.

`help_attrs`: A dictionary of attributes used to customize the default help command.

`help_command`: An instance of the HelpCommand class or its subclass that defines the bot's help command. You can set it to None to remove the help command.

`case_insensitive`: A boolean that indicates whether the bot should ignore the casing of command names and prefixes. Default is False.

`self_bot`: A boolean that indicates whether the bot should only listen to commands invoked by itself. Default is False.

`_BotBase__cogs`: An internal attribute that holds a dictionary of the bot's cogs.

`_BotBase__extensions`: An internal attribute that holds a dictionary of the bot's extensions.

`_BotBase__application_id`: An internal attribute that stores the bot's application ID.

`_BotBase__owner_id`: An internal attribute that stores the bot's owner ID.

`_BotBase__owner_ids`: An internal attribute that stores a set of the bot's owner IDs, if applicable.

These properties are specific to the `discord.ext.commands.Bot` class. However, since it's a subclass of `discord.Client`, it also inherits properties from that class. You can find the complete list of `discord.Client` properties in the official documentation:

`discord.Client`
https://discordpy.readthedocs.io/en/latest/api.html#discord.Client

Combining these properties allows you to create highly customizable Discord bots that can cater to your specific needs. 💅

## Tags
Discord, bot, chatbot, API, OpenAI, conversational AI
