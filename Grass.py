def AutoGrass(max_amount):
	while num_items(Items.Hay) < max_amount:
		for x in range(get_world_size()):
			if get_ground_type() == Grounds.Soil:
				if can_harvest():
					harvest()
				till()		
			if can_harvest():
				harvest()
			move(East)
	return