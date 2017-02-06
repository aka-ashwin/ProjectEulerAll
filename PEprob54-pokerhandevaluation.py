__author__ = 'Ashwin'

value_order = ["2","3","4","5","6","7","8", "9", "T", "J", "Q", "K", "A"]
card_values = range(0,13)
value_lookup_dict = dict(zip(value_order,card_values))
priorities = [0,1,2,3,4,5,6,7,8,9]
handtypes = ["high card", "pair", "two pair","three of a kind", "straight", "flush", "full house", "four of a kind", "straight flush", "royal flush"]


def getHighCard(values):
    return max(values)


def getCardCounts(values):
    countsDict = {}
    for i in range(0,len(values)):
        currval = values[i]
        if(currval in countsDict):
            countsDict[currval] += 1
        else:
            countsDict[currval] = 1

    return countsDict


def getPairsEtc(counts):
    # pairWords = ["high card", "pair", "triple", "four of a kind"]
    # hasN = [True, False, False, False]
    values_list = list(counts.values())
    keys_list = list(counts.keys())
    countsVec = sorted(counts.values())
    if(countsVec == [1,4]):
        fourofIndex = values_list.index(4)
        fourof = keys_list[fourofIndex]
        return "four of a kind", [fourof]
    elif(countsVec == [1,1,3]):
        threeofIndex = values_list.index(3)
        threeof = keys_list[threeofIndex]
        return "three of a kind", [threeof]
    elif(countsVec == [2,3]):
        threeofIndex = values_list.index(3)
        threeof = keys_list[threeofIndex]
        twoof = keys_list[1-threeofIndex]
        return "full house", [threeof, twoof]
    elif(countsVec == [1,2,2]):
        possIndices = [0,1,2]
        oneofIndex = values_list.index(1)
        del(possIndices[oneofIndex])
        pair1 = keys_list[possIndices[0]]
        pair2 = keys_list[possIndices[1]]
        pairs = [pair1,pair2]
        return "two pair", sorted(pairs)

    elif(countsVec == [1,1,1,2]):
        twoofIndex = values_list.index(2)
        twoof = keys_list[twoofIndex]
        return "pair", [twoof]


    elif(countsVec == [1,1,1,1,1]):
        return None, None


def checkFlush(suits):
    isFlush = True
    firstsuit = suits[0]
    for suit in suits[1:len(suits)]:
        if(suit != firstsuit):
            isFlush = False
            break

    return isFlush



def checkStraight(values):
    numvalues = len(values)
    sortedvalues = sorted(values)
    startPoint = sortedvalues[0]
    if(startPoint >= len(value_order) - numvalues):
        return False
    else:
        comparisonVector = card_values[startPoint:startPoint + numvalues]
        if(sortedvalues == comparisonVector):
            return True
        else:
            return False


def process_values(values):
    processed_values = []
    for val in values:
        processed_values.append(value_lookup_dict[val])
    return processed_values


def getHandEvaluation(input_values, suits):
    values = process_values(input_values)

    highcard = [getHighCard(values)]
    handEval = [highcard, None, None, None, None, None, None, None, None, None]
    handParts = [0]

    #get pairs, triples, etc.
    cardCounts = getCardCounts(values)
    pairType, pairValues = getPairsEtc(cardCounts)

    if(pairType != None):
        pairTypePriority = handtypes.index(pairType)
        handEval[pairTypePriority] = pairValues
        handParts.append(pairTypePriority)

    #check for flushes
    has_flush = checkFlush(suits)
    if(has_flush):
        handEval[5] = ["1"]
        handParts.append(5)

    #check for straights; require no pairs, so we only check for them if there are no pairs found
    if(pairType == None):
        has_straight = checkStraight(values)
        if(has_straight):
            if(has_flush):
                if(highcard == 12):
                    straight_type = "royal flush"
                else:
                    straight_type = "straight flush"
                #remove flush from hand; redundant; we'll only keep highest evaluation + ones not implied by it
                handEval[5] = None
                del(handParts[handParts.index(5)])
            else:
                straight_type = "straight"

            straight_type_index = handtypes.index("flush")
            handEval[straight_type_index] = [highcard]
            handParts.append(straight_type_index)

    handParts.sort(reverse=True)


    return handParts, handEval


