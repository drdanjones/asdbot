#! /usr/bin/env python3
import botguts

bot_commands = []

hello = botguts.Bot_Command('hello', response=lambda x: ['How are you?'])
bot_commands.append(hello)
