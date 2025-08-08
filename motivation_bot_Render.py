from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os
"""
Motivation Bot for Telegram
---------------------------
This bot sends motivational quotes to users. It is part of the shkhtdnv project and is designed to provide inspiration and encouragement.
Author: shkhtdnv
Project of channel shkhtdnv (https://t.me/shkhtdnv_path)
"""

# List of commands for the bot
commands = [
    BotCommand("start", "Start the bot"),
    BotCommand("help", "Get help with the bot"),
    BotCommand("motivate", "Get a motivational quote"),
]

# List of motivational quotes
quotes = [
    "You didn’t come that far just to come that far",
    "Win in private", 
    "In a world filled with hate, we must still dare to rise", 
    "With self-discipline most anything is possible", 
    "The earth has music for those who listen",
    "Arise. While there is still time for it",
    "Take rest; a field that has rested gives a bountiful crop",
    "Winner is a same dreamer who never gives up",
    "Winner is just a loser who tried one more time",
    "Do not be afraid to start your own empire",
    "Being defeated is often a temporary condition. Giving up is what makes it permanent",
    "Being weird for others is OKAY",
    "Losses are the part of the game",
    "Just begin",
    "Come rain or shine, you gotta grind",
    "If not about yourself, then for your family",
    "Manage your time, or it will manage you",
    "Planning ahead is the key to success",
    "Discover yourself in silence",
    "Discipline beats motivation",
    "Obsession beats talent",
    "Yes, you can",
    "Yesterday you said tomorrow",
    "Fake it till you make it",
    "You’re the designer of your destiny; you are the author of your story; DO NOT LET IT BE BORING",
    "Till you’re alive, you can change your life",
    "If you’re going through hell, keep going",
    "No Pain, No Gain",
    "Dream your biggest, be your greatest",
    "Nobody will save you"
]

# Global variables to manage quotes
shuffled_quotes = []
quote_index = 0

# function to get the next quote
def get_next_quote():
    """Get the next motivational quote from the shuffling list
        
    If the list is empty or all quotes have been used, random shuffle will happen again."""
    global shuffled_quotes, quote_index

    if not shuffled_quotes or quote_index >= len(shuffled_quotes):
        shuffled_quotes = random.sample(quotes, len(quotes))  # перемешиваем
        quote_index = 0

    quote = shuffled_quotes[quote_index]
    quote_index += 1
    return quote

# Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command and send a welcome message."""
    await update.message.reply_text(
        """You are welcomed by a bot to send motivational phrases.

This project was created by the [shkhtdnv] channel (https://t.me/shkhtdnv_path ) and is a part of it. Quotes are available in English and are mostly taken from open sources (they are not copyrighted). If you want to add your quote, then write a request to [shkhtdnv Chat.](https://t.me/shkhtdnvChat )

To help, click /help""",
        parse_mode='Markdown'
    )

# Command /help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command and send a help message."""
    await update.message.reply_text("""Click /start to learn about the creators and purpose of the bot.

Click /motivate to get a motivational quote.""")

# Command /motivate
async def motivate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /motivate command and send a motivational quote."""
    await update.message.reply_text(get_next_quote())

# Setup commands for the bot
async def setup_commands(app):
    """Set up the bot commands."""
    await app.bot.set_my_commands(commands)

# Main
TOKEN = os.getenv("TELEGRAM_MOTIVATIONAL_BOT_TOKEN")
app = ApplicationBuilder().token(TOKEN).post_init(setup_commands).build()

# Command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("motivate", motivate))

# Long polling
app.run_polling()