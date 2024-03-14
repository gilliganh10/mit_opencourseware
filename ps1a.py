###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
# ================================
# Part A: Transporting Space Cows
# ================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {}

    with open(filename, "r") as file:
        for line in file:
            name, weight = line.strip().split(',')
            cows[name] = int(weight)
    return cows
    pass


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # Sort the values using a lambda function
    # We use cows.items() to get the tuples in the incoming dictionary

    sorted_cows = sorted(cows.items(), key=lambda x:x[1], reverse=True)

    # Now we initialise the comparison list, and also the final destination list

    transported_cows = set() # we use a set because it is immutable and doesn't allow duplicates

    trips = []

    # Now we have a comparison list, we can loop WHILE the comparison list is shorter than the original list

    while len(transported_cows) < len(sorted_cows):

        # initialise the current trip and the weight
        current_trip = []
        weight = 0

        # loop through each cow with a for loop.
        # we use key, value to make sure we get all data from the .items() tuples
        for key, value in sorted_cows:

            # create a variable for the current cow, using the tuple
            current_cow = key, value

            if key not in transported_cows and value + weight <= limit:
                # Add the cow to the trip
                current_trip.append(current_cow)

                # add the key to the transported cows set
                transported_cows.add(key)

                # increase the weight
                weight += value
                #print(weight)
            # Add the current trip to the trips
        trips.append(current_trip)
    return trips




def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    cows = cows.items()

    cow_partitions = get_partitions(cows)

    possible_partitions = []
    impossible_partitions = []
    # Loop through each partition that we have
    i = 1
    for partition in cow_partitions:
        #print(f"Partition {i}")
        partition_possible = True
        i = i +1
        for trip in partition:
            #print(trip)
            trip_weight = 0
            for cow in trip:
                trip_weight += cow[1]
            if trip_weight > limit:
                partition_possible = False
        if partition_possible:
            possible_partitions.append(partition)
        else:
            impossible_partitions.append(partition)


    # Loop through the possible partitions and find the minimum number of trips required to transport the cows:
    minimum_trips = float('inf')
    fewest_trips = []
    for partition in possible_partitions:
        if len(partition) < minimum_trips:
            minimum_trips = len(partition)
            fewest_trips.clear()
            fewest_trips.append(partition)
    return fewest_trips


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    greedy_output = greedy_cow_transport(cows)
    end = time.time()
    print(f"Greedy output: {len(greedy_output)} trips")
    print(f"Greedy elapsed time: {(end-start)}")
    print(f"Optimal solution: {greedy_output}")

    start = time.time()
    brute_force_output = brute_force_cow_transport(cows)
    end = time.time()
    print(f"Brute force output: {len(brute_force_output)}")
    print(f"Brute force elapsed time: {(end-start)}")
    print(f"Optimal solution: {brute_force_output}")

    pass




# Load cow data
cows = load_cows("ps1_cow_data.txt")

# Run the program
compare_cow_transport_algorithms()
