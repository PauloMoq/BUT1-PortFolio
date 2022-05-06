import constants
import math
import random



def createPopulation():
    '''
    Initializes the attributes of each person in the simulation    
    '''

    # list of persons
    persons = []
    # how many people can move
    movable = constants.POPULATION_SIZE * constants.MOVABLE_POPULATION_RATE
    
    for i in range(constants.POPULATION_SIZE):
        # We now calculate various properties of a person (initial position, health state,
        # time before recovery and initial movement speed)
        
        # position
        x = random.uniform(0, constants.SCENE_WIDTH)
        y = random.uniform(0, constants.SCENE_HEIGHT)

        # health state
        state = constants.HEALTHY
        # time before recovery is 0 if a person is healthy
        infectionTTL = 0 # this person is healthy
        if (i >= constants.POPULATION_SIZE - constants.INITIAL_INFECTED_POPULATION_SIZE):
            # this person is infected
            state = constants.INFECTED
            # their time before recovery is positive             
            infectionTTL = constants.INFECTION_TTL

        # the direction the person is facing, as an angle in radians
        angle = random.uniform(0, 2 * math.pi)

        # the speed this person is moving at
        # this person is not moving
        speed = 0
        if (i < movable):
            # this person is moving
            speed = random.uniform(constants.PERSON_MIN_SPEED, constants.PERSON_MAX_SPEED)
        
        # xVelocity and yVelocity are the components of this person's velocity vector 
        xVelocity = speed * math.cos(angle)
        yVelocity = speed * math.sin(angle)

        # We store this person's attributes in a list
        thisPerson = [x, y, state, infectionTTL, xVelocity, yVelocity]

        # We eventually append this person's attributes to the list of persons
        persons.append(thisPerson)
    return persons



def update(person):
    '''
    Updates a person's position and health state during a simulation tick
    '''

    # We shift each coordinate by an amount equal to the corresponding velocity component
    person[0] += person[4]
    person[1] += person[5]
        
    # if a person is outside the scene, we do two things:
    # 1/ we move them back inside the scene by correcting its coordinates
    # 2/ we make them bounce on the scene boundary, by correcting its velocity components

    # if the person is too far left
    if person[0] < 0:
        # we put them back in the scene
        person[0] = 0
        # and make it so they move in the opposite direction with respect to the x axis
        person[4] = -person[4]
    # if the person is too far right
    # we do something similar
    elif person[0] > constants.SCENE_WIDTH:
        person[0] = constants.SCENE_WIDTH
        person[4] = - person[4]

    # if the person is too far up or down
    if person[1] < 0:
        person[1] = 0
        person[5] = -person[5]
    elif person[1] > constants.SCENE_HEIGHT:
        person[1] = constants.SCENE_HEIGHT
        person[5] = -person[5]

    # If a person is infected, we decrease their time before recovery by one
    if person[2] == constants.INFECTED:
        person[3] -= 1
        # if the time before recovery is zero,
        # the person heals and becomes immune to further infection
        if person[3] == 0:
            person[2] = constants.IMMUNE



def circleCollision(c1, c2):
    '''
    Determines if two circles intersect or not
    '''
    angle = 0
    while(angle<3.1415926*2):
        # we pick a point on the first circle
        ptx = c1[0]+(math.cos(angle)*constants.PERSON_RADIUS)
        pty = c1[1]+(math.sin(angle)*constants.PERSON_RADIUS)
        # we compute the length between this point and the center of c2
        dx = ptx - c2[0]
        dy = pty - c2[1]
        d = math.sqrt(dx ** 2 + dy ** 2)
        # if this length is less than the radius of c2, then this point is inside the circle
        if d < constants.PERSON_RADIUS:
            return True
        # we then move to another point close to the previous one, until we loop around c1
        angle = angle + 0.1

    # no collision detected: c1 and c2 do not intersect
    return False


def computeCollisions(persons, personNumber):
    '''
    Computes the collisions between a population of persons and a single person
    among them, identified by their list index
    '''

    collisions = []
    p = persons[personNumber]
    for j in range (len(persons)):
        # To avoid considering collisions with themselves
        if ( j != personNumber):
            q = persons[j]
            # Test collision between the persons p and q
            if circleCollision((p[0],p[1]),(q[0],q[1])):
                collisions.append((personNumber, j))
                    
    return collisions


def processCollisions(persons, colls):
    '''
    Propagates the infection among a list of person,
    given which ones collide as a list of tuples
    '''
    for collision in colls:
        a, b = collision
        p = persons[a]
        q = persons[b]

        # if a healthy person collides with and infected person,
        # the healthy person becomes infected
        if p[2] == constants.INFECTED and q[2] == constants.HEALTHY:
            q[2] = constants.INFECTED
            q[3] = constants.INFECTION_TTL
        elif q[2] == constants.INFECTED and p[2] == constants.HEALTHY:
            p[2] = constants.INFECTED
            p[3] = constants.INFECTION_TTL


def endSimulation(persons):
    '''
    Determines if the simulation can be stopped (because nobody is infected anymore)
    '''
    immuned = 0
    for person in persons:
        if person[2] == constants.INFECTED:
            return False
        if person[2] == constants.IMMUNE:
            immuned += 1

    return True
