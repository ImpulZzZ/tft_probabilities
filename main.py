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


def probability_one_unit(cost, level):
    return roll_probabilities[level - 1][cost - 1] / champions_per_cost[cost - 1]


def main():
    # Aktuell betrachtete Kostenstufe
    current_cost = 5

    # Aktuell betrachtetes Level
    current_level = 8

    print(probability_one_unit(current_cost, current_level))


if __name__ == "__main__":
    main()
