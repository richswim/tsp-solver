import click

from tsp import get_project_root

from tsp.file_operations import read_delivery_points
from tsp.tsp_solver import simulated_annealing_tsp

DEFAULT_PATH = f"{get_project_root()}/delivery_points/"


@click.command()
@click.option(
    "--file", default="delivery_points.txt", help="File containing delivery points."
)
@click.option("--path", default=None, help="Path to the directory containing the file.")
def solve_tsp(file: str = None, path: str = None):
    """
    Solve the Traveling Salesman Problem (TSP) using the Simulated Annealing algorithm.

    This function reads delivery points from a specified file and path, solves the TSP
    using the Simulated Annealing algorithm, and prints the shortest route and its total distance.

    Args:
        file (str, optional): The name of the file containing delivery points. Defaults to "delivery_points.txt".
        path (str, optional): The path to the directory containing the file. Defaults to None.

    Raises:
        FileNotFoundError: If the specified file is not found in the given path.
    """
    try:
        delivery_points = read_delivery_points(
            file_name=file, path=path or DEFAULT_PATH
        )
    except FileNotFoundError as e:
        click.echo(f"ERROR: {e}")
        click.echo("INFO: Exiting the program")
        exit(1)

    # Solve the TSP using Simulated Annealing
    route, distance = simulated_annealing_tsp(delivery_points)

    _route = " -> ".join([str(point) for point in route])

    click.echo(f"Shortest Route: {_route}")
    click.echo(f"Total Distance: {distance:.2f} Units")


if __name__ == "__main__":
    solve_tsp()
