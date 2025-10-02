def AutoCarrots(max_amount):
	while num_items(Items.Carrot) < max_amount:
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				if get_ground_type() == Grounds.Grassland:
					if can_harvest():
						harvest()
					till()
					if not plant(Entities.Carrot):
						return
				else:	
					plant(Entities.Carrot)		
				if can_harvest():
					harvest()
					plant(Entities.Carrot)
				move(North)
			move(East)
	return