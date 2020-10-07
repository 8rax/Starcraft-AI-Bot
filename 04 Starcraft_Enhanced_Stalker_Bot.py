#/*******************************************************
#Nom ......... : 04 Starcraft_Enhanced_Stalker_Bot.py
#Context ......: Advanced Protoss Stalker Micro Bot
#Role .........: Mid game push with upgrades and blink and superior Micro Skills                  
#Auteur ...... : JDO
#Version ..... : V1
#Date ........ : 07.10.2020
#Language : Python
#Version : 3.7.8
#Currently playing on AiArena
#********************************************************/
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import sc2
from sc2 import Race, Difficulty
from sc2.constants import *
from sc2.position import Point2, Point3
from sc2.unit import Unit
from sc2.player import Bot, Computer
from sc2.player import Human
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.ability_id import AbilityId
from sc2.units import Units
import random

#Our bot
class BraxBot(sc2.BotAI):

	def __init__(self):
		sc2.BotAI.__init__(self)
		self.proxy_built = False

	async def on_step(self, iteration):

		await self.distribute_workers()
		await self.build_probes()
		await self.build_pylons()
		await self.build_assimilators() 
		await self.expand()
		await self.build_production_build()
		await self.build_units()
		await self.fight()
		await self.chrono_boost()
		await self.morph_warpgate()
		await self.warpgate_research()
		await self.warp_new_units()
		await self.forge_research()
		await self.twilight_research()
		await self.micro()
		await self.build_obs()
		await self.send_obs()

	#Build more probes
	async def build_probes(self):
		#For every nexus that is created and that does not train a probe at the moment
		for nexus in self.townhalls.ready:
			if self.workers.amount < self.townhalls.amount * 22 and nexus.is_idle:
				if self.can_afford(UnitTypeId.PROBE):
					nexus.train(UnitTypeId.PROBE)

	#Build more pylons
	async def build_pylons(self):
		#If supply remaining is less than 5 and there is no pylon already being built, then we build a pylon near the nexus but 
		#We build it towards the center of the map so that the building are not getting in the way of our probes gathering minerals
		if self.supply_left < 6 and self.already_pending(UnitTypeId.PYLON) == 0 and self.can_afford(UnitTypeId.PYLON) and self.supply_used  < 100:
			for nexus in self.townhalls.ready:
				#if we have enough minerals to build a pylon
				if self.can_afford(UnitTypeId.PYLON) and self.already_pending(UnitTypeId.PYLON) == 0:
					await self.build(UnitTypeId.PYLON, near=nexus.position.towards(self.game_info.map_center, 5))
		elif self.supply_used  > 50 and self.supply_left < 6: 
			for nexus in self.townhalls.ready:
				#if we have enough minerals to build a pylon
				if self.can_afford(UnitTypeId.PYLON) and self.already_pending(UnitTypeId.PYLON) < 2:
					await self.build(UnitTypeId.PYLON, near=nexus.position.towards(self.game_info.map_center, 40))

	#Build gas assimilators
	async def build_assimilators(self):
	#We need gas to build stalkers so we first need to build an assimilator. Our distribute workers method will then assign workers to the gas
		if self.supply_used  > 15:
			for nexus in self.townhalls.ready:
				vgs = self.vespene_geyser.closer_than(15, nexus)
				for vg in vgs:
					if not self.can_afford(UnitTypeId.ASSIMILATOR):
						break
					worker = self.select_build_worker(vg.position)
					if worker is None:
						break
					if not self.gas_buildings or not self.gas_buildings.closer_than(1, vg):
						worker.build(UnitTypeId.ASSIMILATOR, vg)
						worker.stop(queue=True)
					
	#We build an expansation
	async def expand(self):
		if self.townhalls.ready.amount + self.already_pending(UnitTypeId.NEXUS) < 2:
			if self.can_afford(UnitTypeId.NEXUS):
				await self.expand_now()

	#Build production buildings
	async def build_production_build(self):
		if self.structures(UnitTypeId.PYLON).ready:
					#proxy = self.structures(UnitTypeId.PYLON).closest_to(self.enemy_start_locations[0])
					pylon = self.structures(UnitTypeId.PYLON).ready.random
					if self.already_pending(UnitTypeId.GATEWAY) == 1 and not self.structures(UnitTypeId.CYBERNETICSCORE) :
						# If we have no cyber core, build one
							if self.structures(UnitTypeId.GATEWAY).ready and self.can_afford(UnitTypeId.CYBERNETICSCORE)  and self.already_pending(UnitTypeId.CYBERNETICSCORE) == 0:
								await self.build(UnitTypeId.CYBERNETICSCORE, near=pylon)
					# Build up to 4 gates
					else:
						if (
							self.can_afford(UnitTypeId.GATEWAY)
							and self.structures(UnitTypeId.WARPGATE).amount + self.structures(UnitTypeId.GATEWAY).amount < 3
						):
							await self.build(UnitTypeId.GATEWAY, near=pylon)
						elif (
							self.can_afford(UnitTypeId.TWILIGHTCOUNCIL)
							and self.structures(UnitTypeId.WARPGATE).amount + self.structures(UnitTypeId.GATEWAY).amount > 2 
							and not self.structures(UnitTypeId.TWILIGHTCOUNCIL)
							and self.already_pending(UnitTypeId.TWILIGHTCOUNCIL) == 0
						):
							await self.build(UnitTypeId.TWILIGHTCOUNCIL, near=pylon)					
						elif (
							self.can_afford(UnitTypeId.FORGE)
							and self.structures(UnitTypeId.WARPGATE).amount + self.structures(UnitTypeId.GATEWAY).amount > 2 
							and not self.structures(UnitTypeId.FORGE)
							and  self.structures(UnitTypeId.CYBERNETICSCORE).ready.amount == 1
							and self.already_pending(UnitTypeId.FORGE) == 0
						):
							await self.build(UnitTypeId.FORGE, near=pylon)	
						elif (
							self.can_afford(UnitTypeId.GATEWAY)
							and self.structures(UnitTypeId.WARPGATE).amount + self.structures(UnitTypeId.GATEWAY).amount < 7
							and self.structures(UnitTypeId.NEXUS).amount > 1
						):
							await self.build(UnitTypeId.GATEWAY, near=pylon)
						elif (
							self.can_afford(UnitTypeId.ROBOTICSFACILITY)
							and self.structures(UnitTypeId.ROBOTICSFACILITY).amount  < 1
							and self.structures(UnitTypeId.NEXUS).amount > 1
						):
							await self.build(UnitTypeId.ROBOTICSFACILITY, near=pylon)						


	#Build Units - Stalkers
	async def build_units(self):
		#for each gw that is not producing units
		for gw in self.structures(UnitTypeId.GATEWAY).ready:
			#if we can afford it and if we have enough supply left
			#ccore = self.structures(UnitTypeId.CYBERNETICSCORE).ready.first
			#if ccore is not empty: 
			if self.can_afford(UnitTypeId.ZEALOT) and not self.structures(UnitTypeId.CYBERNETICSCORE).ready and gw.is_idle and self.units(UnitTypeId.ZEALOT).amount < 2:
				gw.train(UnitTypeId.ZEALOT)

	#Build Units - Stalkers
	async def build_obs(self):
		#for each gw that is not producing units
		for rf in self.structures(UnitTypeId.ROBOTICSFACILITY).ready:
			#if we can afford it and if we have enough supply left
			#ccore = self.structures(UnitTypeId.CYBERNETICSCORE).ready.first
			#if ccore is not empty: 
			if self.can_afford(UnitTypeId.OBSERVER ) and self.units(UnitTypeId.OBSERVER).amount < 2 and rf.is_idle:
				#we produce a stalker
				rf.train(UnitTypeId.OBSERVER)

	async def warp_new_units(self):
		for warpgate in self.structures(UnitTypeId.WARPGATE).ready:
			abilities = await self.get_available_abilities(warpgate)
			# all the units have the same cooldown anyway so let's just look at ZEALOT
			if AbilityId.WARPGATETRAIN_STALKER in abilities:
				#pos = proxy.position.to2.random_on_distance(4)
				'''
				pos = pylon = self.structures(UnitTypeId.PYLON).ready.random.position.random_on_distance(4)
				placement = await self.find_placement(AbilityId.WARPGATETRAIN_STALKER, pos, placement_step=1)
				if placement is None:
					# return ActionResult.CantFindPlacementLocation
					print("can't place")
					return
				warpgate.warp_in(UnitTypeId.STALKER, placement)
				'''
				self.ordered_pylons = sorted(self.structures(UnitTypeId.PYLON).ready, key=lambda pylon: pylon.distance_to(warpgate))
				pos = self.ordered_pylons[-1].position.random_on_distance(4)
				placement = await self.find_placement(AbilityId.WARPGATETRAIN_STALKER, pos, placement_step=1)
				if placement is None:
					# return ActionResult.CantFindPlacementLocation
					print("can't place")
					return
				warpgate.warp_in(UnitTypeId.STALKER, placement)

	async def chrono_boost(self):
		if self.structures(UnitTypeId.CYBERNETICSCORE).ready:
			ccore = self.structures(UnitTypeId.CYBERNETICSCORE).ready.first
		if self.structures(UnitTypeId.FORGE).ready:	
			forge = self.structures(UnitTypeId.FORGE).ready.first
		if self.structures(UnitTypeId.TWILIGHTCOUNCIL).ready:
			twilight = self.structures(UnitTypeId.TWILIGHTCOUNCIL).ready.first


		if self.structures(UnitTypeId.CYBERNETICSCORE).ready and not ccore.is_idle and not ccore.has_buff(BuffId.CHRONOBOOSTENERGYCOST):
			for nexus in self.townhalls.ready:
				if nexus.energy >= 50:
					nexus(AbilityId.EFFECT_CHRONOBOOSTENERGYCOST, ccore)

		elif self.structures(UnitTypeId.TWILIGHTCOUNCIL).ready and not twilight.is_idle and not twilight.has_buff(BuffId.CHRONOBOOSTENERGYCOST):
			for nexus in self.townhalls.ready:
				if nexus.energy >= 50:
					nexus(AbilityId.EFFECT_CHRONOBOOSTENERGYCOST, twilight)

		elif self.structures(UnitTypeId.FORGE).ready and not forge.is_idle and not forge.has_buff(BuffId.CHRONOBOOSTENERGYCOST):
			for nexus in self.townhalls.ready:
				if nexus.energy >= 50:
					nexus(AbilityId.EFFECT_CHRONOBOOSTENERGYCOST, forge)		

		elif self.workers.amount < 44:
			for nexus in self.townhalls.ready:
				if not nexus.has_buff(BuffId.CHRONOBOOSTENERGYCOST) and not nexus.is_idle and  self.already_pending(UnitTypeId.CYBERNETICSCORE) < 1 and self.workers.amount < 44:
					if nexus.energy >= 60:
						nexus(AbilityId.EFFECT_CHRONOBOOSTENERGYCOST, nexus)

		else:
			for nexus in self.townhalls.ready:
				if nexus.energy >= 50:
					for warpgate in self.structures(UnitTypeId.WARPGATE).ready:
						if not warpgate.has_buff(BuffId.CHRONOBOOSTENERGYCOST):
							if nexus.energy >= 50:
								nexus(AbilityId.EFFECT_CHRONOBOOSTENERGYCOST, nexus)

	async def warpgate_research(self):
		if (
			self.structures(UnitTypeId.CYBERNETICSCORE).ready
			and self.can_afford(AbilityId.RESEARCH_WARPGATE)
			and self.already_pending_upgrade(UpgradeId.WARPGATERESEARCH) == 0
		):
			ccore = self.structures(UnitTypeId.CYBERNETICSCORE).ready.first
			ccore.research(UpgradeId.WARPGATERESEARCH)

	async def twilight_research(self):
		if (
			self.structures(UnitTypeId.TWILIGHTCOUNCIL).ready
			and self.can_afford(AbilityId.RESEARCH_BLINK)
			and self.already_pending_upgrade(UpgradeId.BLINKTECH) == 0
		):
			twilight = self.structures(UnitTypeId.TWILIGHTCOUNCIL).ready.first
			twilight.research(UpgradeId.BLINKTECH)

	async def forge_research(self):
		if  self.structures(UnitTypeId.FORGE).ready:

			forge = self.structures(UnitTypeId.FORGE).ready.first
			if (
				#self.structures(UnitTypeId.FORGE).ready
				 self.can_afford(AbilityId.FORGERESEARCH_PROTOSSGROUNDWEAPONSLEVEL1)
				 and self.already_pending_upgrade(UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1) == 0
				 and forge.is_idle
			):
				forge.research(UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1)
			elif (
				self.can_afford(AbilityId.FORGERESEARCH_PROTOSSGROUNDARMORLEVEL1)
				and self.already_pending_upgrade(UpgradeId.PROTOSSGROUNDARMORSLEVEL1) == 0
				and forge.is_idle
			):
				forge.research(UpgradeId.PROTOSSGROUNDARMORSLEVEL1)
			elif (
				self.can_afford(AbilityId.FORGERESEARCH_PROTOSSGROUNDWEAPONSLEVEL2)
				and self.already_pending_upgrade(UpgradeId.PROTOSSGROUNDWEAPONSLEVEL2) == 0
				and forge.is_idle
			):
				forge.research(UpgradeId.PROTOSSGROUNDWEAPONSLEVEL2)
			elif (
				self.can_afford(AbilityId.FORGERESEARCH_PROTOSSGROUNDARMORLEVEL2)
				and self.already_pending_upgrade(UpgradeId.PROTOSSGROUNDARMORSLEVEL2) == 0
				and forge.is_idle
			):
				forge.research(UpgradeId.PROTOSSGROUNDARMORSLEVEL2)

	#Stalker behavior
	async def fight(self):
		# Make stalkers attack either closest enemy unit or enemy spawn location

		enemies = self.enemy_units.filter(lambda unit: unit.type_id not in {UnitTypeId.LARVA, UnitTypeId.EGG})
		enemy_fighters = enemies.filter(lambda u: u.can_attack) + self.enemy_structures(
			{UnitTypeId.BUNKER, UnitTypeId.SPINECRAWLER, UnitTypeId.PHOTONCANNON}
		)
		if self.units(UnitTypeId.STALKER).amount > 15:
			for stalker in self.units(UnitTypeId.STALKER).ready.idle:
				if enemy_fighters:
					# select enemies in range
					in_range_enemies = enemy_fighters.in_attack_range_of(stalker)
					if in_range_enemies:
						# prioritize workers
						workers = in_range_enemies({UnitTypeId.DRONE, UnitTypeId.SCV, UnitTypeId.PROBE})
						if workers:
							in_range_enemies = workers
						# special micro for ranged units
						if stalker.ground_range > 1:
							# attack if weapon not on cooldown
							if stalker.weapon_cooldown == 0:
								# attack enemy with lowest hp of the ones in range
								lowest_hp = min(in_range_enemies, key=lambda e: (e.health + e.shield, e.tag))
								self.do(stalker.attack(lowest_hp))
							else:
								# micro away from closest unit
								# move further away if too many enemies are near
								friends_in_range = self.units(UnitTypeId.STALKER).in_attack_range_of(stalker)
								closest_enemy = in_range_enemies.closest_to(stalker)
								distance = stalker.ground_range + stalker.radius + closest_enemy.radius
								if (
									len(friends_in_range) <= len(in_range_enemies)
									and closest_enemy.ground_range <= stalker.ground_range
								):
									distance += 1
								else:
									# if more than 5 units friends are close, use distance one shorter than range
									# to let other friendly units get close enough as well and not block each other
									if len(self.units(UnitTypeId.STALKER).closer_than(7, stalker.position)) >= 5:
										distance -= -1
								self.do(stalker.move(closest_enemy.position.towards(stalker, distance)))
						else:
							# target fire with melee units
							lowest_hp = min(in_range_enemies, key=lambda e: (e.health + e.shield, e.tag))
							self.do(stalker.attack(lowest_hp))
					else:
						# no unit in range, go to closest
						self.do(stalker.move(enemy_fighters.closest_to(stalker)))
				# no dangerous enemy at all, attack closest anything
				else:
					stalker.attack(self.enemy_start_locations[0])
		elif self.units(UnitTypeId.STALKER).amount > 0 and  self.units(UnitTypeId.STALKER).amount < 15:
			for stalker in self.units(UnitTypeId.STALKER).ready.idle:
				if enemy_fighters:
					# select enemies in range
					in_range_enemies = enemy_fighters.in_attack_range_of(stalker)
					if in_range_enemies:
						# prioritize workers
						workers = in_range_enemies({UnitTypeId.DRONE, UnitTypeId.SCV, UnitTypeId.PROBE})
						if workers:
							in_range_enemies = workers
						# special micro for ranged units
						if stalker.ground_range > 1:
							# attack if weapon not on cooldown
							if stalker.weapon_cooldown == 0:
								# attack enemy with lowest hp of the ones in range
								lowest_hp = min(in_range_enemies, key=lambda e: (e.health + e.shield, e.tag))
								self.do(stalker.attack(lowest_hp))
							else:
								# micro away from closest unit
								# move further away if too many enemies are near
								friends_in_range = self.units(UnitTypeId.STALKER).in_attack_range_of(unit)
								closest_enemy = in_range_enemies.closest_to(stalker)
								distance = stalker.ground_range + stalker.radius + closest_enemy.radius
								if (
									len(friends_in_range) <= len(in_range_enemies)
									and closest_enemy.ground_range <= stalker.ground_range
								):
									distance += 1
								else:
									# if more than 5 units friends are close, use distance one shorter than range
									# to let other friendly units get close enough as well and not block each other
									if len(self.units(UnitTypeId.STALKER).closer_than(7, stalker.position)) >= 5:
										distance -= -1
								self.do(stalker.move(closest_enemy.position.towards(stalker, distance)))
						else:
							# target fire with melee units
							lowest_hp = min(in_range_enemies, key=lambda e: (e.health + e.shield, e.tag))
							self.do(stalker.attack(lowest_hp))
					else:
						# no unit in range, go to closest
						self.do(stalker.move(enemy_fighters.closest_to(stalker)))
				# no dangerous enemy at all, attack closest anything
		else:
			for zealot in self.units(UnitTypeId.ZEALOT).ready.idle:
				if enemy_fighters:
					self.do(zealot.attack(random.choice(enemy_fighters)))
									
	async def morph_warpgate(self):
				# Morph to warp gate when research is complete
		for gateway in self.structures(UnitTypeId.GATEWAY).ready.idle:
			if self.already_pending_upgrade(UpgradeId.WARPGATERESEARCH) == 1:
				gateway(AbilityId.MORPH_WARPGATE)

	async def send_obs(self):
				# Morph to warp gate when research is complete		
		self.ordered_expansions = None
		self.ordered_expansions = sorted(
            self.expansion_locations.keys(), key=lambda expansion: expansion.distance_to(self.enemy_start_locations[0])
        )
				
		for obs in self.units(UnitTypeId.OBSERVER).ready:
			if obs.is_idle:

				self.do(obs.move(random.choice(self.ordered_expansions[0:4])))

	async def micro(self):

		home_location = self.start_location
		enemies: Units = self.enemy_units | self.enemy_structures
		enemies2 = self.enemy_units.filter(lambda unit: unit.type_id not in {UnitTypeId.DRONE,UnitTypeId.SCV})
		enemies_can_attack: Units = enemies2.filter(lambda unit: unit.can_attack_ground)
		for stalker in self.units(UnitTypeId.STALKER).ready:

			escape_location = stalker.position.towards(home_location, 4)
			enemyThreatsClose: Units = enemies_can_attack.filter(lambda unit: unit.distance_to(stalker) < 15)  # Threats that can attack the stalker

			if stalker.shield < 20 and enemyThreatsClose:

				abilities = await self.get_available_abilities(stalker)

				if AbilityId.EFFECT_BLINK_STALKER in abilities:
					#await self.order(stalker, EFFECT_BLINK_STALKER, escape_location)
					stalker(AbilityId.EFFECT_BLINK_STALKER, escape_location)
					continue
				else: 
					#if not self.has_order(MOVE, stalker):
					#stalker.move(escape_location)
					#continue
					retreatPoints: Set[Point2] = self.neighbors8(stalker.position, distance=2) | self.neighbors8(stalker.position, distance=4)
					# Filter points that are pathable
					retreatPoints: Set[Point2] = {x for x in retreatPoints if self.in_pathing_grid(x)}
					if retreatPoints:
						closestEnemy: Unit = enemyThreatsClose.closest_to(stalker)
						retreatPoint: Unit = closestEnemy.position.furthest(retreatPoints)
						stalker.move(retreatPoint)
						continue  # Continue for loop, dont execute any of the following

		# Stolen and modified from position.py
	def neighbors8(self, position, distance=1) -> Set[Point2]:
		p = position
		d = distance
		return self.neighbors4(position, distance) | {
			Point2((p.x - d, p.y - d)),
			Point2((p.x - d, p.y + d)),
			Point2((p.x + d, p.y - d)),
			Point2((p.x + d, p.y + d)),
		}


	# Stolen and modified from position.py
	def neighbors4(self, position, distance=1) -> Set[Point2]:
		p = position
		d = distance
		return {Point2((p.x - d, p.y)), Point2((p.x + d, p.y)), Point2((p.x, p.y - d)), Point2((p.x, p.y + d))}

def main():
	sc2.run_game(
		sc2.maps.get("Abyssal Reef LE"),
		[Bot(Race.Protoss, BraxBot()), Computer(Race.Zerg, Difficulty.VeryHard)],
		realtime=False,
		save_replay_as="Example.SC2Replay",
	)

#def main():
#    sc2.run_game(
#        sc2.maps.get("Abyssal Reef LE"),
#        [Human(Race.Terran), Bot(Race.Protoss, BraxBot())],
#        realtime=True,
#        save_replay_as="Example.SC2Replay",
#    )

if __name__ == "__main__":
	main()