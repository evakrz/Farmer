def AutoWood(max_amount):
	while num_items(Items.Wood) < max_amount:
		for x in range(get_world_size()):
			for y in range(get_world_size()):		
				if can_harvest(): 
					harvest()
				if x % 2 == 0 and y % 2 == 0 or (x % 2 == 1 and y % 2 == 1):
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)	
				move(North)
			move(East)
	return
	
#AutoWood(259999999999999000)