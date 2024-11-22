import json
from highrise import User, Position
from config.config import config, messages


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = "settele"
        self.description = "Teleport a player to a specific position"
        self.aliases = ['settp']
        self.permissions = ['tele_setter']
        self.cooldown = 5

    async def execute(self, user: User, args: list, message: str):
        prefix = config.prefix
        name_tp = message.split(" ")[1]
        print(name_tp)
        with open("config/json/locations.json", "r+") as f:
            data = json.load(f)
            print(data)
            if name_tp in data["spawn"]["tp"]:
                response = await self.bot.highrise.get_room_users()
                for content in response.content:
                    if content[0].id == user.id:
                        if isinstance(content[1], Position):
                            position = content[1]
                            msg = f"{name_tp} is at ({position.x}x, {position.y}y, {position.z}z) facing '{position.facing}'"
                data["spawn"]["tp"][name_tp]["x"] = position.x
                data["spawn"]["tp"][name_tp]["y"] = position.y 
                data["spawn"]["tp"][name_tp]["z"] = position.z
                data["spawn"]["tp"][name_tp]["facing"] = position.facing

                print(data)        
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()  # Supprimer l'ancien contenu restant

                return await self.bot.highrise.chat(msg)
            await self.bot.highrise.chat("commandes valides : settele 1,2,3 ou vip")

