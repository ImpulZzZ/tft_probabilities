# for the function which creates the permutations
import itertools

# global constant variables:
min_level = 1
max_level = 9
min_cost = 1
max_cost = 5

# amount of champions per cost-tier, for example there are 8 different 5 cost units
champions_per_cost = [13, 13, 13, 10, 8]

# amount of champion copys in the pool: e.g. Aurelion Sol has 10 copies
champion_copys_in_pool = [29, 22, 18, 12, 10]

# probabilities of cost tiers, dependent on level
roll_probabilities = [[1.0, 0.0, 0.0, 0.0, 0.0],  # Level 1
                      [1.0, 0.0, 0.0, 0.0, 0.0],  # Level 2
                      [0.75, 0.25, 0.0, 0.0, 0.0],  # Level 3
                      [0.55, 0.30, 0.15, 0.0, 0.0],  # Level 4
                      [0.40, 0.35, 0.20, 0.05, 0.0],  # Level 5
                      [0.20, 0.40, 0.30, 0.10, 0.0],  # Level 6
                      [0.14, 0.30, 0.40, 0.15, 0.01],  # Level 7
                      [0.14, 0.20, 0.30, 0.30, 0.06],  # Level 8
                      [0.10, 0.15, 0.25, 0.35, 0.15]]  # Level 9


# the probability for one champion, dependent on cost and level
def probability_one_unit(cost, level):
    return roll_probabilities[level - 1][cost - 1] / champions_per_cost[cost - 1]


# probability of a cost-tier at a specific level
def probability_unit_per_cost(cost, level):
    return roll_probabilities[level - 1][cost - 1]


# probability that you need n rolls for a hit
def probability_hit_at_n_rolls(cost, level, n):
    p = probability_one_unit(cost, level)

    return n * p * pow(1 - p, n - 1)


# probability to hit m champions in n rolls
def probability_m_champs_with_n_rolls(cost, rolls, min_champion_hits):
    # amount of all possible outcomes
    champion_copies_of_cost_x = champions_per_cost[cost - 1] * champion_copys_in_pool[cost - 1]
    # amount of all wanted outcomes
    champion_copies_of_searched_champ = champion_copys_in_pool[cost - 1]
    # possibles sequences of hits z.B. (0 , 0 , 1, 0, 1, ...)
    possible_outcomes = list(itertools.product([0, 1], repeat=rolls))
    # the result is computed iteratively in the loop below
    total_p = 0

    # loop over every sequence
    for outcome in possible_outcomes:

        # don't consider sequences where min. amount of champs was not found
        if sum(outcome) < min_champion_hits:
            continue

        # refreshes the variables used for inner loop
        current_copies_of_all_champs = champion_copies_of_cost_x
        current_copies_of_champ = champion_copies_of_searched_champ
        path_probability = 1

        for current in outcome:

            # the current hit-probability is computed by the current amount of searched champs and all champs
            current_p = current_copies_of_champ / current_copies_of_all_champs

            # if we have a hit, we pick the champ out of the pool and add the probability to the path
            if current == 1:
                path_probability = path_probability * current_p
                current_copies_of_champ = current_copies_of_champ - 1

            # else we add the counter-probability to the path
            else:
                path_probability = path_probability * (1 - current_p)

        # iteratively computed result
        total_p = total_p + path_probability

    return total_p


# probability to hit m champions in n rolls dependent on level
def probability_m_champs_with_n_rolls_at_level(cost, rolls, min_champion_hits, level):
    # n rolls, probability that at least m champion are found
    p = probability_m_champs_with_n_rolls(cost, rolls, min_champion_hits)

    return p * roll_probabilities[level - 1][cost - 1]


def main():
    print("here comes gui")


if __name__ == "__main__":
    main()
