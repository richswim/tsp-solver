"""
Unit tests for the tsp_solver module.
All test is based on the Euclidean distance between points.
Delivery points are read from a file and used to test the TSP solver.
The points are generated with the function:
    y=4/3*x which is a linear function for easy testing.
"""
import pytest
from file_operations import read_delivery_points
from tsp import get_project_root

from tsp.tsp_solver import (
    get_euclidean_distance,
    get_total_distance,
    simulated_annealing_tsp,
)

BASE_PATH = get_project_root()

DELIVERY_POINTS_FILE_PATH = f"{BASE_PATH}/tests/test_data/"


@pytest.fixture
def delivery_points():
    return read_delivery_points(path=DELIVERY_POINTS_FILE_PATH)


def test_calculate_distance(delivery_points):
    point1 = delivery_points[0]
    point2 = delivery_points[1]
    assert get_euclidean_distance(point1, point2) == 5


def test_total_distance(delivery_points):
    # Test the total distance calculation for a given route, out and back
    assert get_total_distance(delivery_points) == 10 * 2


def test_solve_tsp(delivery_points):
    # Test the TSP solver on a small set of delivery points
    route, distance = simulated_annealing_tsp(delivery_points)
    assert len(route) == 3
    assert distance == 20
