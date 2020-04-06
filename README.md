# lynbrook-messenger-ml-bot
A bot with AI which can help reply to messages and other such.

## Instructions for running bot

Use ```export FLASK_APP=app.py```, and then execute ```flask run```. This will create a responsive server which will answer to GET/POST requests. After which, use ```ngrok``` to create a temporary endpoint to test it: ```ngrok http 5000```. (5000 is because that is the host number at which we are running the program, this can be changed).

Credentials in the repo would be used for accessing the database.

Currently, we have added the basic connections of the bot, including connections to both firebase and Messenger. We will eventually begin adding more complicated operations as well.

