#/*******************************************************
#Nom ......... : 02 Starcraft_Bot_Worker_Rush.py
#Context ......: Attack with all workers! 
#Role .........: Early game push             
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

class BraxBot(sc2.BotAI):
    async def on_step(self, iteration):
        if iteration == 0:
            for worker in self.workers:
                await self.do(worker.attack(self.enemy_start_locations[0]))

run_game(maps.get("Abyssal Reef LE"), [
    Bot(Race.Zerg, BraxBot()),
    Computer(Race.Protoss, Difficulty.Medium)
], realtime=True)