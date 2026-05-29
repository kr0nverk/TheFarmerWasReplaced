def plant_wood():
	if can_harvest():
		harvest()	

	if get_ground_type() != Grounds.Soil:
		till()	
		
	x = get_pos_x()
	y = get_pos_y() 
		
	if (x%2==0 and y%2==0) or (x%2==1 and y%2==1):	
		plant(Entities.Tree)
	else:	
		plant(Entities.Bush)			

def farm(size, min_wood):
	change_hat(Hats.Brown_Hat)

	while num_items(Items.Wood) < min_wood: 
		
		for i in range(size):
			for j in range(size):
			
				plant_wood()

				move(North)
			move(East)	