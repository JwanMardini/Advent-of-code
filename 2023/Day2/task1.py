RED = 12
GREEN = 13
BLUE = 14
FILE_PATH = "2023/Day2/data.txt"


def parse_game_data(file_path):
    game_data = []

    with open(FILE_PATH, 'r') as file:
        for line in file:
            parts = line.strip().split(': ')
            game_id = int(parts[0].split()[1])  # Extract the game ID
            rounds = [round.split(', ') for round in parts[1].split('; ')]
            game_data.append((game_id, rounds))

    return game_data


def analyze_games(game_data, red_cubes, green_cubes, blue_cubes):
    possible_games = []

    for game in game_data:
        game_id, rounds = game[0], game[1]
        possible = True

        for round in rounds:
            red_count = sum([int(x.split()[0]) for x in round if 'red' in x])
            green_count = sum([int(x.split()[0]) for x in round if 'green' in x])
            blue_count = sum([int(x.split()[0]) for x in round if 'blue' in x])

            if red_count > red_cubes or green_count > green_cubes or blue_count > blue_cubes:
                possible = False
                break

        if possible:
            possible_games.append(game_id)

    return sum(possible_games)


# Number of cubes in the bag
red_cubes = 12
green_cubes = 13
blue_cubes = 14

# Parse the game data from file
game_data = parse_game_data(FILE_PATH)

# Analyze the games and calculate the sum of IDs
sum_of_ids = analyze_games(game_data, red_cubes, green_cubes, blue_cubes)
print(sum_of_ids)
