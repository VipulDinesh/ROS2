import random
import math

def main():
   
    
    # # Example 1: Simulate rolling a six-sided dice
    # dice_roll = random.randint(1, 6)
    # print(f"Dice roll result: {dice_roll}")
    
    # # Example 2: Generate a list of 5 random integers between 1 and 100
    # random_integers = [random.randint(1, 100) for _ in range(5)]
    # print(f"List of random integers: {random_integers}")
    
    # Example : Calculate the distance between two points
    x1, y1 = 1, 2
    x2, y2 = 4, 6
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Distance between points ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")

if __name__ == "__main__":
    # Execute only if run as a script
    main()
