import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from handlers import start_handler, button_handler, help_handler, terms_handler, support_handler, error_handler

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Start the bot."""
    # Get bot token from environment variable
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not bot_token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable is not set!")
        return
    
    # Create the Application
    application = Application.builder().token(bot_token).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_handler))
    application.add_handler(CommandHandler("terms", terms_handler))
    application.add_handler(CommandHandler("support", support_handler))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # Register error handler
    application.add_error_handler(error_handler)
    
    # Get port from environment variable (Railway sets this automatically)
    port = int(os.getenv('PORT', 8000))
    
    logger.info(f"Starting bot on port {port}")
    
    # Start the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
