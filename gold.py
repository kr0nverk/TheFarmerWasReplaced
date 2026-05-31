directions = [North, East, South, West]


def take_treasure():
	if get_entity_type() == Entities.Treasure:
		harvest()
		return True
	return False

def move_one_step(current_direction):
	for i in range(4):
		index = (current_direction + i - 1) % len(directions)
		direction_to_try = directions[index]
		
		if move(direction_to_try):
			return index	


def farm(size, min_gold):
	
	clear()
	
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)
		
	
	while num_items(Items.Gold) < min_gold: 
		harvest()
		plant(Entities.Bush)
		#substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		substance = get_world_size()

		use_item(Items.Weird_Substance, substance)			
		
		current_direction = 0
		while not take_treasure():
			current_direction = move_one_step(current_direction)
			
		
		
		
farm(get_world_size(), 10000)		