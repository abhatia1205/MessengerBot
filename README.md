# lynbrook-messenger-ml-bot
A bot with AI which can help reply to messages and other such.

## Instructions for running bot

Use ```export FLASK_APP=app.py```, and then execute ```flask run```. This will create a responsive server which will answer to GET/POST requests. After which, use ```ngrok``` to create a temporary endpoint to test it: ```ngrok http 5000```. (5000 is because that is the host number at which we are running the program, this can be changed).

Credentials in the repo would be used for accessing the database.

Currently, we have added the basic connections of the bot, including connections to both firebase and Messenger. We will eventually begin adding more complicated operations as well.

## Instructions for testing database functions

To avoid the need to communicate orders through the messenger interface, we can instead directly test functions manipulating firebase by running ```export FLASK_APP=test_utils.py``` and then ```flask shell```. Afterwards, one would be able to import any python files from within the ```src.python.main.functions``` directory with little issues. 

Please note that ```test_utils#connectToTestDB()``` will not work if another terminal is open running another connection to the database, since we are using the same private credentials to connect to the database (we can of course generate another private key, but that is not recommended). 
