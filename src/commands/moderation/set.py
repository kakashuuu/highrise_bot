import json
from highrise import User, Position
from config.config import messages, permissions

class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = "set"
        self.description = "Set the bot to a specific position"
        self.aliases = ['place']
        self.permissions = ['set']
        self.cooldown = 5

    async def execute(self, user: User, args: list, message: str):
        position = None
        try:
            room_users = await self.bot.highrise.get_room_users()
            for room_user, pos in room_users.content:
                if user.id == room_user.id:
                    if isinstance(pos, Position):
                        position = pos

            if position is not None:
                with open("config/json/locations.json", "r+") as file:
                    data = json.load(file)
                    file.seek(0)
                    data["spawn"]["bot"] = {
                        "x": position.x,
                        "y": position.y,
                        "z": position.z,
                        "facing": position.facing
                    }
                    json.dump(data, file)
                    file.truncate()
                await self.bot.highrise.walk_to(position)
                return "Updated bot position."
            else:
                return "Failed to update bot position."
        except Exception as e:
            print(f"Error setting bot position: {e}")
