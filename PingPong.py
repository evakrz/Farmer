def AutoDinosPingPong(max_bones):
	while num_items(Items.Bone) < max_bones:
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
				if not move(North):
					change_hat(Hats.Straw_Hat)
					break
			if apple_x != None:
				break
			if not move(East):
				change_hat(Hats.Straw_Hat)
				break

		# Ping-pong loop
		while num_items(Items.Bone) < max_bones and apple_x != None:
			# Move to the edge column (left or right)
			if on_left:
				# Go to leftmost column (x=0)
				while get_pos_x() != 0:
					if not move(West):
						change_hat(Hats.Straw_Hat)
						break
			else:
				# Go to rightmost column
				while get_pos_x() != get_world_size() - 1:
					if not move(East):
						change_hat(Hats.Straw_Hat)
						break

			# Move to apple's Y position
			while get_pos_y() != apple_y:
				if get_pos_y() < apple_y:
					if not move(North):
						change_hat(Hats.Straw_Hat)
						break
				else:
					if not move(South):
						change_hat(Hats.Straw_Hat)
						break

			# Sweep across until we reach the apple
			if on_left:
				# Sweep right
				while get_pos_x() != apple_x:
					if not move(East):
						change_hat(Hats.Straw_Hat)
						break
			else:
				# Sweep left
				while get_pos_x() != apple_x:
					if not move(West):
						change_hat(Hats.Straw_Hat)
						break

			# Now we're on the apple - measure next apple position
			next_apple = measure()
			if next_apple != None:
				apple_x, apple_y = next_apple
			else:
				apple_x = None

			# Continue to edge
			if on_left:
				while get_pos_x() < get_world_size() - 1:
					if not move(East):
						change_hat(Hats.Straw_Hat)
						break
			else:
				while get_pos_x() > 0:
					if not move(West):
						change_hat(Hats.Straw_Hat)
						break

			# Toggle side for next iteration
			on_left = not on_left

	change_hat(Hats.Straw_Hat)
