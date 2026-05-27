def doing_something():
	if can_harvest():
		harvest()	

	if get_entity_type() != Entities.Bush:
		if get_ground_type() != Grounds.Soil:
			till()	
		
		x = get_pos_x()
		y = get_pos_y() 
		
		if (x%2==0 and y%2==0) or (x%2==1 and y%2==1):	
			plant(Entities.Tree)
		else:	
			plant(Entities.Bush)
		
		plant(Entities.Bush)				

def farm(size, min_wood):
	change_hat(Hats.Brown_Hat)

	x = get_pos_x()
	y = get_pos_y()
	
	doing_something()

	while num_items(Items.Wood) < min_wood: 
		
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