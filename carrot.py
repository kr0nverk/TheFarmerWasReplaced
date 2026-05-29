def plant_carrot():
	if can_harvest():
		harvest()	

	if get_ground_type() != Grounds.Soil:
		till()	
		
	plant(Entities.Carrot)				

def farm(size, min_carrot):
	change_hat(Hats.Brown_Hat)

	while num_items(Items.Carrot) < min_carrot: 
		
		for i in range(size):
			for j in range(size):
			
				plant_carrot()

				move(North)
			move(East)