def plant_hay():
	if can_harvest():
		harvest()	

	if get_ground_type() != Grounds.Grassland:
		till()	
			
def farm(size, min_hay):
	change_hat(Hats.Green_Hat)

	while num_items(Items.Hay) < min_hay: 
		
		for i in range(size):
			for j in range(size):
			
				plant_hay()

				move(North)
			move(East)	