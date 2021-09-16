# Facheng Guo | Auguest 2021
# Special thanks for Qixuan Yu for his support on debug.

import random

# Generate n cards, only use when initial the game.
def _get_n_cards(num=0):
    initial_cards = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
    return_cards = []
    while len(return_cards) < num:
        card = random.choice(initial_cards)
        initial_cards.remove(card)
        return_cards.append(card)
    return return_cards

# Get 2 more card after game started. input_list is the cards already assigned. 
def _two_more_card(input_list):
    initial_cards = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
    return_cards = []
    for i in input_list:
        initial_cards.remove(i)
    while len(return_cards) < 2:
        card = random.choice(initial_cards)
        initial_cards.remove(card)
        return_cards.append(card)
    return return_cards

# Transfer the card number to suit/value.
def card_transfer_to_value_color(cards):
    result = []
    for card in cards:
        result.append([card // 13, card % 13])
    return result

# Fingerprint the Flush.
def Flush_to_fingerprint(cards):
    result = []
    colors_list = [card[0] for card in cards]
    colors_set = set(colors_list)

    if len(colors_set) < 4:
        for color in colors_set:
            if colors_list.count(color) > 4:
                for card in cards:
                    if card[0] == color:
                        result.append(card[1])

    if len(result) > 4:
        return sorted(result,reverse=True)
    else:
        return [0,0,0,0,0]

# Fingerprint the Straight.
def Straight_to_fingerprint(cards):
    values_list = [card[1] for card in cards]
    values_set = set(values_list)
    if len(values_set) >= 5:
        if values_list[-1] - values_list[-5] == 4:
            return values_list[-1]
        try:
            if values_list[-2] - values_list[-6] == 4:
                return values_list[-2]
        except:
            pass
        try:
            if values_list[-3] - values_list[-7] == 4:
                return values_list[-3]
        except:
            pass
    return 0

# Fingerprint the Straight Flush
def Straight_Flush_to_fingerprint(cards):
    colors_list = [card[0] for card in cards]
    colors_set = set(colors_list)
    values_list = [card[1] for card in cards]
    values_set = set(values_list)
    result_list = []
    if len(colors_set) > 3:
        return 0

    for color in colors_list:
        if colors_list.count(color) > 4:
            for card in cards:
                if card[0] == color:
                    result_list.append(card[1])

    result_list.sort()

    if len(result_list) >= 5:
        if result_list[-1] - result_list[-5] == 4:
            return result_list[-1]
        try:
            if result_list[-2] - result_list[-6] == 4:
                return result_list[-2]
        except:
            pass
        try:
            if result_list[-3] - result_list[-7] == 4:
                return result_list[-3]
        except:
            pass

    return 0
        
# Fingerprint the Four of a King.
def Four_of_a_King_to_fingerprint(cards):

    values_list = [card[1] for card in cards]
    values_set = set(values_list)

    if len(values_set) < 5:
        for value in values_set:
            if values_list.count(value) == 4:
                return value
    return 0

# Fingerprint the Full House.
def Full_House_to_fingerprint(cards):
    values_list = [card[1] for card in cards]
    values_set = set(values_list)
    card_type = len(values_set)
    _3_card_list = []
    _2_card_list = []
    if 6 > card_type > 3 :

        for value in values_set:

            if values_list.count(value) == 3:
                _3_card_list.append(value)
            if values_list.count(value) == 2:
                _2_card_list.append(value)

    _3_card_type = len(_3_card_list)
    _2_card_type = len(_2_card_list)

    if _3_card_type == 1 and _2_card_type > 0:
        return [_3_card_list[0],max(_2_card_list)]

    if _3_card_type == 2 and _2_card_type > 0:
        _3_card_list.sort()
        _2_card_list.append(_3_card_list[0])
        return [_3_card_list[1],max(_2_card_list)]
    
    return [0,0]

# Fingerprint the Three of a King.
def Three_of_a_King_to_fingerprint(cards):
    values_list = [card[1] for card in cards]
    values_set = set(values_list)
    rest_cards_list = values_list
    result = []

    if len(values_set) == 5:
        for value in values_set:
            if values_list.count(value) == 3:
                result.append(value)

        if not result == []:
            rest_cards_list.remove(result[0])
            rest_cards_list.remove(result[0])
            rest_cards_list.remove(result[0])

            rest_cards_list.sort(reverse=True)
            result = result + rest_cards_list
            return result[0:3]
    return [0,0,0]

# Fingerprint Two Pairs.
def Two_Pair_to_fingerprint(cards):
    values_list = [card[1] for card in cards]
    values_set = set(values_list)
    rest_cards_list = values_list
    rest_cards_list.sort(reverse=True)
    result = []

    if len(values_set) == 5:
        for value in values_set:
            if values_list.count(value) == 4:
                return [0,0,0]
            if values_list.count(value) == 3:
                return [0,0,0]       
            if values_list.count(value) == 2:
                result.append(value)

        if len(result) == 0:
            return [0,0,0]
        if len(result) == 1:
            return [0,0,0]

        result.sort(reverse=True)

        # If there are 3 pairs, only take the largest 2.
        result = result[0:2]

        rest_cards_list.remove(result[0])
        rest_cards_list.remove(result[0])
        rest_cards_list.remove(result[1])
        rest_cards_list.remove(result[1])

        result.append(max(rest_cards_list))
        return result

    else:
        return [0,0,0]

# Fingprint the One Pair.
def One_Pair_to_fingerprint(cards):
    values_list = [card[1] for card in cards]
    values_set = set(values_list)
    rest_cards_list = values_list
    result = []

    if len(values_set) == 6:
        for value in values_set:         
            if values_list.count(value) == 2:
                result.append(value)
                break

        rest_cards_list.remove(result[0])
        rest_cards_list.remove(result[0])
        rest_cards_list.sort(reverse=True)

        result = result + rest_cards_list    
        return result[0:4]

    else:
        return [0,0,0,0]

# Fingerprint the High Card.
def High_Card_to_fingerprint(cards):
    values = [card[1] for card in cards]
    values_set = set(values)
    rest_cards = values_set
    result = []

    if len(values_set) == 7:
        values.sort(reverse=True)
        return values[0:5]
        
    return [0,0,0,0,0]

# Combine all the fingerprints.
def cards_finger_print(cards):
    return [Straight_Flush_to_fingerprint(cards),Four_of_a_King_to_fingerprint(cards),Full_House_to_fingerprint(cards),Flush_to_fingerprint(cards),Straight_to_fingerprint(cards),Three_of_a_King_to_fingerprint(cards),Two_Pair_to_fingerprint(cards),One_Pair_to_fingerprint(cards),One_Pair_to_fingerprint(cards),High_Card_to_fingerprint(cards)]

# Compare player's cards' fingerprint and determine who is the winner. If more than 1 winner, all winner will be returned.
def compare_machine(finger_print_1,finger_print_2,finger_print_3=None,finger_print_4=None,finger_print_5=None,finger_print_6=None,finger_print_7=None,finger_print_8=None,finger_print_9=None):
    # return 1, finger_print_1 is larger
    # return 2, finger_print_2 is larger
    # return n, finger_print_n is larger
    # return 0, they are equal
    compare_list = []
    compare_list.append(finger_print_1)
    compare_list.append(finger_print_2)
    result = []

    if finger_print_3 is not None:
        compare_list.append(finger_print_3)
    if finger_print_4 is not None:
        compare_list.append(finger_print_4)
    if finger_print_5 is not None:
        compare_list.append(finger_print_5)
    if finger_print_6 is not None:
        compare_list.append(finger_print_6)
    if finger_print_7 is not None:
        compare_list.append(finger_print_7)
    if finger_print_8 is not None:
        compare_list.append(finger_print_8)
    if finger_print_9 is not None:
        compare_list.append(finger_print_9)

    player_number = len(compare_list)
    card_type = 0

    while card_type < 10:
        temp_list = []

        for player in compare_list:
            temp_list.append(player[card_type])

        if type(temp_list[0]) is int:
            max_number = max(temp_list)

            if not max_number == 0: 
                for i in range(player_number):
                    if temp_list[i] == max_number:
                        result.append(i+1)

        if not result == []:
            return result

        if not type(temp_list[0]) is int:
            max_list = max(temp_list)
            if not set(max_list) == {0}:
                for i in range(player_number):
                    if temp_list[i] == max_list:
                        result.append(i+1)

        if not result == []:
            return result

        card_type += 1

# Test
table = _get_n_cards(5)
print("Cards on the tables are: " + str(table))
player_1 = table + _two_more_card(table)
player_2 = table + _two_more_card(player_1)
player1 = card_transfer_to_value_color(player_1)
player2 = card_transfer_to_value_color(player_2)

print("Player 1's cards are" + str(player1))
print("Player 2's cards are" + str(player2))

print("The winner is Player " + str(compare_machine(cards_finger_print(player1),cards_finger_print(player2))))