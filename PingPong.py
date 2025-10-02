def go_to_start():
	while get_pos_x() != 0:
		move(East)
	while get_pos_y() != 0:
		move(North)
		
def move_to_pos(x, y):
	while get_pos_x() != x:
		move(East)
	while get_pos_y() != y:
		move(North)


def move_when_noapple(direction):
	if get_entity_type() == Entities.Apple:
		change_hat(Hats.Dinosaur_Hat)
		return
	move(direction)
	change_hat(Hats.Dinosaur_Hat)


	

def AutoDinosPingPOng():
	clear()
	go_to_start()
	change_hat(Hats.Dinosaur_Hat)
	if get_world_size() % 2 == 0:
		for y in range(get_world_size()):
			move_when_noapple(North)
			change_hat(Hats.Straw_Hat)
			change_hat(Hats.Dinosaur_Hat)
		for x in range(get_world_size()):
			move_when_noapple(East)
			change_hat(Hats.Straw_Hat)
			change_hat(Hats.Dinosaur_Hat)
		move_when_noapple(South)
		change_hat(Hats.Straw_Hat)
		change_hat(Hats.Dinosaur_Hat)
		while get_pos_y() > 1:

			while (get_pos_x()) > 1:
				if not move_when_noapple(West):
					change_hat(Hats.Straw_Hat)
					change_hat(Hats.Dinosaur_Hat)
			if not move_when_noapple(South):
				change_hat(Hats.Straw_Hat)
				change_hat(Hats.Dinosaur_Hat)
			while (get_pos_x()) < (get_world_size() - 1):
				if not move_when_noapple(East):
					change_hat(Hats.Straw_Hat)
					change_hat(Hats.Dinosaur_Hat)
			if not move_when_noapple(South):
				change_hat(Hats.Straw_Hat)
				change_hat(Hats.Dinosaur_Hat)
		while (get_pos_x()) > 0:
			if not move_when_noapple(West):
				change_hat(Hats.Straw_Hat)
				change_hat(Hats.Dinosaur_Hat)
	
	else:
		move_to_pos(0,1)
		change_hat(Hats.Dinosaur_Hat)

		alternate_path = False
		for x in range(1):

			go_north = True
			for x in range(get_world_size()-3):
				for _ in range(get_world_size()-2):
					if go_north:
						move_when_noapple(North)
					else:
						move_when_noapple(South)

				go_north = not go_north
				move_when_noapple(East)
			
			go_east = True
			for y in range(get_world_size()-2):
				if go_east:
					move_when_noapple(East)
				else:
					move_when_noapple(West)
				
				go_east = not go_east
				move_when_noapple(South)
			
			if alternate_path:
				move_when_noapple(West)
				move_when_noapple(South)
			else:
				move_when_noapple(South)
				move_when_noapple(West)
			alternate_path = not alternate_path

			for _ in range(get_world_size()-2):
				move_when_noapple(West)
			
			if not move_when_noapple(North):
				change_hat(Hats.Straw_Hat)
				move_to_pos(0,1)
				change_hat(Hats.Dinosaur_Hat)

def DInosOP():
	AutoDinosPingPOng()
	x, y = measure()
	for x in range(abs(get_pos_x() - get_world_size())):
		if get_pos_x() < get_world_size() / 2:
			move_when_noapple(West)
			go_east = True
		else:
			move_when_noapple(East)
			go_east = False


	for _ in range(abs(get_pos_y() - y)):
		if y < get_pos_y():
			move_when_noapple(South)
		else:
			move_when_noapple(North)

	for _ in range(get_world_size()):
		if go_east:
			move_when_noapple(East)
			go_east = False
		else:
			move_when_noapple(West)
			go_east = True

DInosOP()