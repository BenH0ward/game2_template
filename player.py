from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
global current_room
current_room = rooms["Reception"]
