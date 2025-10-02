
	while True:
		for x in range(get_world_size()):
			for y in range(get_world_size()):	
				if get_ground_type() == Grounds.Soil:
					till()		
				if can_harvest():
					harvest()
					plant(Entities.Bush)
				move(North)
			move(East)
	