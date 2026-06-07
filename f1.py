
max_drones = max_drones()


def plant_hay():
	if can_harvest():
		harvest()	

	if get_ground_type() != Grounds.Grassland:
		till()	

def drone_job(size):
	for i in range(size):
		for j in range(size):
		
			plant_hay()

			move(North)
		move(East)	
	
def harvest_column():
	for _ in range(get_world_size()):
		harvest()
		move(North)	
	
def farm_multiple(size, min_hay, max_drones):
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)	
	
	change_hat(Hats.Brown_Hat)	


	while True:
		if spawn_drone(harvest_column):
			move(East)

	while num_items(Items.Hay) < min_hay:
			
		for i in range(max_drones):
			if spawn_drone(drone_job(size)):
				for j in range(size / max_drones):
					move(East)
					
farm_multiple(get_world_size(), 100000000, max_drones)		
			
		