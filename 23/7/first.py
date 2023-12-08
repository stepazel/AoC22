text = open('input', 'r')


def to_hex_str(number: str):
    return (number
            .replace('A', 'E')
            .replace('K', 'D')
            .replace('Q', 'C')
            .replace('J', 'B')
            .replace('T', 'A'))


def get_counts_of_labels(card: str) -> list:
    unique_labels = list(set(card))
    counts = []
    for label in unique_labels:
        counts.append(card.count(label))
    counts.sort(reverse=True)
    return counts


poker_hands = {
    'Highest card': 1,
    'One pair': 2,
    'Two pair': 3,
    'Three of a kind': 4,
    'Full house': 5,
    'Four of a kind': 6,
    'Five of a kind': 7
}


def get_card_type_value(card: str) -> int:
    counts = get_counts_of_labels(card)
    match counts:
        case [5]:
            return poker_hands['Five of a kind']
        case [4, 1]:
            return poker_hands['Four of a kind']
        case [3, 2]:
            return poker_hands['Full house']
        case [3, 1, 1]:
            return poker_hands['Three of a kind']
        case [2, 2, 1]:
            return poker_hands['Two pair']
        case [2, 1, 1, 1]:
            return poker_hands['One pair']
        case _:
            return poker_hands['Highest card']


cards_by_bid = {}
while True:
    line = text.readline()
    if not line:
        break

    card = line.split(' ')[0]
    bid = int(line.split(' ')[1])
    card = str(get_card_type_value(card)) + card
    cards_by_bid[bid] = int(to_hex_str(card), 16)

sorted_cards_by_bid = dict(sorted(cards_by_bid.items(), key=lambda item: item[1]))
answer = 0
rank = 1
for bid in sorted_cards_by_bid.keys():
    answer += bid * rank
    rank += 1
print(answer) # 249204891
