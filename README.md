# SE_Bot
A bot for StackExchange chatrooms. In use in ChemistrySE's main chatroom.

## How to use this framework [Outdated help, will update later]

Enter the email and password of the account you will be using in the appropriate fields at the beginning of the script.

A bunch of functions are defined, and at the end there's a comment "# Main Loop"

Below this comment you should have

    login()
    joinRooms({"id1": f1, "id2": f2})

This will connect the bot to the rooms with ids "id1", "id2". Every time some activity is detected in, for instance, the room with id "id1", the function "f1" will be called and the events will be passed as an argument.

The function "handleActivity", joint with "handleMessages", is an example of how you can costomize the bot do make it do whatever you want.

[More documentation will be added later on]
