import hay
import wood
import carrot
import pumpkin
import power
import cactus

min_hay = 10000
min_wood = 10000
min_carrot = 10000
min_pumpkin = 10000
min_cactus = 10000

min_power = 10000

size = get_world_size()

while get_pos_x() > 0:
	move(West)
while get_pos_y() > 0:
	move(South)

while True:

	if num_items(Items.Power) < min_power:		
		power.farm(size, min_power)	

	elif num_items(Items.Hay) < min_hay:
		if num_items(Items.Wood) > get_cost(Unlocks.Grass)[Items.Wood]:
			unlock(Unlocks.Grass)		
		
		hay.farm(size, min_wood)
		
	elif num_items(Items.Wood) < min_wood:
		if num_items(Items.Hay) > get_cost(Unlocks.Trees)[Items.Hay]:
			unlock(Unlocks.Trees)			
		
		wood.farm(size, min_wood)
	
	elif num_items(Items.Carrot) < min_carrot:
		if num_items(Items.Wood) > get_cost(Unlocks.Carrots)[Items.Wood]:
			unlock(Unlocks.Carrots)			
		
		carrot.farm(size, min_carrot)		

	elif num_items(Items.Pumpkin) < min_pumpkin:
		if num_items(Items.Carrot) > get_cost(Unlocks.Pumpkins)[Items.Carrot]:
			unlock(Unlocks.Pumpkins)				
		
		pumpkin.farm(size, min_pumpkin)	

	elif num_items(Items.Cactus) < min_cactus:
		if num_items(Items.Pumpkin) > get_cost(Unlocks.Cactus)[Items.Pumpkin]:
			unlock(Unlocks.Cactus)				
		
		cactus.farm(size, min_cactus)	

	else:
		min_hay += 10000
		min_wood += 10000
		min_carrot += 10000
		min_pumpkin += 10000
		min_cactus += 10000					