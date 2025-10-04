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
	

def AutoDinos(max_value):
	clear()
	change_hat(Hats.Dinosaur_Hat)
	while num_items(Items.Bone) < max_value:
		if get_world_size() % 2 == 0:
			for y in range(get_world_size()):
				move(North)
			for x in range(get_world_size()):
				move(East)
	
			move(South)
	
			while get_pos_y() > 1:
	
				while (get_pos_x()) > 1:
					if not move(West):
						change_hat(Hats.Straw_Hat)
						change_hat(Hats.Dinosaur_Hat)
				if not move(South):
					change_hat(Hats.Straw_Hat)
					change_hat(Hats.Dinosaur_Hat)
				while (get_pos_x()) < (get_world_size() - 1):
					if not move(East):
						change_hat(Hats.Straw_Hat)
						change_hat(Hats.Dinosaur_Hat)
				if not move(South):
					change_hat(Hats.Straw_Hat)
					change_hat(Hats.Dinosaur_Hat)
			while (get_pos_x()) > 0:
				if not move(West):
					change_hat(Hats.Straw_Hat)
					change_hat(Hats.Dinosaur_Hat)
		
		else:
			move_to_pos(0,1)
			change_hat(Hats.Dinosaur_Hat)
			change_hat(Hats.Dinosaur_Hat)
			change_hat(Hats.Dinosaur_Hat)
			change_hat(Hats.Dinosaur_Hat)
	
			alternate_path = False
			while True:
				go_north = True
				for x in range(get_world_size()-2):
					for _ in range(get_world_size()-2):
						if go_north:
							move(North)
						else:
							move(South)
	
					go_north = not go_north
					move(East)
				
				go_east = True
				for y in range(get_world_size()-2):
					if go_east:
						move(East)
					else:
						move(West)
					
					go_east = not go_east
					move(South)
				
				if alternate_path:
					move(West)
					move(South)
				else:
					move(South)
					move(West)
				alternate_path = not alternate_path
	
				for _ in range(get_world_size()-2):
					move(West)
				
				if not move(North):
					change_hat(Hats.Straw_Hat)
					move_to_pos(0,1)
					change_hat(Hats.Dinosaur_Hat)
AutoDinos(14000000)