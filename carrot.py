import base

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

def farm_multiple(size, max_drones, min_carrot):	
	
	def drone_job():
		for i in range(size):
			if get_entity_type() == Entities.Carrot and can_harvest():
				base.do_polyculture()
				harvest()
				
			base.till_and_plant(Entities.Carrot)
			move(North)

	base.move_to_pos(0, 0)

	while num_items(Items.Carrot) < min_carrot: 
		n = 0
		while n < size:
			if num_drones() < max_drones:
				spawn_drone(drone_job)
				move(East)
				n += 1					