import random
from collections import Counter

'''
An Australian powerball simulator that emulate the outcomes and earnings
'''


# https://australia.national-lottery.com/powerball/dividends
winning_patterns={
    '7+1':('Division 1',23_199_104.77),
    '7+0':('Division 2',126_166.43),
    '6+1':('Division 3',5323.70),
    '6+0':('Division 4',455.18),
    '5+1':('Division 5',158.46),
    '4+1':('Division 6',70.89),
    '5+0':('Division 7',42.23),
    '3+1':('Division 8',17.58),
    '2+1':('Division 9',10.72)
}


# core function to generate 7+1 combo
def generate_one_combo(total_balls=8):
    regular_ball=list(range(1,35))
    power_ball=list(range(1,21))
    run=True
    combo=[]
    while run:
        # generate regular ball
        if len(combo)<total_balls-1:
            pick=random.choice(regular_ball)
            if pick not in combo:
                combo.append(pick)
        else:
            run=False
    
    # sort regular balls
    combo.sort()
    # generate powerball
    combo.append(random.choice(power_ball))
    return combo

# core function to distinguish winning patterns
def check_winning_pattern(winning_combo,candidate):
    regular_match=0
    powerball=0
    # first compare powerball
    powerball = 1 if winning_combo[-1]==candidate[-1] else 0

    # then compare regular ball
    regular_match=len(set(winning_combo[:-1]).intersection(candidate[:-1]))

    return f"{regular_match}+{powerball}"



# check player's winning pattern
def outcome_analyzer(winning_combo, player_combo):
    all_winnings=[]
    total_prize=0
    for candidate in player_combo:
        win=winning_patterns.get(check_winning_pattern(winning_combo,candidate))
        if win:
            # append to all_winnings
            all_winnings.append(win[0])
            # accumulate total prize
            total_prize+=win[-1]
            # print(f"Won {win[0]} on {candidate} with prize of ${win[-1]:.2f}, total winning: ${total_prize:.2f}")

    return Counter(all_winnings), total_prize



if __name__=='__main__':
    # set initial params
    total_play=10000
    cost_per_play=4.85/4

    # initialize winning combo
    winning_combo=generate_one_combo()
    print(f"Winning combo is {winning_combo}")

    # initialize player's combo
    player_combo=[]
    for _ in range(total_play):
        one_play=generate_one_combo()
        if one_play not in player_combo:
            player_combo.append(one_play)
    # print(f"player_combo: {player_combo}")

    # display outcome
    counter, total_prize = outcome_analyzer(winning_combo,player_combo)
    print(counter)
    print(f"After {total_play} plays, ${total_play*cost_per_play:,.2f} was spent, ${total_prize:,.2f} was earned, \
net profit/loss is ${(total_prize-total_play*cost_per_play):,.2f}")

