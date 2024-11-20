import math
import random

from tsp.file_operations import read_delivery_points


def get_euclidean_distance(
    point1: tuple[float, float], point2: tuple[float, float]
) -> float:
    """
    Calculate the Euclidean distance between two points.
    d = √((x2 - x1)² + (y2 - y1)²)

    Args:
        point1 (tuple[float, float]): The first point as a tuple of (x, y) coordinates.
        point2 (tuple[float, float]): The second point as a tuple of (x, y) coordinates.

    Returns:
        float: The Euclidean distance between the two points.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def get_total_distance(route: list[tuple[float, float]]) -> float:
    """
    Calculate the total distance of a given route.

    The total distance is calculated by summing the Euclidean distances
    between consecutive points in the route, and then adding the distance
    from the last point back to the first point to complete the loop.

    Args:
        route (list[tuple[float, float]]): A list of tuples, each containing
        the x and y coordinates of a point in the route.

    Returns:
        float: The total distance of the route.
    """

    # Calculate the total distance of the route
    distance = sum(
        get_euclidean_distance(route[i], route[i + 1]) for i in range(len(route) - 1)
    )

    # Return to the starting point to complete the loop
    distance += get_euclidean_distance(route[-1], route[0])

    return distance


def get_neighbor(route: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """
    Generate a neighboring solution by swapping two points in the route.

    Args:
        route (list[tuple[float, float]]): The current route as a list of tuples,
        each containing the x and y coordinates of a point.

    Returns:
        list[tuple[float, float]]: A new route with two points swapped.
    """
    # Create a copy of the whole route
    new_route = route[:]

    # Choose two random indices to swap
    i, j = random.sample(range(len(route)), 2)

    # Swap the two points
    new_route[i], new_route[j] = new_route[j], new_route[i]

    return new_route


def simulated_annealing_tsp(
    points: list[tuple[float, float]],
    initial_temperature: int = 1000,
    cooling_rate: float = 0.995,
    min_temperature: float = 1e-3,
) -> tuple[list[tuple[float, float]], float]:
    """
    Solve the Traveling Salesman Problem (TSP) using the Simulated Annealing algorithm.

    Args:
        points (list[tuple[float, float]]): A list of tuples, each containing the x and y coordinates of a delivery point.
        initial_temperature (int): The initial temperature for the annealing process. Defaults to 1000.
        cooling_rate (float): The rate at which the temperature decreases. Defaults to 0.995.
        min_temperature (float): The minimum temperature at which the annealing process stops. Defaults to 1e-3.

    Returns:
        tuple[list[tuple[float, float]], float]: A tuple containing the best route found and its total distance.
    """

    # Start with a random initial route
    current_route = points[:]
    random.shuffle(current_route)
    current_distance = get_total_distance(current_route)

    # Initialize the best route and distance
    best_route = current_route[:]
    best_distance = current_distance

    # Initialize the temperature
    temperature = initial_temperature

    # Simulated Annealing loop
    while temperature > min_temperature:
        # Generate a neighboring solution
        neighbor_route = get_neighbor(current_route)
        neighbor_distance = get_total_distance(neighbor_route)

        # Determine if the neighbor should be accepted
        if neighbor_distance < current_distance or random.random() < math.exp(
            (current_distance - neighbor_distance) / temperature
        ):
            current_route = neighbor_route
            current_distance = neighbor_distance

            # Update the best solution if applicable
            if current_distance < best_distance:
                best_route = current_route[:]
                best_distance = current_distance

        # Decrease the temperature
        temperature *= cooling_rate

    return best_route, best_distance


# def solve_tsp():
#     # Read delivery points from the file
#     delivery_points = read_delivery_points()
#     # Solve the TSP using Simulated Annealing
#     route, distance = simulated_annealing_tsp(delivery_points)
#
#     return route, distance
