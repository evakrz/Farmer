def AutoDinosPingPong(max_bones):
	clear()
	change_hat(Hats.Dinosaur_Hat)

	on_left = True

	# Find first apple by scanning
	apple_x = None
	apple_y = None
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_entity_type() == Entities.Apple:
				# Measure to get next apple position
				next_apple = measure()
				if next_apple != None:
					apple_x, apple_y = next_apple
					break
			move(North)
		if apple_x != None:
			break
		move(East)

	while num_items(Items.Bone) < max_bones and apple_x != None:
		# Move to the edge column (left or right)
		if on_left:
			# Go to leftmost column (x=0)
			while get_pos_x() != 0:
				move(West)
		else:
			# Go to rightmost column
			while get_pos_x() != get_world_size() - 1:
				move(East)

		# Move to apple's Y position
		while get_pos_y() != apple_y:
			if get_pos_y() < apple_y:
				move(North)
			else:
				move(South)

		# Sweep across until we reach the apple
		if on_left:
			# Sweep right
			while get_pos_x() != apple_x:
				move(East)
		else:
			# Sweep left
			while get_pos_x() != apple_x:
				move(West)

		# Now we're on the apple - measure next apple position
		next_apple = measure()
		if next_apple != None:
			apple_x, apple_y = next_apple
		else:
			apple_x = None

		# Continue to edge
		if on_left:
			while get_pos_x() < get_world_size() - 1:
				move(East)
		else:
			while get_pos_x() > 0:
				move(West)

		# Toggle side for next iteration
		on_left = not on_left

	change_hat(Hats.Straw_Hat)
