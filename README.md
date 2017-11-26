# SE_Bot
A bot for StackExchange chatrooms. In use in ChemistrySE's main chatroom.

The framework is located in `chatbot.py`, all the other files are optional.

`chatbot.py` provides an interface to communicate with StackExchange's chatrooms.

An example of how to use this framework is provided in `main.py`, Chemobot's script.

`upsidedown.py`is simply a library used in Chemobot.

## How to use this framework

First of all initalize the chatbot:
````
from chatbot import Chatbot
my_chatbot=Chatbot() # create an instance of Chatbot
my_chatbot.login() # logs in to the SE network. username/pass are input through the CLI, or decrypted from a previous save file
````

Then join the rooms you want:
````
room1=my_chatbot.joinRoom(1,handleEvents) # Sandbox
room3229=my_chatbot.joinRoom(3229,handleEvents) # The Periodic Table
#my_chatbot.joinRoom(roomId, callbackEventFunction)
````
 You can now receive events from the chatroom with your `callbackEventFunction`, and send / edit messages using `room.sendMessage(msg)` or `room.editMessage(newMsg, msgId)`


And you're set !

## Some documentation

### chatbot.joinRoom(roomId, callbackEventFunction)

Upon joining a room using this function, whenever the chatbot received events from that room, it will call `callbackEventFunction(room, event)`.

`chatbot.joinRoom` returns a `Room`object.

### Room objects - sending and editing messages

`Room`objects enable you to send and edit messages in the joined room - `room=chatbot.joinRoom(roomId, callbackEventFunction)`

Sending a message: `id=room.sendMessage('Hello, world!')`. This functions returns the `id` of the sent message.

Editing a message: `room.editMessage('Goodbye, World!', id)`

### Credidentials

When calling `chatbot.login()`, if your credidentials have not been saved, they will be asked as inputs in the CLI. Then, you will have the possibility to store them in an encrypted file (DES encryption) protected by a password. You will then be able to login using only that password.

Credidentials are stored in `Credidentials` in the working directory.

### Events

The events passed on to your `callbackEventFunction` are the unmodified events sent by the server, in the following template:

`{'e': [{'event_type': 1, 'time_stamp': 1511703791, 'content': 'test string', 'id': 81969291, 'user_id': 200207, 'user_name': 'Chemobot', 'room_id': 1, 'room_name': 'Sandbox', 'message_id': 41365631}], 't': 81969291, 'd': 1}`

All the parameters are explicit, except the `event_type`. Here are some event types values:

* `'event_type': 1` - new message
* `'event_type': 3` - user entered the room
* `'event_type': 6` - a message had its star count changed
* `'event_type': 10` - deleted message
