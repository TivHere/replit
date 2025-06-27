import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from menu_data import CAFE_MENU, MENU_CATEGORIES
from keyboards import get_main_menu_keyboard, get_category_keyboard, get_item_keyboard

logger = logging.getLogger(__name__)

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command."""
    welcome_message = (
        "✨ **COZY CORNER CAFE** ✨\n\n"
        "┌─ 🏮 WELCOME 🏮 ─┐\n"
        "│ Premium cafe experience\n"
        "│ Fresh • Fast • Delicious\n"
        "│ Now delivering to you!\n"
        "└─────────────────────┘\n\n"
        "🎯 **What's Special Today:**\n"
        "• 🔥 Fresh-brewed artisan coffee\n"
        "• 🥞 Made-to-order breakfast\n"
        "• 🚀 20-minute delivery promise\n"
        "• 💎 Premium ingredients only\n\n"
        "**Ready to indulge?**"
    )
    
    keyboard = get_main_menu_keyboard()
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=keyboard,
        parse_mode='Markdown'
    )

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command."""
    help_message = (
        "🤖 **Cafe Bot Help** 🤖\n\n"
        "**Commands:**\n"
        "• /start - Show main menu\n"
        "• /help - Show this help message\n"
        "• /terms - View Terms and Conditions\n"
        "• /support - Get customer support\n\n"
        "**Navigation:**\n"
        "• Use the buttons to browse our menu\n"
        "• Tap on items to see details and prices\n"
        "• Use 'Back' buttons to return to previous menu\n"
        "• Use 'Main Menu' to return to the start\n\n"
        "**Payment & Ordering:**\n"
        "• Select 'Order & Pay Now' for any item\n"
        "• Choose from FPX Banking, Touch 'n Go, or Card\n"
        "• Complete secure payment through your preferred method\n"
        "• Receive order confirmation and delivery updates\n\n"
        "Enjoy your visit to Cozy Corner Cafe!"
    )
    
    await update.message.reply_text(
        help_message,
        parse_mode='Markdown'
    )

