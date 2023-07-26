#One Piece TCG Card Finder Discord Bot
Written in Python with using Discord.py. and onepiece-cardgame.dev's library of Card Data and Card Images. 

To install Discord.py, use:

`pip install -U discord.py`

To run, you will need to include a Discord Bot's Token, stored in a `bot-token.txt` file added to the top level of the
project folder. The Discord Bot will need messaging permissions and all Privileged Gateway Intents enabled.

Users can search for cards using `$optcg -find -name` followed by the character's name (E.G. "Sabo") to search for cards
by character name, or with `$optcg -find -cardid` followed by the card's Card ID (E.G. "OP04-083") to search for cards 
by ID. The bot will return images for all matching entries of the search, up to a max of 10 results. (Searching for 
"Luffy" would yield more than 10 results, so you'll need to search by Card ID for him)

Have fun!