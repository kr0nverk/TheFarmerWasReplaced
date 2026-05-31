def plant_cactus(size):
	for row in range(size):
		for col in range(size):
			
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Cactus:			
				plant(Entities.Cactus)
					
			move(East)
		move(North)		

def sort_row(size):
	for i in range(size-1):
		for j in range(size-i-1):
			if measure() > measure(East):
				swap(East)
			move(East)
		while get_pos_x() > 0:
			move(West)

def sort_col(size):
	for i in range(size-1):	
		for j in range(size-i-1):
			if measure() > measure(North):
				swap(North)
			move(North)
		while get_pos_y() > 0:
			move(South)		

def farm(size, min_cactus):
	
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)
		
	
	while num_items(Items.Cactus) < min_cactus: 
	
		plant_cactus(size)		

		for row in range(size):
			sort_row(size)
			move(North)
	
		for col in range(size):
			sort_col(size)
			move(East)
		
		harvest()								