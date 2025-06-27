"""Keyboard layouts for the Telegram bot."""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from menu_data import MENU_CATEGORIES

def get_main_menu_keyboard():
    """Create the main menu keyboard."""
    keyboard = []
    
    # Add category buttons (2 per row)
    categories = list(MENU_CATEGORIES.items())
    for i in range(0, len(categories), 2):
        row = []
        for j in range(2):
            if i + j < len(categories):
                cat_key, cat_info = categories[i + j]
                button_text = f"{cat_info['emoji']} {cat_info['name']}"
                row.append(InlineKeyboardButton(button_text, callback_data=cat_key))
        keyboard.append(row)
    
    # Add bottom action buttons
    keyboard.append([
        InlineKeyboardButton("❓ Help & Support", callback_data="help"),
        InlineKeyboardButton("📞 Contact Us", callback_data="support")
    ])
    
    return InlineKeyboardMarkup(keyboard)

def get_category_keyboard(category: str, items: list):
    """Create keyboard for a specific category."""
    keyboard = []
    
    # Add item buttons (1 per row for better readability)
    for item in items:
        button_text = f"{item['name']} - ${item['price']:.2f}"
        keyboard.append([InlineKeyboardButton(button_text, callback_data=f"item_{item['id']}")])
    
    # Add back to main menu button
    keyboard.append([InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")])
    
    return InlineKeyboardMarkup(keyboard)

def get_item_keyboard(item_id: str, category: str):
    """Create keyboard for item details."""
    keyboard = [
        [
            InlineKeyboardButton(f"↩️ Back to {MENU_CATEGORIES[category]['name']}", callback_data=category),
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")
        ]
    ]
    
    return InlineKeyboardMarkup(keyboard)

def get_help_keyboard():
    """Create keyboard for help message."""
    keyboard = [
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ]
    
    return InlineKeyboardMarkup(keyboard)
