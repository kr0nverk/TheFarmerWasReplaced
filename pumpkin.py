import base

nChk = 0
preID = 0

def plant_pumpkin():
	if get_entity_type() != Entities.Pumpkin:
		harvest()
	
	if get_ground_type() != Grounds.Soil:
		till()
		
	plant(Entities.Pumpkin)
	if num_items(Items.Fertilizer) > 1:
		use_item(Items.Fertilizer)
	
def check_pumpkin(dead_pumpkin_list):	
	if get_entity_type() == Entities.Dead_Pumpkin:
		dead_pumpkin_list.append((get_pos_x(), get_pos_y()))
		plant(Entities.Pumpkin)
	

def replant_dead_pumpkin(dead_pumpkins):
	max_measure = get_world_size() * get_world_size() * get_world_size()

	dead_pumpkin_set = set(dead_pumpkins)

	while dead_pumpkin_set:
		for pumpkin in dead_pumpkins:
			if pumpkin not in dead_pumpkin_set:
				continue
			
			base.move_to_pos(pumpkin[0], pumpkin[1])
			
			if get_entity_type() != Entities.Pumpkin:
				use_item(Items.Water)
				plant(Entities.Pumpkin)
			elif can_harvest():
				dead_pumpkin_set.remove(pumpkin)
			else:
				use_item(Items.Water)
				if num_items(Items.Fertilizer) > 1:
					use_item(Items.Fertilizer)
				
	harvest()
	
def second_plant(dead_pumpkins):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			check_pumpkin(dead_pumpkins)

			move(North)
		move(East)

def first_plant():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			
			plant_pumpkin()

			move(North)
		move(East)

def farm(size, min_pumpkin):
	#change_hat(Hats.Pumpkin_Hat)

	while num_items(Items.Pumpkin) < min_pumpkin: 
		first_plant()
		
		dead_pumpkins = []
		second_plant(dead_pumpkins)
		
		replant_dead_pumpkin(dead_pumpkins)	
		

def farm_multiple(size, max_drones, min_pumpkin):	
	
	def drone_job():
		for i in range(size):
			if get_entity_type() != Entities.Pumpkin:
				harvest()				
				base.till_and_plant(Entities.Pumpkin)
			move(North)

	while num_items(Items.Pumpkin) < min_pumpkin: 
		global nChk
		global preID
		n = 0
		while n < size:
			if num_drones() < max_drones:
				spawn_drone(drone_job)
				if preID == measure():
					nChk += 1
				else:
					nChk = 0
					preID = measure()
				if nChk > size / 2:
					nChk = 0
					harvest()
				move(East)
				n += 1		
		