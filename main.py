import itertools

# Globale Variablen:
# Die Anzahl von Champions je Kostenstufe, z.B. 8 unterschiedliche Legendäre
champions_per_cost = [13, 13, 13, 10, 8]

# Anzahl der Kopien eines Champs im Pool: Aurelion Sol mit 10 Kopien im Pool
champion_copys_in_pool = [29, 22, 18, 12, 10]

# Wahrscheinlichkeiten der einzelnen Stufen wobei [1, 0] W'keit auf Level 2 für 1 Cost
roll_probabilities = [[1.0, 0.0, 0.0, 0.0, 0.0],  # Level 1
                      [1.0, 0.0, 0.0, 0.0, 0.0],  # Level 2
                      [0.75, 0.25, 0.0, 0.0, 0.0],  # Level 3
                      [0.55, 0.30, 0.15, 0.0, 0.0],  # Level 4
                      [0.40, 0.35, 0.20, 0.05, 0.0],  # Level 5
                      [0.20, 0.40, 0.30, 0.10, 0.0],  # Level 6
                      [0.14, 0.30, 0.40, 0.15, 0.01],  # Level 7
                      [0.14, 0.20, 0.30, 0.30, 0.06],  # Level 8
                      [0.10, 0.15, 0.25, 0.35, 0.15]]  # Level 9

# Anzahl der Kostenstufen
cost_levels = 5


def faculty(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def binomial_coefficient(n, k):
    return faculty(n) / (faculty(k) * faculty(n - k))


def probability_one_unit(cost, level):
    return roll_probabilities[level - 1][cost - 1] / champions_per_cost[cost - 1]


def probability_unit_per_cost(cost, level):
    return roll_probabilities[level - 1][cost - 1]


def probability_hit_at_n_rolls(cost, level, n):
    p = probability_one_unit(cost, level)

    return n * p * pow(1 - p, n - 1)


def probability_m_hits_at_n_rolls(cost, level, n, m):
    p = 0
    champion_hits = m
    rolls_left = n
    while rolls_left > 0:
        p = p + probability_hit_at_n_rolls(cost, level, n)

        rolls_left = rolls_left - 1
        champion_hits = champion_hits - 1


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


def probability_m_champs_with_n_rolls_at_level(cost, rolls, min_champion_hits, level):
    # n rolls, probability that at least m champion are found
    p = probability_m_champs_with_n_rolls(cost, rolls, min_champion_hits)

    return p * roll_probabilities[level - 1][cost - 1]


def main():
    # Aktuell betrachtete Kostenstufe
    current_cost = 1

    # Aktuell betrachtetes Level
    current_level = 1


if __name__ == "__main__":
    main()
