import click

from tsp import get_project_root

from tsp.file_operations import read_delivery_points
from tsp.tsp_solver import simulated_annealing_tsp


@click.command()
@click.option(
    "--file", default="delivery_points.txt", help="File containing delivery points."
)
@click.option("--path", default=None, help="Path to the directory containing the file.")
def solve_tsp(file: str = None, path: str = None):
    # Read delivery points from the file
    if file and path:
        delivery_points = read_delivery_points(file_name=file, path=path)
    elif file:
        click.echo(
            "Path not provided, trying to run with defaults,"
            "make sure the file to be process is in the default directory"
        )
        click.echo(f"Default Directory: {get_project_root()}")
        delivery_points = read_delivery_points(file_name=file)
    else:
        click.echo(
            "File and Path not provided, we will process the file in the default directory"
        )
        click.echo(f"Default Directory: {get_project_root()}")
        delivery_points = read_delivery_points()
    # Solve the TSP using Simulated Annealing
    route, distance = simulated_annealing_tsp(delivery_points)

    click.echo(f"Shortest Route: {route}")
    click.echo(f"Total Distance: {distance}")


if __name__ == "__main__":
    solve_tsp()
