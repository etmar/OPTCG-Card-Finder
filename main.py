import json
import discord

cards = json.load(open("cardinventory.json"))
# TODO: handle missing 'bot-token.txt'
token = open('bot-token.txt').read()


def card_search_name(card_name):
    results = []

    for i in cards:
        if card_name in i['n']:
            results.append(i)

    # for i in results:
    #     print(i['iu'])

    return results


def card_search_card_id(card_id):
    results = []

    for i in cards:
        if card_id in i['cid']:
            results.append(i)

    # for i in results:
    #     print(i['iu'])

    return results


if __name__ == '__main__':
    print("loaded %2d cards" % (len(cards)))
    print(f'Bot Token {token}')
    # May be better to init as a bot so the messages show up nice and fancy
    client = discord.Client(intents=discord.Intents.all())


    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))


    @client.event
    async def on_message(message):
        # need to do string to lowercase

        print(message.content)

        if message.content.startswith('$optcg -find -name '):
            query = message.content.split('$optcg -find -name ')[1]
            print(query)
            results = card_search_name(query)
            if len(results) == 0:
                await message.channel.send(f"No results found for `{query}`!")
            elif len(results) < 10:
                await message.channel.send(f"%2d Results for `{query}` :" % (len(results)))
                for i in results:
                    await message.channel.send(i['iu'])
            else:
                await message.channel.send(f"Too many results for `{query}`! try being more specific or using `$optcg "
                                           f"-find -cardid <Card ID>` instead.")

        if message.content.startswith('$optcg -find -cardid '):
            query = message.content.split('$optcg -find -cardid ')[1]
            print(query)
            results = card_search_card_id(query)
            if len(results) == 0:
                await message.channel.send(f"No results found for `{query}`!")
            elif len(results) < 10:
                await message.channel.send(f"%2d Results for `{query}` :" % (len(results)))
                for i in results:
                    await message.channel.send(i['iu'])
            else:
                await message.channel.send(f"Too many results for `{query}`!")


    client.run(token)
