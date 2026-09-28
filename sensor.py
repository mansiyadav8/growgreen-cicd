import random

def read_moisture():
    # Simulates a soil moisture reading percentage
    return random.randint(30, 70)

if __name__ == "__main__":
    level = read_moisture()
    print(f"GrowGreen Sensor: Current soil moisture level is {level}%.")