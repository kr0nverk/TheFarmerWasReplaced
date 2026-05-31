def move_to_pos(to_x, to_y):
	x = get_pos_x()
	
	first_x = abs(x - to_x)
	second_x = get_world_size() - first_x
	
	if x < to_x:
		if first_x < second_x:
			dir = East
			num = first_x
		else:
			dir = West
			num = second_x
	else:
		if first_x < second_x:
			dir = West
			num = first_x
		else:
			dir = East
			num = second_x
	
	for i in range(num):
		move(dir)
	
	y = get_pos_y()
	
	first_y = abs(y - to_y)
	second_y = get_world_size() - first_y
	
	if y < to_y:
		if first_y < second_y:
			dir = North
			num = first_y
		else:
			dir = South
			num = second_y
	else:
		if first_x < second_x:
			dir = South
			num = first_y
		else:
			dir = North
			num = second_y
	
	for i in range(num):
		move(dir)

def plant_sunflower(size):
	
	petals = {}
	
	for i in range(size):
		for j in range(size):
			
			if get_entity_type() != Entities.Sunflower:
				if can_harvest():
					harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Sunflower)
				if num_items(Items.Fertilizer) > 1:
					use_item(Items.Fertilizer)
				
			
			petal = measure()
			
			if petal:				
				if petal not in petals:
					petals[petal] = []
				
				x, y = get_pos_x(), get_pos_y()
				petals[petal].append((x, y))
				
			move(North)
		move(East)
	
	min_petal = 7
	max_petal = 15
	harvest_counter = size * size
	
	for i in range(max_petal, min_petal - 1, -1):
		targets = petals[i]
		
		for target in targets:

			if harvest_counter < 10:
				return

			move_to_pos(target[0], target[1])
			
			while not can_harvest() and num_items(Items.Fertilizer) > 1:
				use_item(Items.Fertilizer)
			harvest()
			harvest_counter -= 1	
			
			

def farm(size, min_power):
	#change_hat(Hats.Pumpkin_Hat)
	
	while num_items(Items.Power) < min_power: 
		plant_sunflower(size)