#!/usr/bin/env python3
"""
Enhanced Telegram Cafe Bot with Add-to-Cart System
Main application entry point
"""

import asyncio
import logging
import os
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters

from enhanced_handlers import (
    start_command,
    menu_command,
    cart_command,
    help_command,
    contact_command,
    location_command,
    handle_callback_query,
    handle_contact,
    handle_message
)
from enhanced_config import BOT_TOKEN

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Main function to run the enhanced bot"""
    try:
        # Create application
        application = ApplicationBuilder().token(BOT_TOKEN).build()
        
        # Add command handlers
        application.add_handler(CommandHandler("start", start_command))
        application.add_handler(CommandHandler("menu", menu_command))
        application.add_handler(CommandHandler("cart", cart_command))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("contact", contact_command))
        application.add_handler(CommandHandler("location", location_command))
        
        # Add callback query handler for inline keyboards
        application.add_handler(CallbackQueryHandler(handle_callback_query))
        
        # Message handlers for contact and text
        application.add_handler(MessageHandler(filters.CONTACT, handle_contact))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        logger.info("Starting Enhanced Cafe Bot with Add-to-Cart System...")
        
        # Start the bot with polling
        application.run_polling(allowed_updates=["message", "callback_query"])
        
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        raise

if __name__ == "__main__":
    main()