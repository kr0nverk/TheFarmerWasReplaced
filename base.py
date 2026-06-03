def change_soil_to_plant(entitie = Entities.Grass):
	ground = get_ground_type()	
	
	if entitie == Entities.Grass and ground != Grounds.Grassland:
		till()

	elif entitie == Entities.Tree and ground != Grounds.Soil:
		till()
	
	elif entitie == Entities.Carrot and ground != Grounds.Soil:
		till()

	elif entitie == Entities.Pumpkin and ground != Grounds.Soil:
		till()

	elif entitie == Entities.Sunflower and ground != Grounds.Soil:
		till()

	elif entitie == Entities.Cactus and ground != Grounds.Soil:
		till()

def till_and_plant(entitie = Entities.Grass):
	if can_harvest():
		harvest()	
	
	change_soil_to_plant(entitie)
			
	plant(entitie)
	
	if get_water() < 0.25 and num_items(Items.Water) > 1: 
		use_item(Items.Water)
		
	if entitie == Entities.Pumpkin and num_items(Items.Fertilizer) > 1:
		use_item(Items.Fertilizer)
		
def do_polyculture():
	if get_companion() != None:
		plant_type, (to_x, to_y) = get_companion()
		x, y = get_pos_x(), get_pos_y()
		
		move_to_pos(to_x, to_y)
		
		harvest()
		till_and_plant(plant_type)
		
		move_to_pos(x, y)

def move_to_pos(to_x, to_y):
	x, y = get_pos_x(), get_pos_y()
	
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