def plant_sunflower(size):
	for i in range(size):
		for j in range(size):
			
			if get_entity_type() != Entities.Sunflower:
				if can_harvest():
					harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Sunflower)
			
			x, y = get_pos_x(), get_pos_y()
			measures_dict = {(x,y):measure()}		
							
			move(North)
		move(East)

	for i in range(15,7,-1):	
		for row in range(size):
			for col in range(size):
				
				if measure() == i:
					harvest()
							 
				move(North)
			move(East)

def farm(size, min_power):
	#change_hat(Hats.Pumpkin_Hat)
	
	while num_items(Items.Power) < min_power: 
		plant_sunflower(size)