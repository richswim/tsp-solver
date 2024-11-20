"""Tests for the delivery points module."""

from tsp import get_project_root
from tsp.file_operations import read_delivery_points

BASE_PATH = get_project_root()

DELIVERY_POINTS_FILE_PATH = f"{BASE_PATH}/tests/test_data/"


def test_read_delivery_points():
    delivery_points = read_delivery_points(path=DELIVERY_POINTS_FILE_PATH)
    assert len(delivery_points) == 3
