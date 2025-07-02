"""
Enhanced Order management for the Telegram Cafe Bot
Handles order creation, storage, and status tracking
"""

import json
import logging
import os
import uuid
from datetime import datetime
from enhanced_config import ORDERS_FILE, ORDER_STATUS

logger = logging.getLogger(__name__)

class OrderManager:
    """Manages customer orders"""
    
    def __init__(self):
        self._initialize_orders_file()
    
    def _initialize_orders_file(self):
        """Initialize orders file if it doesn't exist"""
        try:
            if not os.path.exists(ORDERS_FILE):
                with open(ORDERS_FILE, 'w', encoding='utf-8') as f:
                    json.dump({}, f)
                logger.info("Orders file initialized")
        except Exception as e:
            logger.error(f"Error initializing orders file: {e}")
    
    def _load_orders(self):
        """Load orders from file"""
        try:
            with open(ORDERS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error("Orders file not found")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing orders JSON: {e}")
            return {}
        except Exception as e:
            logger.error(f"Error loading orders: {e}")
            return {}
    
    def _save_orders(self, orders):
        """Save orders to file"""
        try:
            with open(ORDERS_FILE, 'w', encoding='utf-8') as f:
                json.dump(orders, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving orders: {e}")
    
    def create_order(self, order_data):
        """Create a new order"""
        try:
            orders = self._load_orders()
            
            # Generate unique order ID
            order_id = str(uuid.uuid4())[:8].upper()
            
            # Ensure unique ID
            while order_id in orders:
                order_id = str(uuid.uuid4())[:8].upper()
            
            # Create order record
            order = {
                'id': order_id,
                'user_id': order_data.get('user_id'),
                'username': order_data.get('username'),
                'first_name': order_data.get('first_name'),
                'last_name': order_data.get('last_name'),
                'phone_number': order_data.get('phone_number'),
                'contact_info': order_data.get('contact_info'),
                'items': order_data.get('items', {}),
                'status': ORDER_STATUS['PENDING'],
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat(),
                'notes': order_data.get('notes', ''),
                'total_amount': order_data.get('total_amount', 0)
            }
            
            # Save order
            orders[order_id] = order
            self._save_orders(orders)
            
            logger.info(f"Created order {order_id} for user {order_data.get('user_id')}")
            return order_id
            
        except Exception as e:
            logger.error(f"Error creating order: {e}")
            return None
    
    def get_order(self, order_id):
        """Get order by ID"""
        try:
            orders = self._load_orders()
            return orders.get(order_id)
        except Exception as e:
            logger.error(f"Error getting order {order_id}: {e}")
            return None
    
    def update_order_status(self, order_id, status):
        """Update order status"""
        try:
            if status not in ORDER_STATUS.values():
                logger.error(f"Invalid order status: {status}")
                return False
            
            orders = self._load_orders()
            
            if order_id in orders:
                orders[order_id]['status'] = status
                orders[order_id]['updated_at'] = datetime.now().isoformat()
                self._save_orders(orders)
                
                logger.info(f"Updated order {order_id} status to {status}")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Error updating order status: {e}")
            return False