# Size of the application
SCENE_WIDTH = 1000
SCENE_HEIGHT = 800

# Colors of circles
PALETTE = [(50, 50, 50), (220, 25, 0), (10, 200, 35)]
# Background color
BACKGROUND_COLOR = (220, 220, 220)

# Radius of the circle representing a person
PERSON_RADIUS = 8

# Seed - pick a fixed value to always have the same simulation
SEED = None

# constants for health state
HEALTHY = 0
INFECTED = 1
IMMUNE = 2

# Min and max speed of a person
PERSON_MIN_SPEED = 1.0
PERSON_MAX_SPEED = 2.5

# Number of persons infected at the beginning of the simulation
INITIAL_INFECTED_POPULATION_SIZE = 1

# number of rendered frames before a person recovers from an infection
INFECTION_TTL = 600

# Number of persons in the scene and moving population ratio
POPULATION_SIZE = 100
MOVABLE_POPULATION_RATE = 1