def compare_elements(a0,a1):
    if(a0>a1):
        return 0
    elif(a0<a1):
        return 1
    else:
        return None


def compare_hands(hand0parts, hand0eval, hand1parts, hand1eval):
    winner = None
    curr_handpart_index = 0
    curr_sub_index = 0
    while(winner == None):
        hand0current_part = hand0parts[curr_handpart_index]
        hand1current_part = hand1parts[curr_handpart_index]

        winner = compare_elements(hand0current_part,hand1current_part)
        if(winner != None):
            break

        curr_index_for_card_values = hand0current_part

        #messy code - would be better to loop through. but for now all parts only have 1-2 elements, so I'm just doing this.
        hand0current_part_value = hand0eval[curr_index_for_card_values][curr_sub_index]
        hand1current_part_value = hand1eval[curr_index_for_card_values][curr_sub_index]

        winner = compare_elements(hand0current_part_value,hand1current_part_value)
        if(winner != None):
            break

        curr_sub_index += 1
        if(len(hand0eval[curr_handpart_index])>1):
            hand0current_part_value = hand0eval[curr_index_for_card_values][curr_sub_index]
            hand1current_part_value = hand1eval[curr_index_for_card_values][curr_sub_index]

            winner = compare_elements(hand0current_part_value,hand1current_part_value)
            if(winner != None):
                break

        curr_handpart_index += 1
        curr_sub_index = 0

    #for debugging (tracking combo counts)
    highest_combo_found_index = max(hand0parts[0],hand1parts[0])
    return winner, highest_combo_found_index

def parse_hand_into_values_and_suits(hand):
    handvals = []
    handsuits = []
    for card in hand:
        handvals.append(card[0])
        handsuits.append(card[1])

    return handvals, handsuits


def split_text_into_hands(hands_text):
    card_list = hands_text.split(" ")
    hand1 = card_list[0:5]
    hand2 = card_list[5:10]

    return hand1,hand2

def get_winner_from_line(line):
    hand1,hand2 = split_text_into_hands(line)
    print(hand1)
    hand1vals, hand1suits = parse_hand_into_values_and_suits(hand1)
    hand2vals, hand2suits = parse_hand_into_values_and_suits(hand2)

    print(hand1vals,hand1suits)

    hand1parts, hand1eval = getHandEvaluation(hand1vals, hand1suits)
    hand2parts, hand2eval = getHandEvaluation(hand2vals, hand2suits)

    #for debugging (tracking combo counts)
    winner, highest_combo = compare_hands(hand1parts,hand1eval,hand2parts, hand2eval)

    return winner, highest_combo

def loop_over_lines(line_list):
    player_0_win_count = 0
    player_1_win_count = 0
    #for debugging (tracking combo counts)
    combo_type_count = list([0]*12)
    for line in line_list:
        curr_winner, curr_highest_combo = get_winner_from_line(line)
        #for debugging (tracking combo counts)
        combo_type_count[curr_highest_combo] += 1
        if(curr_winner == 0):
            player_0_win_count += 1
        elif(curr_winner == 1):
            player_1_win_count += 1
        print(curr_winner)
    #for debugging (tracking combo counts)
    combos_list = dict(zip(handtypes,combo_type_count))
    return player_0_win_count, player_1_win_count, combos_list


hands_list_file = open("C:/Users/Ashwin/Documents/Project Euler files/p054_poker.txt", "r")

hands_list_raw = hands_list_file.read()

hands_list_split = hands_list_raw.split("\n")

wins = loop_over_lines(hands_list_split)

print(wins)

