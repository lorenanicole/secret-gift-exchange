import itertools
import random

import pandas as pd


def select(names):
    if len(names) == 3:
        return [(names[0], names[1], names[2])]
    if len(names) == 2:
        return [(names[0], names[1])]
    random.shuffle(names)
    possible_pairs = list(itertools.combinations(names, 2))
    pair = [possible_pairs.pop()]
    names.remove(pair[0][0]), names.remove(pair[0][1])
    pairings = pair + select(names)
    return pairings


if __name__ == "__main__":
    print('Drawing names...')
    names_df = pd.read_csv('names.csv')
    gift_pairings = select(names_df.Name.to_list())
    gift_exchange_info = []
    print('Outputting pairs to csv...')
    for pair in gift_pairings:
        if len(pair) == 2:
            gift_exchange_info.append({
                'gifter': pair[0],
                'gifter email': names_df[names_df.Name == pair[0]].Email.item(),
                'recipient': pair[1],
                'recipient address': names_df[names_df.Name == pair[1]]["Address (street, city, country and zip code)"].item(),
                'recipient email': names_df[names_df.Name == pair[1]].Email.item(),
                'gift information': names_df[names_df.Name == pair[1]]["Please provide some choices of things you want to receive"].item()
            })
            gift_exchange_info.append({
                'gifter': pair[1],
                'gifter email': names_df[names_df.Name == pair[1]].Email.item(),
                'recipient': pair[0],
                'recipient address': names_df[names_df.Name == pair[0]]["Address (street, city, country and zip code)"].item(),
                'recipient email': names_df[names_df.Name == pair[0]].Email.item(),
                'gift information': names_df[names_df.Name == pair[1]]["Please provide some choices of things you want to receive"].item()
            })
        else:
            gift_exchange_info.append({
                'gifter': pair[0],
                'gifter email': names_df[names_df.Name == pair[0]].Email.item(),
                'recipient': pair[1],
                'recipient address': names_df[names_df.Name == pair[1]]["Address (street, city, country and zip code)"].item(),
                'recipient email': names_df[names_df.Name == pair[1]].Email.item(),
                'gift information': names_df[names_df.Name == pair[1]]["Please provide some choices of things you want to receive"].item()
            })
            gift_exchange_info.append({
                'gifter': pair[1],
                'gifter email': names_df[names_df.Name == pair[1]].Email.item(),
                'recipient': pair[2],
                'recipient address': names_df[names_df.Name == pair[2]]["Address (street, city, country and zip code)"].item(),
                'recipient email': names_df[names_df.Name == pair[2]].Email.item(),
                'gift information': names_df[names_df.Name == pair[1]]["Please provide some choices of things you want to receive"].item()
            })
            gift_exchange_info.append({
                'gifter': pair[2],
                'gifter email': names_df[names_df.Name == pair[2]].Email.item(),
                'recipient': pair[0],
                'recipient address': names_df[names_df.Name == pair[0]]["Address (street, city, country and zip code)"].item(),
                'recipient email': names_df[names_df.Name == pair[0]].Email.item(),
                'gift information': names_df[names_df.Name == pair[1]]["Please provide some choices of things you want to receive"].item()
            })

    gift_exchange_df = pd.DataFrame(gift_exchange_info)
    gift_exchange_df.to_csv('secret_exchange_pairings.csv', index=False)

messages = []
for indx, person in gift_exchange_df.iterrows():
    text = f'👋 {person.gifter},\n' \
    f'Fellow Octogatos Michelle, Gloridel, & Lorena here! We\'re writing to share your information for your pair for this year\'s Amigosgiving!\n' \
    f' This year you are buying for....... {person.recipient}!!!!\n' \
    f'Here is the information you\'ll need:\n' \
    f'Email: {person["recipient email"]}\n'  \
    f'Address: {person["recipient address"]}\n' \
    f'What they want: {person["gift information"]}\n'  \
    f'Remember the limit is $25.00 USD and  the Amigosgiving is happening on January 6th 2021 at 2:00pm PST.'  \
    f'You\'re welcome to expense a meal up to  $25.00 USD too!\n'  \
    f'See you in 2021!\n' \
    f'Michelle, Gloridel, & Lorena'
    messages.append(f'=== Message for Gifter {indx+1} ===')
    messages.append('\n\n\n')
    messages.append(text)
    messages.append('\n\n\n')
    messages.append(f'===================================')
print('Outputting email text...')
with open('messages.txt', 'w') as file:
    for message in messages:
        file.writelines(message)
print('Done!')
