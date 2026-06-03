import base

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
		
def farm_multiple(size, max_drones, min_cactus):	
	
	def drone_job_plant(size):
		for i in range(size):
			if get_entity_type() != Entities.Cactus:
				harvest()				
				base.till_and_plant(Entities.Cactus)
			move(North)

	def drone_job_sort_x(size):
		while get_pos_x() != size - 1:
			x = get_pos_x()
			a = measure() 
			b = measure(East)
			if a > b:
				swap(East)
				if x != 0:
					move(West)
			else:
				move(East)

	def drone_job_sort_y(size):
		while get_pos_y() != size - 1:
			y = get_pos_y()
			a = measure()
			b = measure(North)
			if a > b:
				swap(North)
				if y != 0:
					move(South)
			else:
				move(North)

	while num_items(Items.Cactus) < min_cactus: 
		id_drones = set()
		for i in range(3):
			n = 0
			while n < size:
				if num_drones() < max_drones:
					n += 1
					if i == 0:
						id_drones.add(spawn_drone(drone_job_plant, size))
						move(East)
					elif i == 1:
						id_drones.add(spawn_drone(drone_job_sort_y, size))
						move(East)
					else:
						id_drones.add(spawn_drone(drone_job_sort_x, size))
						move(North)
				else:
					if i == 1:
						drone_job_sort_y(size)
					elif i == 2:
						drone_job_sort_x(size)
						
			for id in list(id_drones):
				base.move_to_pos(0, 0)
				wait_for(id)
				id_drones.remove(id)
		harvest()								