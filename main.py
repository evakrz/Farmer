from Grass import *
from Trees import *
from Carrots import *
from Pumpkins import *
from Dinosaurs import *
change_hat(Hats.Straw_Hat)
Can_carrot = get_cost(Unlocks.Carrots)
Can_pumpkin = get_cost(Unlocks.Pumpkins)
Can_dinos = get_cost(Unlocks.Dinosaurs)
while True:	
	AutoGrass(1000)
	AutoWood(1000)
	for item in Can_carrot:
		if num_items(item) > Can_carrot[item]:
			AutoCarrots(900)
	for item in Can_pumpkin:
		if num_items(item) > Can_pumpkin[item]:	
			AutoPumpkin(1400)
	for item in Can_dinos:
		if num_items(item) < Can_dinos[item]:	
			AutoDinos(15000)

			