"""
Enhanced Configuration settings for the Telegram Cafe Bot with Add-to-Cart System
"""

import os

# Bot Token - get from environment variable
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "your_bot_token_here")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID", "admin_chat_id_here")

# Cafe Information
CAFE_NAME = "☕ The Artisan Cafe"
CAFE_TAGLINE = "Crafting Perfect Moments, One Cup at a Time"
CAFE_DESCRIPTION = """
Welcome to The Artisan Cafe! ☕✨

We're passionate about serving the finest coffee, freshly baked pastries, and delicious meals in a warm, welcoming atmosphere.

🌟 What makes us special:
• Premium coffee beans from around the world
• Freshly baked pastries daily
• Cozy atmosphere perfect for work or relaxation
• Friendly staff who love what they do
"""

# Contact Information
CAFE_PHONE = "+1 (555) 123-CAFE"
CAFE_EMAIL = "hello@artisancafe.com"
CAFE_ADDRESS = "123 Coffee Street, Brew City, BC 12345"
CAFE_HOURS = """
📅 Opening Hours:
Monday - Friday: 6:30 AM - 8:00 PM
Saturday - Sunday: 7:00 AM - 9:00 PM
"""

# Social Media
CAFE_WEBSITE = "www.artisancafe.com"
CAFE_INSTAGRAM = "@artisancafe"

# Order Information
ORDER_PHONE = "+1 (555) 123-ORDER"
ORDER_EMAIL = "orders@artisancafe.com"

# Cart and Order Settings
MAX_CART_ITEMS = 50
ORDER_TIMEOUT = 3600  # 1 hour in seconds
CURRENCY = '$'

# Order status options
ORDER_STATUS = {
    'PENDING': 'Pending',
    'CONFIRMED': 'Confirmed',
    'PREPARING': 'Preparing',
    'READY': 'Ready',
    'DELIVERED': 'Delivered',
    'CANCELLED': 'Cancelled'
}

# Data file paths
MENU_FILE = 'attached_assets/menu_data.json'
ORDERS_FILE = 'orders.json'

# Bot Messages
WELCOME_MESSAGE = f"""
🎉 {CAFE_NAME} 🎉

{CAFE_TAGLINE}

{CAFE_DESCRIPTION}

Use the buttons below to explore our menu, add items to your cart, and place orders directly through this bot!
"""

HELP_MESSAGE = """
🤖 How to use this bot:

/start - Welcome message and main menu
/menu - Browse our delicious menu
/cart - View your shopping cart
/contact - Get our contact information
/location - Find us and see our hours
/help - Show this help message

🛒 Shopping Features:
• Browse menu categories
• Add items to your cart
• Adjust quantities with + and - buttons
• Place orders directly through the bot
• Orders are sent to our kitchen automatically!
"""