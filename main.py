import json
import os.path
import discord


def load_cards():
    if os.path.isfile("cardinventory.json"):
        try:
            card_list = json.load(open("cardinventory.json"))
            print("loaded %2d cards" % (len(card_list)))
            return card_list

        # Exit if card inventory is not in JSON format
        except json.decoder.JSONDecodeError as err:
            exit("Invalid JSON")
    # Exit if no cardinventory.json file
    else:
        exit("Missing cardinventory.json")


def load_bot_token():
    if os.path.isfile("bot-token.txt"):
        loaded_token = open('bot-token.txt').read()
        # Exit if there's nothing in the bot token file
        if loaded_token == "":
            exit("Bot token empty")

        print(f'Bot Token {loaded_token}')
        return loaded_token
    # Exit if no bot-token.txt file
    else:
        exit("Missing bot-token.txt")


def card_search_name(card_name, cardinventory):
    results = []

    for i in cardinventory:
        if card_name in i['n'].lower():
            results.append(i)

    # Code display each image link found
    # for i in results:
    #     print(i['iu'])

    return results


def card_search_card_id(card_id, cardinventory):
    results = []

    for i in cardinventory:
        if card_id in i['cid'].lower():
            results.append(i)

    # Code to display each image link found
    # for i in results:
    #     print(i['iu'])

    return results


# combines all search result img links into one string to send as a single message
def append_search_results(result_array):
    message = ""
    for i in result_array:
        message += (i['iu'] + "\n")
    return message


if __name__ == '__main__':
    cards = load_cards()
    token = load_bot_token()

    # Will throw a HTTPException and LoginFailure if the bot-token is invalid
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        # This will print every message seen by the bot
        # print(message.content)

        if message.content.startswith('$optcg -find -name '):
            query = message.content.split('$optcg -find -name ')[1].lower()
            print(query)
            results = card_search_name(query, cards)
            if len(results) == 0:
                await message.channel.send(f"No results found for `{query}`!")
            elif len(results) < 10:
                await message.channel.send(f"%2d Results for `{query}` :" % (len(results)))
                await message.channel.send(append_search_results(results))
            else:
                await message.channel.send(f"Too many results for `{query}`! try being more specific or using `$optcg "
                                           f"-find -cardid <Card ID>` instead.")

        if message.content.startswith('$optcg -find -cardid '):
            query = message.content.split('$optcg -find -cardid ')[1].lower()
            print(query)
            results = card_search_card_id(query, cards)
            if len(results) == 0:
                await message.channel.send(f"No results found for `{query}`!")
            elif len(results) < 10:
                await message.channel.send(f"%2d Results for `{query}` :" % (len(results)))
                await message.channel.send(append_search_results(results))
            else:
                await message.channel.send(f"Too many results for `{query}`!")


    client.run(token)
