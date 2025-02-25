from highrise import BaseBot
from highrise.webapi import HighriseAPI
from highrise.models import AnchorPosition, CurrencyItem, Item, Position, Reaction, SessionMetadata, User
from src.handlers.handleEvents import handle_chat, handle_join, handle_leave, handle_start, handle_whisper, handle_emote, handle_tips, handle_reactions, handle_movements
from src.handlers.handleCommands import CommandHandler
from asyncio import run as arun
from config.config import authorization

class Bot(BaseBot):
    def __init__(self, api: HighriseAPI):
        self.api = api
        self.command_handler = CommandHandler(self)
        super().__init__()

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await handle_start(self, session_metadata)

    async def on_chat(self, user: User, message: str) -> None:
        await handle_chat(self, user, message)

    async def on_whisper(self, user: User, message: str) -> None:
        await handle_whisper(self, user, message)

    async def on_user_join(self, user: User, pos: Position) -> None:
        await handle_join(self, user)

    async def on_user_leave(self, user: User) -> None:
        await handle_leave(self, user)

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        await handle_emote(self, user, emote_id, receiver)

    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
        await handle_tips(self, sender, receiver, tip)

    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        await handle_reactions(self, user, reaction, receiver)

    async def on_user_move(self, user: User, destination: Position | AnchorPosition) -> None:
        await handle_movements(self, user, destination)

if __name__ == "__main__":
    room_id = authorization.room
    api_token = authorization.token

    # ✅ API Token ka use karke bot initialize karo
    api = HighriseAPI(api_token)
    bot = Bot(api)

    # ✅ Bot ko run karo
    arun(bot.run())
