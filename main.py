import hay
import wood
import carrot
import pumpkin

min_hay = 500
min_wood = 500
min_carrot = 500
min_pumpkin = 500

size = get_world_size()

while get_pos_x() > 0:
	move(West)
while get_pos_y() > 0:
	move(South)

while True:
	
	if num_items(Items.Hay) < min_hay:
		hay.farm(size, min_wood)
		
	if num_items(Items.Wood) < min_wood:
		wood.farm(size, min_wood)
	
	if num_items(Items.Carrot) < min_carrot:
		carrot.farm(size, min_carrot)		

	if num_items(Items.Pumpkin) < min_pumpkin:
		pumpkin.farm(size, min_pumpkin)	

	else:
		min_hay += 500
		min_wood += 500
		min_carrot += 500
		min_pumpkin += 500					