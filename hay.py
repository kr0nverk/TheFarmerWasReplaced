import base

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

def do_polyculture():
	if get_companion() != None:
		plant_type, (to_x, to_y) = get_companion()
		
		x, y = get_pos_x(), get_pos_y()
		
		base.move_to_pos(to_x, to_y)
		harvest()
		base.change_soil_to_plant(plant_type)
		plant(plant_type)
		
		base.move_to_pos(x, y)

def farm_multiple(size, max_drones, min_hay):	
	
	def drone_job():
		for i in range(size):
			if get_entity_type() == Entities.Grass and can_harvest():
				do_polyculture()
				harvest()
				
			plant(Entities.Grass)
			move(North)

	base.move_to_pos(0, 0)

	while num_items(Items.Hay) < min_hay: 
		n = 0
		while n < size:
			if num_drones() < max_drones:
				spawn_drone(drone_job)
				move(East)
				n += 1			