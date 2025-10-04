from Grass import *
from Tree import *
from Carrots import *
from Pumpkins import *
from Dinosaurs import *
change_hat(Hats.Straw_Hat)
Can_carrot = get_cost(Unlocks.Carrots)
Can_pumpkin = get_cost(Unlocks.Pumpkins)
Can_dinos = get_cost(Unlocks.Dinosaurs)
while True:	
	AutoGrass(20000)
	AutoWood(20000000)
	for item in Can_carrot:
		if num_items(item) > Can_carrot[item]:
			AutoCarrots(90000000)
	for item in Can_pumpkin:
		if num_items(item) > Can_pumpkin[item]:	
			AutoPumpkin(140000000)
	for item in Can_dinos:
		if num_items(item) < Can_dinos[item]:	
			AutoDinos(1500000000)

			