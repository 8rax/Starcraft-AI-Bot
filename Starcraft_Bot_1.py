import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PROBE, PYLON, ASSIMILATOR, GATEWAY, CYBERNETICSCORE, STALKER
import random
#This bots defeats Easy and Medium BOTS quite convincingly

#Our bot
class BraxBot(sc2.BotAI):
    async def on_step(self, iteration):
    	#Our bot distributes the workers on the minerals patch
    	await self.distribute_workers()
    	#Rest of concurrent tasks to be performed : 
    	await self.build_workers()
    	await self.build_pylons()
    	await self.build_assimilators() 
    	await self.expand()
    	await self.offensive_force_buildings()
    	await self.build_offensive_force()
    	await self.attack()

    #Build more workers
    async def build_workers(self):
        # nexus = command center
        for nexus in self.units(NEXUS).ready.noqueue:
            if self.can_afford(PROBE) and self.units(PROBE).amount < 70:
                await self.do(nexus.train(PROBE))
    #Build more pylons to increase your supply
    async def build_pylons(self):
    	#If supply remaining is less than 5 and there is no pylon already being built, then we build a pylon near the nexus
    	if self.supply_left < 5 and not self.already_pending(PYLON):
    		nexuses = self.units(NEXUS).ready
    		if nexuses.exists:
    			if self.can_afford(PYLON):
    				await self.build(PYLON, near=nexuses.first)

    #Build gas assimilators
    async def build_assimilators(self):
    	for nexus in self.units(NEXUS).ready:
    		vaspenes = self.state.vespene_geyser.closer_than(15.0, nexus)
    		for vaspene in vaspenes: 
    			if not self.can_afford(ASSIMILATOR):
    				break
    			worker = self.select_build_worker(vaspene.position)
    			if worker is None:
    				break
    			#If there is no assimilator that exists closely
    			if not self.units(ASSIMILATOR).closer_than(1.0, vaspene).exists: 
    				await self.do(worker.build(ASSIMILATOR, vaspene))
    #Expand ! 
    async def expand(self):
    	if self.units(NEXUS).amount < 3 and self.can_afford(NEXUS):
    		await self.expand_now()

    #Build Gateways and one cybernetic core
    async def offensive_force_buildings(self):
    	if self.units(PYLON).ready.exists:
    		pylon = self.units(PYLON).ready.random
    		if self.units(GATEWAY).ready.exists and not self.units(CYBERNETICSCORE):
    			if self.can_afford(CYBERNETICSCORE) and not self.already_pending(CYBERNETICSCORE):
    				await self.build(CYBERNETICSCORE, near=pylon)

    		elif len(self.units(GATEWAY)) < 7: 
    			if self.can_afford(GATEWAY) and not self.already_pending(GATEWAY):
    				await self.build(GATEWAY, near=pylon)
    #Build stalkers
    async def build_offensive_force(self):
    	for gw in self.units(GATEWAY).ready.noqueue:
    		if self.can_afford(STALKER) and self.supply_left > 0:
    			await self.do(gw.train(STALKER))

    #Find an ennemy, a structure OR go and attack the starting location of the enemy
    def find_target(self, state):
        if len(self.known_enemy_units) > 0:
            return random.choice(self.known_enemy_units)
        elif len(self.known_enemy_structures) > 0:
            return random.choice(self.known_enemy_structures)
        else:
            return self.enemy_start_locations[0]
   	
   	#The stalkers will defend our base by attacking any aggressive units on the map or attack an ennemy if we have a big army
    async def attack(self):
        if self.units(STALKER).amount > 15:
            for s in self.units(STALKER).idle:
                await self.do(s.attack(self.find_target(self.state)))

        elif self.units(STALKER).amount > 3:
            if len(self.known_enemy_units) > 0:
                for s in self.units(STALKER).idle:
                    await self.do(s.attack(random.choice(self.known_enemy_units)))
    

#Launch the game map/our bot/the other Bot/Real time ?
run_game(maps.get("Abyssal Reef LE"), [
    Bot(Race.Protoss, BraxBot()),
    Computer(Race.Zerg, Difficulty.Easy)
], realtime=False)