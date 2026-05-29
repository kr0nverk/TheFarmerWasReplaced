def plant_pumpkin():
	if get_entity_type() != Entities.Pumpkin:
		harvest()
	
	if get_ground_type() != Grounds.Soil:
		till()
		
	plant(Entities.Pumpkin)

def check_pumpkin(dead_pumpkin_list):	
	if get_entity_type() == Entities.Dead_Pumpkin:
		dead_pumpkin_list.append((get_pos_x(), get_pos_y()))
		plant(Entities.Pumpkin)
	

def replant_dead_pumpkin(dead_pumpkins):
	dead_pumpkin_set = set(dead_pumpkins)

	while dead_pumpkin_set:
		for pumpkin in dead_pumpkins:
			if pumpkin not in dead_pumpkin_set:
				continue
			
			move_to_pos(pumpkin[0], pumpkin[1])
			
			if get_entity_type() != Entities.Pumpkin:
				use_item(Items.Water)
				plant(Entities.Pumpkin)
			elif can_harvest():
				dead_pumpkin_set.remove(pumpkin)	 
			else:
				use_item(Items.Water)
				
	harvest()
		
	
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
	
def second_plant(dead_pumpkins):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			check_pumpkin(dead_pumpkins)

			move(North)
		move(East)

def first_plant():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			
			plant_pumpkin()

			move(North)
		move(East)



def farm(size, min_pumpkin):
	#change_hat(Hats.Pumpkin_Hat)

	while num_items(Items.Pumpkin) < min_pumpkin: 
		first_plant()
		
		dead_pumpkins = []
		second_plant(dead_pumpkins)
		
		replant_dead_pumpkin(dead_pumpkins)	
	