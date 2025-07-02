"""
Enhanced Message and callback handlers for the Telegram Cafe Bot with Add-to-Cart System
"""

import logging
import random
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from enhanced_config import (
    WELCOME_MESSAGE, HELP_MESSAGE, CAFE_PHONE, CAFE_EMAIL, 
    CAFE_ADDRESS, CAFE_HOURS, CAFE_WEBSITE, CAFE_INSTAGRAM,
    ORDER_PHONE, ORDER_EMAIL, CAFE_NAME, ADMIN_CHAT_ID, CURRENCY
)
from enhanced_cart_manager import CartManager
from enhanced_order_manager import OrderManager

logger = logging.getLogger(__name__)

# Initialize managers
cart_manager = CartManager()
order_manager = OrderManager()
user_states = {}  # Track user conversation states

def load_menu_data():
    """Load menu data from JSON file"""
    try:
        with open('attached_assets/menu_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading menu data: {e}")
        return {}

def get_item_by_id(item_id):
    """Get menu item by ID"""
    try:
        menu_data = load_menu_data()
        for category, items in menu_data.items():
            if isinstance(items, list):
                for item in items:
                    if item.get('id') == item_id:
                        return item
    except Exception as e:
        logger.error(f"Error getting item {item_id}: {e}")
    return None

def create_main_menu_keyboard():
    """Create main menu keyboard with cart indicator"""
    keyboard = [
        [InlineKeyboardButton("☕ Beverages", callback_data="category_beverages")],
        [InlineKeyboardButton("🍽️ Food", callback_data="category_food")],
        [InlineKeyboardButton("🥧 Desserts", callback_data="category_desserts")],
        [InlineKeyboardButton("🛒 My Cart", callback_data="show_cart")],
        [InlineKeyboardButton("📞 Contact", callback_data="contact"),
         InlineKeyboardButton("📍 Location", callback_data="location")]
    ]
    return InlineKeyboardMarkup(keyboard)

def create_category_keyboard(category):
    """Create keyboard for menu category with items"""
    try:
        menu_data = load_menu_data()
        items = menu_data.get(category, [])
        
        keyboard = []
        for item in items:
            if isinstance(item, dict):
                keyboard.append([InlineKeyboardButton(
                    f"{item.get('name', 'Item')} - {item.get('price', '$0.00')}", 
                    callback_data=f"item_{item.get('id', '')}"
                )])
        
        keyboard.append([InlineKeyboardButton("🛒 View Cart", callback_data="show_cart")])
        keyboard.append([InlineKeyboardButton("◀️ Back to Menu", callback_data="main_menu")])
        
        return InlineKeyboardMarkup(keyboard)
    except Exception as e:
        logger.error(f"Error creating category keyboard: {e}")
        return InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Back", callback_data="main_menu")]])

def create_item_keyboard(item_id):
    """Create keyboard for individual menu item"""
    keyboard = [
        [InlineKeyboardButton("🛒 Add to Cart", callback_data=f"add_item_{item_id}")],
        [InlineKeyboardButton("◀️ Back to Category", callback_data="back_to_category"),
         InlineKeyboardButton("🛒 View Cart", callback_data="show_cart")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command with welcome message"""
    try:
        await update.message.reply_text(
            WELCOME_MESSAGE,
            reply_markup=create_main_menu_keyboard(),
            parse_mode=ParseMode.MARKDOWN
        )
    except Exception as e:
        logger.error(f"Error in start_command: {e}")
        await update.message.reply_text(
            f"Welcome to {CAFE_NAME}! 🎉",
            reply_markup=create_main_menu_keyboard()
        )

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /menu command"""
    try:
        message = """
🍽️ **Our Menu** 🍽️

Explore our delicious offerings by category:
• Fresh coffee and specialty drinks
• Hearty meals and light bites  
• Sweet desserts and pastries

Choose a category to see our full selection and add items to your cart!
"""
        
        await update.message.reply_text(
            message,
            reply_markup=create_main_menu_keyboard(),
            parse_mode=ParseMode.MARKDOWN
        )
    except Exception as e:
        logger.error(f"Error in menu_command: {e}")
        await update.message.reply_text(
            "Here's our menu! 🍽️",
            reply_markup=create_main_menu_keyboard()
        )

async def cart_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /cart command"""
    try:
        user_id = update.effective_user.id
        await show_cart_internal(update, context, user_id, is_message=True)
    except Exception as e:
        logger.error(f"Error in cart_command: {e}")
        await update.message.reply_text(
            "🛒 Your cart is empty!",
            reply_markup=create_main_menu_keyboard()
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /help command"""
    try:
        keyboard = [[InlineKeyboardButton("◀️ Back to Menu", callback_data="main_menu")]]
        await update.message.reply_text(
            HELP_MESSAGE,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
    except Exception as e:
        logger.error(f"Error in help_command: {e}")
        await update.message.reply_text("Here's how to use this bot! 🤖")

async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /contact command"""
    try:
        contact_message = f"""
📞 **Contact {CAFE_NAME}** 📞

**Phone:** {CAFE_PHONE}
**Email:** {CAFE_EMAIL}
**Website:** {CAFE_WEBSITE}
**Instagram:** {CAFE_INSTAGRAM}

**Address:**
{CAFE_ADDRESS}

We'd love to hear from you! 💌
"""
        keyboard = [[InlineKeyboardButton("◀️ Back to Menu", callback_data="main_menu")]]
        
        await update.message.reply_text(
            contact_message,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
    except Exception as e:
        logger.error(f"Error in contact_command: {e}")
        await update.message.reply_text(f"📞 Contact us at {CAFE_PHONE}")

async def location_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /location command"""
    try:
        location_message = f"""
📍 **Find {CAFE_NAME}** 📍

**Address:**
{CAFE_ADDRESS}

{CAFE_HOURS}

See you soon! ✨
"""
        keyboard = [[InlineKeyboardButton("◀️ Back to Menu", callback_data="main_menu")]]
        
        await update.message.reply_text(
            location_message,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
    except Exception as e:
        logger.error(f"Error in location_command: {e}")
        await update.message.reply_text(f"📍 Visit us at {CAFE_ADDRESS}")

async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle all callback queries from inline keyboards"""
    try:
        query = update.callback_query
        await query.answer()
        
        callback_data = query.data
        user_id = update.effective_user.id
        
        if callback_data == "main_menu":
            await handle_main_menu(query)
        elif callback_data.startswith("category_"):
            category = callback_data.replace("category_", "")
            await handle_category_selection(query, category)
        elif callback_data.startswith("item_"):
            item_id = callback_data.replace("item_", "")
            await handle_item_selection(query, item_id)
        elif callback_data.startswith("add_item_"):
            item_id = callback_data.replace("add_item_", "")
            await handle_add_to_cart(query, context, item_id)
        elif callback_data.startswith("increase_"):
            item_id = callback_data.replace("increase_", "")
            await handle_quantity_change(query, context, item_id, "increase")
        elif callback_data.startswith("decrease_"):
            item_id = callback_data.replace("decrease_", "")
            await handle_quantity_change(query, context, item_id, "decrease")
        elif callback_data == "show_cart":
            await handle_show_cart(query, context)
        elif callback_data == "place_order":
            await handle_place_order(query, context)
        elif callback_data == "clear_cart":
            await handle_clear_cart(query, context)
        elif callback_data == "back_to_category":
            await handle_main_menu(query)
        elif callback_data == "contact":
            await handle_contact_info(query)
        elif callback_data == "location":
            await handle_location_info(query)
            
    except Exception as e:
        logger.error(f"Error in handle_callback_query: {e}")
        try:
            await query.message.reply_text("Something went wrong! Use /start to restart.")
        except:
            pass

async def handle_main_menu(query) -> None:
    """Handle main menu callback"""
    try:
        main_menu_text = """
🍽️ **Welcome to Our Menu!** 🍽️

Choose a category below to explore our delicious offerings:

✨ Fresh ingredients, made with love
💫 Perfect for dine-in, takeout, or delivery
🛒 Add items to your cart and order directly!
"""
        
        await query.edit_message_text(
            main_menu_text,
            reply_markup=create_main_menu_keyboard(),
            parse_mode=ParseMode.MARKDOWN
        )
    except Exception as e:
        logger.error(f"Error in handle_main_menu: {e}")

async def handle_category_selection(query, category: str) -> None:
    """Handle category selection"""
    try:
        category_message = f"🍽️ **{category.title()} Menu**\n\nChoose an item to view details:"
        
        await query.edit_message_text(
            category_message,
            reply_markup=create_category_keyboard(category),
            parse_mode=ParseMode.MARKDOWN
        )
    except Exception as e:
        logger.error(f"Error in handle_category_selection: {e}")

async def handle_item_selection(query, item_id: str) -> None:
    """Handle menu item selection"""
    try:
        item = get_item_by_id(item_id)
        
        if not item:
            await query.edit_message_text(
                "Sorry, this item is not available.",
                reply_markup=create_main_menu_keyboard()
            )
            return
        
        item_message = f"""
**{item.get('name', 'Menu Item')}**

💰 **Price:** {item.get('price', '$0.00')}
📝 **Description:** {item.get('description', 'Delicious menu item')}

Ready to add this to your cart?
"""
        
        await query.edit_message_text(
            item_message,
            reply_markup=create_item_keyboard(item_id),
            parse_mode=ParseMode.MARKDOWN
        )
    except Exception as e:
        logger.error(f"Error in handle_item_selection: {e}")

async def handle_add_to_cart(query, context, item_id: str) -> None:
    """Handle adding item to cart"""
    try:
        user_id = query.from_user.id
        item = get_item_by_id(item_id)
        
        if not item:
            await query.answer("Item not found!")
            return
        
        success = cart_manager.add_item(user_id, item_id, 1)
        
        if success:
            await query.answer(f"✅ {item['name']} added to cart!")
            
            # Show quantity controls
            keyboard = [
                [
                    InlineKeyboardButton("➖", callback_data=f"decrease_{item_id}"),
                    InlineKeyboardButton("1", callback_data=f"quantity_{item_id}"),
                    InlineKeyboardButton("➕", callback_data=f"increase_{item_id}")
                ],
                [InlineKeyboardButton("🛒 View Cart", callback_data="show_cart")],
                [InlineKeyboardButton("◀️ Continue Shopping", callback_data="main_menu")]
            ]
            
            text = f"**{item['name']}** added to cart!\n\n"
            text += f"💰 Price: {item['price']}\n"
            text += f"📝 {item.get('description', '')}\n\n"
            text += "Adjust quantity or continue shopping:"
            
            await query.edit_message_text(
                text,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await query.answer("Failed to add item to cart!")
            
    except Exception as e:
        logger.error(f"Error adding item to cart: {e}")
        await query.answer("Error adding item to cart")

async def handle_quantity_change(query, context, item_id: str, action: str) -> None:
    """Handle quantity increase/decrease"""
    try:
        user_id = query.from_user.id
        current_qty = cart_manager.get_item_quantity(user_id, item_id)
        
        if action == "increase":
            new_qty = current_qty + 1
        elif action == "decrease":
            new_qty = max(0, current_qty - 1)
        else:
            return
        
        if new_qty == 0:
            cart_manager.remove_item(user_id, item_id)
            await query.answer("Item removed from cart!")
            await handle_show_cart(query, context)
        else:
            cart_manager.update_quantity(user_id, item_id, new_qty)
            await query.answer(f"Quantity updated to {new_qty}")
            
            item = get_item_by_id(item_id)
            keyboard = [
                [
                    InlineKeyboardButton("➖", callback_data=f"decrease_{item_id}"),
                    InlineKeyboardButton(str(new_qty), callback_data=f"quantity_{item_id}"),
                    InlineKeyboardButton("➕", callback_data=f"increase_{item_id}")
                ],
                [InlineKeyboardButton("🛒 View Cart", callback_data="show_cart")],
                [InlineKeyboardButton("◀️ Continue Shopping", callback_data="main_menu")]
            ]
            
            price = float(item.get('price', '$0.00').replace('$', ''))
            item_total = price * new_qty
            
            text = f"**{item['name']}** - Quantity: {new_qty}\n\n"
            text += f"💰 Price: {item['price']} each\n"
            text += f"💰 Total: ${item_total:.2f}\n\n"
            text += "Adjust quantity or continue shopping:"
            
            await query.edit_message_text(
                text,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode=ParseMode.MARKDOWN
            )
            
    except Exception as e:
        logger.error(f"Error updating quantity: {e}")
        await query.answer("Error updating quantity")

async def handle_show_cart(query, context) -> None:
    """Handle show cart callback"""
    try:
        user_id = query.from_user.id
        await show_cart_internal(query, context, user_id, is_message=False)
    except Exception as e:
        logger.error(f"Error showing cart: {e}")

async def show_cart_internal(update_or_query, context, user_id, is_message=False) -> None:
    """Internal function to show cart contents"""
    try:
        cart = cart_manager.get_cart(user_id)
        
        if not cart or not cart.get('items'):
            text = "🛒 Your cart is empty!\n\nBrowse our menu to add some delicious items."
            keyboard = [[InlineKeyboardButton("🍴 View Menu", callback_data="main_menu")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            if is_message:
                await update_or_query.message.reply_text(text, reply_markup=reply_markup)
            else:
                await update_or_query.edit_message_text(text, reply_markup=reply_markup)
            return
        
        text = "🛒 **Your Cart**\n\n"
        total = 0
        keyboard = []
        
        for item_id, quantity in cart['items'].items():
            item = get_item_by_id(item_id)
            if item:
                price = float(item.get('price', '$0.00').replace('$', ''))
                item_total = price * quantity
                total += item_total
                
                text += f"**{item['name']}**\n"
                text += f"💰 {item['price']} × {quantity} = ${item_total:.2f}\n\n"
                
                keyboard.append([
                    InlineKeyboardButton("➖", callback_data=f"decrease_{item_id}"),
                    InlineKeyboardButton(f"{item['name']} ({quantity})", callback_data=f"item_{item_id}"),
                    InlineKeyboardButton("➕", callback_data=f"increase_{item_id}")
                ])
        
        text += f"💰 **Total: ${total:.2f}**\n\n"
        
        if total > 0:
            keyboard.append([InlineKeyboardButton("📋 Place Order", callback_data="place_order")])
        
        keyboard.append([InlineKeyboardButton("🍴 Continue Shopping", callback_data="main_menu")])
        keyboard.append([InlineKeyboardButton("🗑️ Clear Cart", callback_data="clear_cart")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        if is_message:
            await update_or_query.message.reply_text(
                text,
                reply_markup=reply_markup,
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await update_or_query.edit_message_text(
                text,
                reply_markup=reply_markup,
                parse_mode=ParseMode.MARKDOWN
            )
            
    except Exception as e:
        logger.error(f"Error showing cart: {e}")

async def handle_place_order(query, context) -> None:
    """Handle place order process"""
    try:
        user_id = query.from_user.id
        cart = cart_manager.get_cart(user_id)
        
        if not cart or not cart.get('items'):
            await query.answer("Your cart is empty!")
            return
        
        # Set user state to collecting contact info
        user_states[user_id] = 'awaiting_contact'
        
        text = "📞 **Contact Information Required**\n\n"
        text += "To place your order, we need your contact information.\n\n"
        text += "Please share your phone number using the button below, or type your contact details:"
        
        # Create contact request keyboard
        contact_keyboard = ReplyKeyboardMarkup([
            [KeyboardButton("📞 Share Phone Number", request_contact=True)]
        ], resize_keyboard=True, one_time_keyboard=True)
        
        await query.edit_message_text(text, parse_mode=ParseMode.MARKDOWN)
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="👆 Use the button below or type your contact info:",
            reply_markup=contact_keyboard
        )
        
    except Exception as e:
        logger.error(f"Error placing order: {e}")
        await query.answer("Error placing order")

async def handle_clear_cart(query, context) -> None:
    """Handle clear cart"""
    try:
        user_id = query.from_user.id
        cart_manager.clear_cart(user_id)
        await query.answer("Cart cleared!")
        await handle_main_menu(query)
    except Exception as e:
        logger.error(f"Error clearing cart: {e}")
        await query.answer("Error clearing cart")

async def handle_contact_info(query) -> None:
    """Handle contact information display"""
    try:
        contact_message = f"""
📞 **Contact {CAFE_NAME}** 📞

**Phone:** {CAFE_PHONE}
**Email:** {CAFE_EMAIL}
**Website:** {CAFE_WEBSITE}
**Instagram:** {CAFE_INSTAGRAM}

**Address:**
{CAFE_ADDRESS}

We'd love to hear from you! 💌
"""
        
        keyboard = [[InlineKeyboardButton("◀️ Back to Menu", callback_data="main_menu")]]
        
        await query.edit_message_text(
            contact_message,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
        
    except Exception as e:
        logger.error(f"Error in handle_contact_info: {e}")

async def handle_location_info(query) -> None:
    """Handle location information"""
    try:
        location_message = f"""
📍 **Find {CAFE_NAME}** 📍

**Address:**
{CAFE_ADDRESS}

{CAFE_HOURS}

See you soon! ✨
"""
        
        keyboard = [[InlineKeyboardButton("◀️ Back to Menu", callback_data="main_menu")]]
        
        await query.edit_message_text(
            location_message,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
        
    except Exception as e:
        logger.error(f"Error in handle_location_info: {e}")

async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle contact information shared by user"""
    try:
        user_id = update.effective_user.id
        
        if user_states.get(user_id) != 'awaiting_contact':
            return
        
        contact = update.message.contact
        phone_number = contact.phone_number
        
        await finalize_order(update, context, phone_number=phone_number)
        
    except Exception as e:
        logger.error(f"Error handling contact: {e}")
        await update.message.reply_text("Error processing your contact information.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle text messages from users"""
    try:
        user_id = update.effective_user.id
        
        if user_states.get(user_id) == 'awaiting_contact':
            contact_info = update.message.text
            await finalize_order(update, context, contact_info=contact_info)
        else:
            await update.message.reply_text(
                "I'm here to help you order food! Use /menu to browse our items or /help for commands."
            )
            
    except Exception as e:
        logger.error(f"Error handling message: {e}")

async def finalize_order(update: Update, context: ContextTypes.DEFAULT_TYPE, phone_number=None, contact_info=None) -> None:
    """Finalize and submit the order"""
    try:
        user_id = update.effective_user.id
        user = update.effective_user
        cart = cart_manager.get_cart(user_id)
        
        if not cart or not cart.get('items'):
            await update.message.reply_text("Your cart is empty!")
            return
        
        # Calculate total
        total = 0
        for item_id, quantity in cart['items'].items():
            item = get_item_by_id(item_id)
            if item:
                price = float(item.get('price', '$0.00').replace('$', ''))
                total += price * quantity
        
        # Create order data
        order_data = {
            'user_id': user_id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': phone_number,
            'contact_info': contact_info,
            'items': cart['items'].copy(),
            'total_amount': total
        }
        
        # Create the order
        order_id = order_manager.create_order(order_data)
        
        if order_id:
            # Clear user's cart
            cart_manager.clear_cart(user_id)
            
            # Reset user state
            user_states.pop(user_id, None)
            
            # Send confirmation to customer
            confirmation_text = f"✅ **Order Placed Successfully!**\n\n"
            confirmation_text += f"📋 Your Order ID: #{order_id}\n\n"
            confirmation_text += "Your order has been sent to our kitchen. "
            confirmation_text += "We'll contact you shortly to confirm details.\n\n"
            confirmation_text += "Thank you for your order! 🍽️"
            
            await update.message.reply_text(
                confirmation_text,
                parse_mode=ParseMode.MARKDOWN
            )
            
            # Send order to admin chat
            await send_order_to_admin(context, order_id)
            
        else:
            await update.message.reply_text(
                "Sorry, there was an error processing your order. Please try again."
            )
            
    except Exception as e:
        logger.error(f"Error finalizing order: {e}")
        await update.message.reply_text(
            "Sorry, there was an error placing your order. Please try again later."
        )

async def send_order_to_admin(context: ContextTypes.DEFAULT_TYPE, order_id: str) -> None:
    """Send order notification to admin chat"""
    try:
        order = order_manager.get_order(order_id)
        if not order:
            logger.error(f"Order {order_id} not found")
            return
        
        # Format order message for admin
        admin_message = "🔔 **NEW ORDER RECEIVED**\n\n"
        admin_message += f"📋 Order ID: #{order['id']}\n"
        admin_message += f"👤 Customer: {order['first_name']} {order.get('last_name', '')}\n"
        admin_message += f"📱 Phone: {order.get('phone_number', order.get('contact_info', 'Not provided'))}\n"
        admin_message += f"📅 Time: {order['created_at'][:19].replace('T', ' ')}\n\n"
        
        admin_message += "**ITEMS ORDERED:**\n"
        total = 0
        
        for item_id, quantity in order['items'].items():
            item = get_item_by_id(item_id)
            if item:
                price = float(item.get('price', '$0.00').replace('$', ''))
                item_total = price * quantity
                total += item_total
                admin_message += f"• {item['name']} × {quantity} = ${item_total:.2f}\n"
        
        admin_message += f"\n💰 **TOTAL: ${total:.2f}**\n"
        admin_message += f"📊 Status: {order['status']}"
        
        # Send to admin chat
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=admin_message,
            parse_mode=ParseMode.MARKDOWN
        )
        
        logger.info(f"Order {order_id} sent to admin chat")
        
    except Exception as e:
        logger.error(f"Error sending order to admin: {e}")