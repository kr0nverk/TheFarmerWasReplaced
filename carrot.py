def doing_something():
	if can_harvest():
		harvest()	

	if get_entity_type() != Entities.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()	
		
		plant(Entities.Carrot)				

def farm(size, min_carrot):
	change_hat(Hats.Brown_Hat)

	x = get_pos_x()
	y = get_pos_y()
	
	doing_something()

	while num_items(Items.Carrot) < min_carrot: 
		
		for row in range(size - y):
			if (row + y) % 2 == 0:
				dir = East
			else:
				dir = West
				
			for col in range(size-1):
				move(dir)
				doing_something()
		
			if (row + y) != size-1:
				move(North)
				doing_something()
		
		move(South)
		doing_something()
						
		for row in range(size-2-y):
			if (size-1 + row + y) % 2 == 0:
				dir = West
			else:
				dir = East
					
			for col in range(size-1):
				move(dir)
				doing_something()

			if (row - y) != size-2:
				move(South)	
				doing_something()	