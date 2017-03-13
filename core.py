#! /usr/bin/env python3
import botguts
import random

bot_commands = []

def sing(command):
    response = []
    response.append('Give me an "A"')
    response.append('Give me an "S"')
    response.append('Give me a "D"')
    response.append('Go, Go, ASD!')
    return response


asdsong = botguts.Bot_Command(call='asd song', response=sing)
bot_commands.append(asdsong)


def magic_8(string):
    magic = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes, definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]

    return random.choice(magic)


magic8 = botguts.Bot_Command(call='magic8', response=magic_8)
bot_commands.append(magic8)
