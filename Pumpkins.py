def AutoPumpkin(max_value):
	if not plant(Entities.Pumpkin):
		return
	clear()
	
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_ground_type() == Grounds.Grassland:
				if can_harvest():
						harvest()	
				till()
			else:	
				plant(Entities.Pumpkin)
			move(North)
		move(East)
	while num_items(Entities.Pumpkin) < max_value:
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				if get_ground_type() == Grounds.Grassland:
					till()
				else:	
					plant(Entities.Pumpkin)
				pumpkins = 0
				for x in range(get_world_size()):
					for y in range(get_world_size()):	
						if get_entity_type() == Entities.Pumpkin and can_harvest():
							pumpkins += 1
						else:
							plant(Entities.Pumpkin)
						move(North)
					move(East)
				if can_harvest() and pumpkins == get_world_size()**2:
					harvest()
					plant(Entities.Pumpkin)
				move(North)
			move(East)
			pumpkins = 0