async def terms_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /terms command."""
    terms_message = (
        "📋 **Terms and Conditions**\n\n"
        "**Cozy Corner Cafe Bot Terms of Service**\n\n"
        "**1. Service Agreement**\n"
        "By using this bot and placing orders, you agree to these terms and our payment policies.\n\n"
        "**2. Payment Processing**\n"
        "• We accept FPX Online Banking, Touch 'n Go eWallet, and Credit/Debit Cards\n"
        "• All payments are processed securely through certified payment providers\n"
        "• Prices include applicable taxes and service charges as displayed\n\n"
        "**3. Order Policy**\n"
        "• Orders are confirmed upon successful payment\n"
        "• Delivery time: 20-30 minutes during business hours\n"
        "• Cancellations must be requested within 5 minutes of order placement\n\n"
        "**4. Refund Policy**\n"
        "• Refunds available for cancelled orders or service issues\n"
        "• Processing time: 3-5 business days\n"
        "• Contact /support for refund requests\n\n"
        "**5. Contact Information**\n"
        "• Business Hours: 7 AM - 10 PM daily\n"
        "• Support: Use /support command\n"
        "• Location: Kuala Lumpur, Malaysia\n\n"
        "Last updated: June 27, 2025"
    )
    
    await update.message.reply_text(
        terms_message,
        parse_mode='Markdown'
    )

async def support_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /support command."""
    support_message = (
        "🛠️ **Customer Support**\n\n"
        "**Need Help?**\n"
        "We're here to assist you with any questions or issues.\n\n"
        "**Common Issues:**\n"
        "• Payment problems: Check your internet connection and try again\n"
        "• Order status: Your order confirmation includes tracking details\n"
        "• Delivery delays: Contact us if order is more than 45 minutes late\n"
        "• Refund requests: Provide your order ID for faster processing\n\n"
        "**Contact Methods:**\n"
        "📞 Phone: +60 3-1234-5678\n"
        "📧 Email: support@cozycornercafe.my\n"
        "⏰ Support Hours: 7 AM - 10 PM daily\n\n"
        "**For Immediate Help:**\n"
        "Please provide your order ID and describe the issue clearly.\n\n"
        "We typically respond within 15 minutes during business hours."
    )
    
    await update.message.reply_text(
        support_message,
        parse_mode='Markdown'
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses."""
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    try:
        if data == "main_menu":
            await show_main_menu(query)
        elif data in MENU_CATEGORIES:
            await show_category_menu(query, data)
        elif data.startswith("item_"):
            item_id = data.replace("item_", "")
            await show_item_details(query, item_id)
        elif data.startswith("back_"):
            category = data.replace("back_", "")
            await show_category_menu(query, category)
        else:
            await query.edit_message_text("❌ Unknown command. Please use /start to begin.")
            
    except Exception as e:
        logger.error(f"Error handling button press: {e}")
        await query.edit_message_text("❌ An error occurred. Please try again or use /start.")

async def show_main_menu(query) -> None:
    """Show the main menu."""
    welcome_message = (
        "☕ **Cozy Corner Cafe** ☕\n\n"
        "Please select a category from our menu:"
    )
    
    keyboard = get_main_menu_keyboard()
    
    await query.edit_message_text(
        welcome_message,
        reply_markup=keyboard,
        parse_mode='Markdown'
    )

async def show_category_menu(query, category: str) -> None:
    """Show items in a specific category."""
    category_info = MENU_CATEGORIES[category]
    items = CAFE_MENU[category]
    
    message = f"{category_info['emoji']} **{category_info['name']}** {category_info['emoji']}\n\n"
    message += f"{category_info['description']}\n\n"
    message += "Select an item to view details:"
    
    keyboard = get_category_keyboard(category, items)
    
    await query.edit_message_text(
        message,
        reply_markup=keyboard,
        parse_mode='Markdown'
    )

async def show_item_details(query, item_id: str) -> None:
    """Show details of a specific item."""
    # Find the item in all categories
    item = None
    category = None
    
    for cat, items in CAFE_MENU.items():
        for item_data in items:
            if item_data['id'] == item_id:
                item = item_data
                category = cat
                break
        if item:
            break
    
    if not item:
        await query.edit_message_text("❌ Item not found. Please try again.")
        return
    
    # Send photo with caption if available
    if 'image' in item:
        caption = f"🌟 **{item['name']}** 🌟\n\n"
        caption += f"┌─ 💎 PREMIUM SELECTION ─┐\n"
        caption += f"│ Price: ${item['price']:.2f}\n"
        caption += f"│ Category: {MENU_CATEGORIES.get(category or '', {}).get('name', 'Special')}\n"
        caption += f"│ Fresh • Artisan • Quality\n"
        caption += f"└───────────────────────┘\n\n"
        caption += f"📖 **About This Item:**\n{item['description']}\n\n"
        
        if 'ingredients' in item:
            caption += f"🥘 **Fresh Ingredients:**\n{item['ingredients']}\n\n"
        
        if 'allergens' in item:
            caption += f"⚠️ **Please Note:**\n{item['allergens']}\n\n"
        
        caption += f"🚀 **Ready in 15-20 minutes**\n"
        caption += f"🔥 **Made fresh when you order**"
        
        keyboard = get_item_keyboard(item_id, category or '')
        
        # Delete previous message and send photo
        await query.message.delete()
        await query.message.reply_photo(
            photo=item['image'],
            caption=caption,
            reply_markup=keyboard,
            parse_mode='Markdown'
        )
        return
    
    # Fallback to text if no image
    message = f"🌟 **{item['name']}** 🌟\n\n"
    message += f"┌─ 💎 PREMIUM SELECTION ─┐\n"
    message += f"│ Price: ${item['price']:.2f}\n"
    message += f"│ Category: {MENU_CATEGORIES.get(category or '', {}).get('name', 'Special')}\n"
    message += f"│ Fresh • Artisan • Quality\n"
    message += f"└───────────────────────┘\n\n"
    message += f"📖 **About This Item:**\n{item['description']}\n\n"
    
    if 'ingredients' in item:
        message += f"🥘 **Fresh Ingredients:**\n{item['ingredients']}\n\n"
    
    if 'allergens' in item:
        message += f"⚠️ **Please Note:**\n{item['allergens']}\n\n"
    
    message += f"🚀 **Ready in 15-20 minutes**\n"
    message += f"🔥 **Made fresh when you order**"
    
    keyboard = get_item_keyboard(item_id, category)
    
    await query.edit_message_text(
        message,
        reply_markup=keyboard,
        parse_mode='Markdown'
    )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors."""
    logger.error(f"Update {update} caused error {context.error}")
    
    # Only try to send error message if we have an update with a message
    if update and update.effective_message:
        error_message = (
            "😅 Oops! Something went wrong.\n\n"
            "Please try again or use /start to return to the main menu.\n\n"
            "If the problem persists, please contact our support team."
        )
        
        try:
            await update.effective_message.reply_text(error_message)
        except Exception as e:
            logger.error(f"Failed to send error message: {e}")
    else:
        # For webhook conflicts and other non-user errors, just log them
        logger.warning(f"System error (no user message): {context.error}")
