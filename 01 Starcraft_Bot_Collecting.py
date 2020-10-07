#/*******************************************************
#Nom ......... : 01 Starcraft_Bot_Collecting.py
#Context ......: Gather monerals! 
#Role .........: Early game economy            
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
    	 await self.distribute_workers()

run_game(maps.get("Abyssal Reef LE"), [
    Bot(Race.Zerg, BraxBot()),
    Computer(Race.Protoss, Difficulty.Medium)
], realtime=True)