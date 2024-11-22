import json
from highrise.models import SessionMetadata, Position
from config.config import config, loggers


async def on_start(bot, session_metadata: SessionMetadata) -> None:
    if loggers.SessionMetadata:
        rate_limits = session_metadata.rate_limits
        formatted_rate_limits = ', '.join(
            str(value) for value in rate_limits.values())
        print(f"Bot ID: {session_metadata.user_id}\nRate Limits: {formatted_rate_limits}\nConnection ID: {session_metadata.connection_id}\nSDK Version: {session_metadata.sdk_version}")

    coords = config.coordinates
    with open("./config/json/locations.json", "r") as file:
        data = json.load(file)
        pos = data["spawn"]["bot"]
    await bot.highrise.walk_to(Position(pos["x"], pos["y"], pos["z"], pos["facing"]))
    print(f"{config.botName} is now ready.")


