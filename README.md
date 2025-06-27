# Professional Telegram Cafe Bot

A beautiful, visual Telegram bot for cafe menu browsing with professional food photography and modern interface design.

## Features

- 🖼️ **Professional Food Images**: High-quality photos from Unsplash for visual appeal
- 🎨 **Modern Interface**: Premium styling with visual boxes and professional formatting
- 📱 **Clean Navigation**: Intuitive button layouts without payment distractions
- ☕ **Complete Menu**: Coffee, cold drinks, breakfast, lunch, desserts, and snacks
- 🚀 **Railway Ready**: Configured for easy deployment on Railway platform

## Installation

1. **Get Bot Token**:
   - Create a bot via [@BotFather](https://t.me/botfather) on Telegram
   - Copy your bot token

2. **Set Environment Variables**:
   ```bash
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   PORT=8000
   ```

3. **Install Dependencies**:
   ```bash
   pip install python-telegram-bot==20.7
   ```

4. **Run the Bot**:
   ```bash
   python main.py
   ```

## File Structure

```
telegram-cafe-bot/
├── main.py           # Bot entry point and setup
├── handlers.py       # Command and button handlers
├── keyboards.py      # Button layout definitions
├── menu_data.py      # Menu items with images
├── Procfile          # Railway deployment config
├── .env.example      # Environment variables template
└── README.md         # This file
```

## Deployment on Railway

1. Upload these files to your Railway project
2. Set `TELEGRAM_BOT_TOKEN` in Railway environment variables
3. Railway will automatically use the Procfile to start the bot

## Customization

### Adding Menu Items
Edit `menu_data.py` to add new items:
```python
{
    "id": "new_item",
    "name": "New Item Name",
    "price": 5.95,
    "description": "Item description",
    "allergens": "Any allergens",
    "image": "https://your-image-url.com/image.jpg"
}
```

### Changing Bot Messages
Edit the welcome messages and text in `handlers.py` to match your cafe's branding.

### Adding New Categories
1. Add category to `MENU_CATEGORIES` in `menu_data.py`
2. Add items under the new category in `CAFE_MENU`

## Bot Commands

- `/start` - Show main menu
- `/help` - Display help information
- `/terms` - View terms and conditions
- `/support` - Get customer support info

## Technical Details

- **Framework**: python-telegram-bot v20.7
- **Architecture**: Handler-based event system
- **Images**: Professional food photography from Unsplash
- **Navigation**: Callback-based button interactions
- **Deployment**: Worker process on Railway platform

## Support

For technical support or customization requests, contact your development team.

---

Built with ❤️ for professional cafe presentation