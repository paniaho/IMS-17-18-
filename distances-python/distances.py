distances = {
    'A': 114.17,
    'B': 77.16,
    'C': 73.64,
    'D': 164.8,
    'E': 153.0,
    'F': 142.64,
    'G': 163.48,
    'H': 110,
    'CEITEC': 229.36,
    'AdMaS': 607.87,
    'FacultyOfChemistry': 125.02
}

personMinSpeed = 1.12 # m/s
personMaxSpeed = 1.39 # m/s

if __name__ == '__main__':
    for building, distance in distances.items():
        print("{}: Uniform({}, {})".format(building, personMinSpeed*distance, personMaxSpeed*distance))