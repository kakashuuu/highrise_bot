class config:
    # Basic configuration: If you are unsure how to obtain the Bot ID, simply start the bot and it will be logged in the console.
    prefix = "!"
    botID = '67473ea326de90b560dc2bfe'
    botName = 'senku'
    ownerName = 'kakashi'
    roomName = 'Home'
    coordinates = {
        'x': 8.5,
        'y': 0.6000,
        'z': 20.5,
        'facing': 'FrontRight'
    }


class loggers:
    # The following settings are related to events. Each event log can be enabled or disabled. Note that turning these off will not affect their usage in the game.
    SessionMetadata = True
    messages = True
    whispers = True
    joins = True
    leave = True
    tips = True
    emotes = False
    reactions = False
    userMovement = False


class messages:
    # The following are optional and serve as a basic usage example for calling messages and replacing variables.
    invalidPosition = "Your position could not be determined."
    invalidPlayer = "{user} is not in the room."
    invalidUser = "User {user} is not found."
    invalidUsage = "Usage: {prefix}{commandName}{args}"
    invalidUserFormat = "Invalid user format. Please use '@username'."


class permissions:
    # You can add as many IDs as you want, for example: ['id1', 'id2'].
    owners = ['669c057a9e348d95fa896b66']
    moderators = ['669c057a9e348d95fa896b66']


class authorization:
    # To obtain your token, visit https://highrise.game/ and log in. Then, go to the settings and create a new bot. Accept the terms and generate a token.
    # To obtain your room ID, go to the game and navigate to the top right corner where the player list is displayed. Click on "Share this room" and copy the ID.
    room = '6746480b6ec0bcb87994c1af'
    token = 'b8584eca67175f99d751eb2f0b9300de11690ece96a7f99da247345800d4337d'
