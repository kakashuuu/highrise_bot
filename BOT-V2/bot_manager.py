import json


class BotManager:
    filepath = "configs/bot_owner.json"
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)


    for key, values in data.items():
        print(f"Clé : {clé}, Valeur : {valeur}")
