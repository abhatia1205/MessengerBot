# lynbrook-messenger-ml-bot
A bot with AI which can help reply to messages and other such.

## A quick description of the project
My freind, Richard Yu, and I created this chatbot as a way to create an automated communications touch point between members and officers for various clubs in our school. The project is still under way of being completed. The idea is that every club defines a set of members, topics, and actions of interst (for example, the math club might have John, Oliver, and Amy as members, Number Theory and Combinatorics as topics, and get_club_pounts, sign_up_for_math_compeitions, and email_officers as functions). The chatbot is made in a general enough way that it takes these sets of members, topics, and functions, as well as a text in natural language from a user, and perfomreds the interpreted functions on the users from the given text.

For example, if a user in the mathclub were to text "Sign me up for the Mandelbrot competition please", the NLP bot would interpret "me" as the texter (and map it to his id), and the rest of the phrase as closest to the function sign_up_for_competition. Thus, the bot would automatically return this interpreted information to a script specific to the club, and the request would be completed in an automated fashion.

The NLP part of the bot was coded by me, Anant Bhatia, and uses a sentiment analysis model created by myself, as well as entity linkage and named entity resolution functions from the NLTK library. I also coded my very own Word2Vec model to see numerically calculate the similarity between two stirings, which was used to determine users and actions in the text.

## Instructions for running bot

Use ```export FLASK_APP=app.py```, and then execute ```flask run```. This will create a responsive server which will answer to GET/POST requests. After which, use ```ngrok``` to create a temporary endpoint to test it: ```ngrok http 5000```. (5000 is because that is the host number at which we are running the program, this can be changed).

Credentials in the repo would be used for accessing the database.

Currently, we have added the basic connections of the bot, including connections to both firebase and Messenger. We will eventually begin adding more complicated operations as well.

## Instructions for testing database functions

To avoid the need to communicate orders through the messenger interface, we can instead directly test functions manipulating firebase by running ```export FLASK_APP=test_utils.py``` and then ```flask shell```. Afterwards, one would be able to import any python files from within the ```src.python.main.functions``` directory with little issues. 

## Caution with running ```chatbot.py```

As of right now, ```chatbot.py``` relies on Keras model files stored on a Kaggle account. The app will not run unless the model files are downloaded and the filepaths for the aformentioned model files are changed. These files will be uploaded later.
