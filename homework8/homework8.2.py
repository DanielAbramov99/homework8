import statistics

player_height: list[float] = []
stop: int = -999
tall_than_2: int = 0
bigger_than_avg: int = 0
while True:
    enter_height: float = float(input("enter player height:"))
    if enter_height == stop:
        break
    if not 1.60 <= enter_height <= 3:
        continue
    player_height.append(enter_height)
    if enter_height > 2:
        tall_than_2 += 1
if len(player_height) > 0:
    print(player_height)
    print(f"the amount of players is:{len(player_height)}")
    print(f"the tallest player is:{max(player_height)}")
    print(f"the shortest player is:{min(player_height)}")
    print(f"the average height of the players is:{statistics.mean(player_height)}")
    print(f"the amount of player taller than 2 meters is:{tall_than_2}")
length = len(player_height)
for i in range(length):
    if player_height[i] > statistics.mean(player_height):
        bigger_than_avg += 1

print(f"the amount of players that have above average height in this roster is:{bigger_than_avg}")
