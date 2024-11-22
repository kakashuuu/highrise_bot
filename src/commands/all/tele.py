import json
from highrise import User, Position
from config.config import config, messages


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = "tele"
        self.description = "Teleport a player to a specific position"
        self.aliases = ['tp']
        #self.permissions = ['teleport']
        self.cooldown = 5

    async def execute(self, user: User, args: list, message: str):
        prefix = config.prefix
        name_tp = message.split(" ")[1]
        with open("config/json/locations.json") as f:
            self.room_positions = json.load(f)  
        pos = self.room_positions["spawn"]["tp"][name_tp]
        position = Position(x=pos["x"], y=pos["y"], z=pos["z"], facing=pos["facing"])
        return await self.bot.highrise.teleport(user_id=user.id, dest=position)
    