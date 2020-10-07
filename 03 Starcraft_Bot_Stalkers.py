#/*******************************************************
#Nom ......... : 03 Starcraft_Bot_Stalkers.py
#Context ......: Simple stalker Bot
#Role .........: Mid game push             
#Auteur ...... : JDO
#Version ..... : V1
#Date ........ : 06.10.2020
#Language : Python
#Version : 3.7.8
#
#********************************************************/
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import *
import random

#Our bot
class BraxBot(sc2.BotAI):
	async def on_step(self, iteration):

		#List of available methods that we have created for our bot : 

		#Our bot distributes the workers on the mineral patchs :
		await self.distribute_workers()
		#Out bot builds workers : 
		await self.build_probes()
		#Out bot builds pylons : 
		await self.build_pylons()
		#Out bot builds Assimilators : 
		await self.build_assimilators() 
		#Out bot expands
		await self.expand()
	    #Out bot builds production buildings
		await self.build_production_build()
		#Out bot builds units
		await self.build_units()
		#Out bot fights
		await self.fight()

	#Build more probes
	async def build_probes(self):
		#For every nexus that is created and that does not train a probe at the moment
		for nexus in self.units(NEXUS).ready.idle:
			#If we have enough minerals for a probe and we have less than 70 probes
			if self.can_afford(PROBE) and self.units(PROBE).amount < 70:
				#Build a probe
				await self.do(nexus.train(PROBE))

	#Build more pylons
	async def build_pylons(self):
		#If supply remaining is less than 5 and there is no pylon already being built, then we build a pylon near the nexus but 
		#We build it towards the center of the map so that the building are not getting in the way of our probes gathering minerals
		if self.supply_left < 5 and not self.already_pending(PYLON):
			nexuses = self.units(NEXUS).ready
			if nexuses.exists:
				#if we have enough minerals to build a pylon
				if self.can_afford(PYLON):
					await self.build(PYLON, near=self.units(NEXUS).first.position.towards(self.game_info.map_center, 5))

	#Build gas assimilators
	async def build_assimilators(self):
	#We need gas to build stalkers so we first need to build an assimilator. Our distribute workers method will then assign workers to the gas
		#For every nexus
		for nexus in self.units(NEXUS).ready:
			#we get the list of vespene geyser closer than 15 unit to our nexus
			vespenes = self.state.vespene_geyser.closer_than(15.0, nexus)
			#for all vespene geysers that we have identified
			for vespene in vespenes: 
				#if we can't affor an assimilator
				if not self.can_afford(ASSIMILATOR):
					#We break
					break
				#else we select a probe that is available
				worker = self.select_build_worker(vespene.position)
				if worker is None:
					break
				#and finally if we can afford it, a location and the worker and no assimilator is being build 
				if not self.units(ASSIMILATOR).closer_than(1.0, vespene).exists: 
					#we build the assimilator ! 
					await self.do(worker.build(ASSIMILATOR, vespene))
	#We build an expansation
	async def expand(self):
		#if we have less than 2 nexuses and we can afford it we expend, prebuilt method
		if self.units(NEXUS).amount < 2 and self.can_afford(NEXUS):
			await self.expand_now()

	#Build production buildings
	async def build_production_build(self):
		#if we have a pylon (production buildings needs to be built near a pylon)
		if self.units(PYLON).ready.exists:
			#we select a random pylon that is already built
			pylon = self.units(PYLON).ready.random
			#If we have already a gateway but no cyberneticscore
			if self.units(GATEWAY).ready.exists and not self.units(CYBERNETICSCORE):
				#if we can afford one and we are currently not already building a cyberneticscore
				if self.can_afford(CYBERNETICSCORE) and not self.already_pending(CYBERNETICSCORE):
					#then we build a cybernetics core ! 
					await self.build(CYBERNETICSCORE, near=pylon)
			#Else, if we have less than 7 gates
			elif len(self.units(GATEWAY)) < 3: 
				#and if we can afford it
				if self.can_afford(GATEWAY):
					#We build a gateway
					await self.build(GATEWAY, near=pylon)
			elif len(self.units(GATEWAY)) > 3 and not self.already_pending(GATEWAY): 
				#and if we can afford it
				if self.can_afford(GATEWAY):
					#We build a gateway
					await self.build(GATEWAY, near=pylon)
	#Build Units - Stalkers
	async def build_units(self):
		#for each gw that is not producing units
		for gw in self.units(GATEWAY).ready.idle:
			#if we can afford it and if we have enough supply left
			if self.can_afford(STALKER) and self.supply_left > 2:
				#we produce a stalker
				await self.do(gw.train(STALKER))

	#find a target to attack
	def target(self, state):
		#if we identified an ennemy unit
		if len(self.known_enemy_units) > 0:
			#we return one of those units randomly
			return random.choice(self.known_enemy_units)
		else:
			#Else we return the starting location of the enemy
			return self.enemy_start_locations[0]
	
	#Stalker behavior
	async def fight(self):
		#If we have more than 15 stalkers
		if self.units(STALKER).amount > 15:
			#Every stalker that is not doing anything
			for s in self.units(STALKER).idle:
				#Will attack either a known unit or go attack the base of our enemy
				await self.do(s.attack(self.target(self.state)))
		#But if we have less than 15 stalkers
		elif self.units(STALKER).amount > 0 and self.units(STALKER).amount < 15:
			#if we see enemy units
			if len(self.known_enemy_units) > 0:
				#for every idle stalker
				for s in self.units(STALKER).idle:
					#attack a random unit that we know
					await self.do(s.attack(random.choice(self.known_enemy_units)))
	

#Launch the game to fight an easy Zerg bot
run_game(maps.get("Abyssal Reef LE"), [
	Bot(Race.Protoss, BraxBot()),
	Computer(Race.Zerg, Difficulty.Easy)
], realtime=False)