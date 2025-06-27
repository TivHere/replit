"""Menu data for the Cozy Corner Cafe bot."""

MENU_CATEGORIES = {
    "coffee": {
        "name": "Coffee & Hot Drinks",
        "emoji": "☕",
        "description": "Freshly brewed coffee and warming beverages to start your day right."
    },
    "cold_drinks": {
        "name": "Cold Drinks & Smoothies",
        "emoji": "🧊",
        "description": "Refreshing cold beverages and healthy smoothies."
    },
    "breakfast": {
        "name": "Breakfast",
        "emoji": "🍳",
        "description": "Hearty breakfast options to fuel your morning."
    },
    "lunch": {
        "name": "Lunch & Mains",
        "emoji": "🍽️",
        "description": "Satisfying lunch dishes and main courses."
    },
    "desserts": {
        "name": "Desserts & Pastries",
        "emoji": "🧁",
        "description": "Sweet treats and freshly baked pastries."
    },
    "snacks": {
        "name": "Snacks & Light Bites",
        "emoji": "🥨",
        "description": "Perfect for a quick bite or sharing with friends."
    }
}

CAFE_MENU = {
    "coffee": [
        {
            "id": "espresso",
            "name": "Classic Espresso",
            "price": 2.95,
            "description": "Rich, bold espresso shot made from our signature dark roast blend. Perfect for coffee purists.",
            "allergens": "None",
            "image": "https://images.unsplash.com/photo-1510707577100-8c4a403d4934?w=400&h=300&fit=crop&crop=center"
        },
        {
            "id": "americano",
            "name": "Americano",
            "price": 3.45,
            "description": "Smooth espresso diluted with hot water for a lighter, longer coffee experience.",
            "allergens": "None",
            "image": "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=400&h=300&fit=crop&crop=center"
        },
        {
            "id": "cappuccino",
            "name": "Cappuccino",
            "price": 4.25,
            "description": "Perfect balance of espresso, steamed milk, and velvety foam. Dusted with cocoa powder.",
            "allergens": "Dairy",
            "image": "https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=400&h=300&fit=crop&crop=center"
        },
        {
            "id": "latte",
            "name": "Caffe Latte",
            "price": 4.75,
            "description": "Creamy espresso with steamed milk and a light layer of foam. Available with oat milk alternative.",
            "allergens": "Dairy (Oat milk available)",
            "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400&h=300&fit=crop&crop=center"
        },
        {
            "id": "mocha",
            "name": "Chocolate Mocha",
            "price": 5.25,
            "description": "Indulgent blend of espresso, rich chocolate, and steamed milk topped with whipped cream.",
            "allergens": "Dairy",
            "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop&crop=center"
        },
        {
            "id": "chai_latte",
            "name": "Chai Latte",
            "price": 4.95,
            "description": "Warming spiced tea blend with steamed milk, cinnamon, and a touch of honey.",
            "allergens": "Dairy",
            "image": "https://images.unsplash.com/photo-1571934811356-5cc061b6821f?w=400&h=300&fit=crop&crop=center"
        }
    ],
    "cold_drinks": [
        {
            "id": "iced_coffee",
            "name": "Iced Coffee",
            "price": 3.95,
            "description": "Refreshing cold brew coffee served over ice with optional milk and sweetener.",
            "allergens": "Optional Dairy"
        },
        {
            "id": "frappuccino",
            "name": "Caramel Frappuccino",
            "price": 5.75,
            "description": "Blended ice coffee with caramel syrup, topped with whipped cream and caramel drizzle.",
            "allergens": "Dairy"
        },
        {
            "id": "green_smoothie",
            "name": "Green Goddess Smoothie",
            "price": 6.25,
            "description": "Healthy blend of spinach, banana, mango, and coconut milk. Packed with vitamins.",
            "ingredients": "Spinach, banana, mango, coconut milk, chia seeds",
            "allergens": "None"
        },
        {
            "id": "berry_smoothie",
            "name": "Mixed Berry Smoothie",
            "price": 5.95,
            "description": "Antioxidant-rich smoothie with strawberries, blueberries, and Greek yogurt.",
            "ingredients": "Strawberries, blueberries, banana, Greek yogurt, honey",
            "allergens": "Dairy"
        },
        {
            "id": "lemonade",
            "name": "Fresh Lemonade",
            "price": 3.75,
            "description": "House-made lemonade with fresh lemons and mint. Perfectly tart and refreshing.",
            "allergens": "None"
        }
    ],
    "breakfast": [
        {
            "id": "avocado_toast",
            "name": "Avocado Toast Deluxe",
            "price": 8.95,
            "description": "Smashed avocado on sourdough toast with cherry tomatoes, feta cheese, and everything bagel seasoning.",
            "ingredients": "Sourdough bread, avocado, cherry tomatoes, feta cheese, red pepper flakes",
            "allergens": "Gluten, Dairy"
        },
        {
            "id": "breakfast_burrito",
            "name": "Southwest Breakfast Burrito",
            "price": 9.75,
            "description": "Scrambled eggs with black beans, cheese, salsa, and potatoes wrapped in a flour tortilla.",
            "ingredients": "Eggs, black beans, cheddar cheese, potatoes, salsa, flour tortilla",
            "allergens": "Eggs, Dairy, Gluten"
        },
        {
            "id": "pancakes",
            "name": "Fluffy Buttermilk Pancakes",
            "price": 7.95,
            "description": "Three golden pancakes served with maple syrup and fresh berries.",
            "ingredients": "Flour, buttermilk, eggs, fresh berries, maple syrup",
            "allergens": "Gluten, Dairy, Eggs"
        },
        {
            "id": "yogurt_bowl",
            "name": "Greek Yogurt Bowl",
            "price": 6.95,
            "description": "Creamy Greek yogurt topped with granola, fresh fruit, and honey drizzle.",
            "ingredients": "Greek yogurt, house-made granola, seasonal fruit, honey",
            "allergens": "Dairy, Nuts (in granola)"
        }
    ],
    "lunch": [
        {
            "id": "club_sandwich",
            "name": "Classic Club Sandwich",
            "price": 11.95,
            "description": "Triple-decker sandwich with turkey, bacon, lettuce, tomato, and mayo on toasted bread.",
            "ingredients": "Turkey, bacon, lettuce, tomato, mayo, sourdough bread",
            "allergens": "Gluten, Eggs (in mayo)"
        },
        {
            "id": "caesar_salad",
            "name": "Chicken Caesar Salad",
            "price": 12.45,
            "description": "Crisp romaine lettuce with grilled chicken, parmesan, croutons, and house Caesar dressing.",
            "ingredients": "Romaine lettuce, grilled chicken, parmesan cheese, croutons, Caesar dressing",
            "allergens": "Dairy, Gluten, Fish (anchovies in dressing)"
        },
        {
            "id": "quinoa_bowl",
            "name": "Mediterranean Quinoa Bowl",
            "price": 10.95,
            "description": "Nutritious quinoa bowl with roasted vegetables, feta cheese, and tahini dressing.",
            "ingredients": "Quinoa, roasted vegetables, feta cheese, chickpeas, tahini dressing",
            "allergens": "Dairy, Sesame"
        },
        {
            "id": "grilled_cheese",
            "name": "Gourmet Grilled Cheese",
            "price": 8.75,
            "description": "Artisan bread with three cheeses, caramelized onions, and tomato soup for dipping.",
            "ingredients": "Artisan bread, cheddar, swiss, brie, caramelized onions",
            "allergens": "Gluten, Dairy"
        }
    ],
    "desserts": [
        {
            "id": "chocolate_cake",
            "name": "Decadent Chocolate Cake",
            "price": 5.95,
            "description": "Rich, moist chocolate cake with dark chocolate ganache and fresh berries.",
            "allergens": "Gluten, Dairy, Eggs"
        },
        {
            "id": "cheesecake",
            "name": "New York Cheesecake",
            "price": 6.45,
            "description": "Creamy vanilla cheesecake with graham cracker crust and seasonal fruit compote.",
            "allergens": "Gluten, Dairy, Eggs"
        },
        {
            "id": "tiramisu",
            "name": "Classic Tiramisu",
            "price": 6.95,
            "description": "Italian dessert with coffee-soaked ladyfingers, mascarpone, and cocoa powder.",
            "allergens": "Gluten, Dairy, Eggs"
        },
        {
            "id": "fruit_tart",
            "name": "Seasonal Fruit Tart",
            "price": 5.75,
            "description": "Buttery pastry shell filled with vanilla custard and topped with fresh seasonal fruit.",
            "allergens": "Gluten, Dairy, Eggs"
        },
        {
            "id": "cookies",
            "name": "Artisan Cookies (3-pack)",
            "price": 4.25,
            "description": "Selection of house-made cookies: chocolate chip, oatmeal raisin, and double chocolate.",
            "allergens": "Gluten, Dairy, Eggs"
        }
    ],
    "snacks": [
        {
            "id": "hummus_plate",
            "name": "Mediterranean Hummus Plate",
            "price": 7.95,
            "description": "House-made hummus with fresh vegetables, olives, and pita bread.",
            "ingredients": "Hummus, vegetables, olives, pita bread",
            "allergens": "Gluten, Sesame"
        },
        {
            "id": "cheese_board",
            "name": "Artisan Cheese Board",
            "price": 12.95,
            "description": "Selection of local cheeses with crackers, nuts, and dried fruit.",
            "ingredients": "Assorted cheeses, crackers, nuts, dried fruit",
            "allergens": "Dairy, Gluten, Nuts"
        },
        {
            "id": "nachos",
            "name": "Loaded Nachos",
            "price": 9.75,
            "description": "Crispy tortilla chips with cheese, jalapeños, salsa, and sour cream.",
            "ingredients": "Tortilla chips, cheese, jalapeños, salsa, sour cream",
            "allergens": "Dairy"
        },
        {
            "id": "soup",
            "name": "Soup of the Day",
            "price": 5.95,
            "description": "Ask your server about today's fresh soup selection, served with artisan bread.",
            "allergens": "Varies (ask server)"
        }
    ]
}
