from flask import Flask
import telebot
import random

app = Flask(__name__)

token = '7681308855:AAGnyZxlgXSMdogWou0geL0ExUGyGX0E5Xo'
bot = telebot.TeleBot(token)

# List of quotes and images as per your existing code

@app.route('/')
def health_check():
    return 'Bot is running', 200  # Health check endpoint

if __name__ == "__main__":
    bot.infinity_polling()  # Start bot polling
    app.run(host='0.0.0.0', port=8000)  # Run Flask on port 8000


# List of quotes
quotes = [
    "The great and powerful worm/shrimp creature Garloid!.",
    "The Garloids of all countries, unites!.",
    "I saw Garloids in my dark forest",
    "Agios O Garloid"
]


imagestable = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT2R5njwfGkW0e7ZjtZcaw6A6qp5IbHjviZA&s",
    "https://i.ytimg.com/vi/gi0Xk7MpFtY/oar2.jpg?sqp=-oaymwEiCPEEENAFSFqQAgHyq4qpAxEIARUAAAAAJQAAyEI9AICiQw==&rs=AOn4CLAe0ytnMPB-yhwhmAqTHfKZssL9Ww",
    "https://media.tenor.com/v9TjCSxji_AAAAAe/garloid-schlee.png"
]

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! I'm your bot. Type /help to see available commands.")

# Help command
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Available commands:\n"
                                      "/start - Start the bot\n"
                                      "/help - Show available commands\n"
                                      "/echo [text] - Repeat your text\n"
                                      "/reverse [text] - Reverse your text\n"
                                      "/quote - Get a random motivational quote\n"
                                      "/garloid - Sends image of Garloid")

# Echo command
@bot.message_handler(commands=['echo'])
def echo(message):
    text = message.text.replace("/echo", "").strip()
    if text:
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "Usage: /echo [text]")

# Reverse command
@bot.message_handler(commands=['reverse'])
def reverse(message):
    text = message.text.replace("/reverse", "").strip()
    if text:
        bot.send_message(message.chat.id, text[::-1])
    else:
        bot.send_message(message.chat.id, "Usage: /reverse [text]")


@bot.message_handler(commands=['garloid'])
def garloid(message):
    bot.send_photo(message.chat.id, random.choice(imagestable), caption="Here is Garloid!")




    
# Quote command
@bot.message_handler(commands=['quote'])
def quote(message):
    bot.send_message(message.chat.id, random.choice(quotes))

# Default handler for any other text messages
@bot.message_handler(content_types=['text'])
def default_response(message):
    bot.send_message(message.chat.id, "I don't understand that command. Use /help to see available commands.")

# Start polling
bot.infinity_polling()
