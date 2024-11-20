from tsp import get_project_root

DELIVERY_POINTS_PATH = f"{get_project_root()}/delivery_points/"
FILE_NAME = "delivery_points.txt"


# Function to read delivery points from the file
def read_delivery_points(
    file_name: str = FILE_NAME, path: str = DELIVERY_POINTS_PATH
) -> list[tuple[float, float]]:
    """
    Reads delivery points from a specified file.

    Args:
        file_name (str): The name of the file containing delivery points. Defaults to 'delivery_points.txt'.
        path (str): The path to the directory containing the file. Defaults to the DELIVERY_POINTS_PATH.

    Returns:
        list[tuple[float, float]]: A list of tuples, each containing the x and y coordinates of a delivery point.
    """
    points = []
    with open(f"{path}{file_name}", "r") as file:
        for line in file:
            x, y = map(float, line.strip().split(","))
            points.append((x, y))
    return points
