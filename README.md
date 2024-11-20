# Traveling Salesman Problem (TSP) Solver

This project provides a solution to the Traveling Salesman Problem (TSP) using the Simulated Annealing algorithm. The project includes modules for reading delivery points from a file, calculating distances, and solving the TSP.

## Prerequisites

- Python 3.8 or higher
- `pip` for managing Python packages

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/richswim/tsp-solver.git
    cd tsp-solver
    ```

2. Install the required packages:
    ```sh
    pipenv install
    ```

## Usage

### Command Line Interface

You can use the provided CLI to solve the TSP with your delivery points.

1. Navigate to the project directory:
    ```sh
    cd tsp-solver
    ```

2. Run the CLI command:
    ```sh
    python -m tsp.tsp_click --file delivery_points.txt --path /path/to/directory
    ```

### Example

To solve the TSP using the default delivery points file located in the default directory:
```sh
python -m tsp.tsp_click
```

### Testing

Unit tests are provided to ensure the correctness of the implementation. To run the tests, use `pytest`:

1. Navigate to the project directory:
    ```sh
    cd tsp-solver
    ```

2. Run the tests:
    ```sh
    pytest
    ```

## Project Structure

- `tsp/`: Contains the main modules for the TSP solver.
  - `__init__.py`: Initializes the `tsp` package.
  - `file_operations.py`: Functions for reading delivery points from a file.
  - `tsp_solver.py`: Functions for calculating distances and solving the TSP.
  - `tsp_click.py`: CLI for solving the TSP.
- `tests/`: Contains unit tests for the project.
  - `unit/`: Unit tests for individual modules.
  - `test_data/`: Test data files.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.