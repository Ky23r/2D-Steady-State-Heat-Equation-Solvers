from solvers.jacobi import jacobi
from solvers.gauss_seidel import gauss_seidel
from solvers.gauss_seidel_with_5point_sor import gauss_seidel_with_5point_sor
from solvers.gauss_seidel_with_9point_sor import gauss_seidel_with_9point_sor
from solvers.conjugate_gradient import conjugate_gradient
from utils.optimizer_for_sor_method import find_optimal_omega
from utils.convergence_visualization import plot_convergence_curves


def get_float(prompt: str, default: float = None) -> float:
    while True:
        entry = input(prompt).strip()
        if entry == "" and default is not None:
            return default
        try:
            value = float(entry)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_int(prompt: str, min_value: int = None) -> int:
    while True:
        entry = input(prompt).strip()
        try:
            value = int(entry)
            if min_value is not None and value < min_value:
                print(f"Invalid input. Please enter an integer >= {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


length_x = get_float("Enter the domain length in the x-direction: ")
length_y = get_float("Enter the domain length in the y-direction: ")

nx = get_int(
    "Enter the number of grid points along x (positive integer): ", min_value=1
)
ny = get_int(
    "Enter the number of grid points along y (positive integer): ", min_value=1
)

convergence_threshold = get_float(
    "Enter the convergence threshold [press Enter for default 1e-4]: ", default=1e-4
)

T_bottom = get_float("Enter the temperature at the bottom boundary: ")
T_top = get_float("Enter the temperature at the top boundary: ")
T_left = get_float("Enter the temperature at the left boundary: ")
T_right = get_float("Enter the temperature at the right boundary: ")

omega_for_gs_with_5point_sor = 1.97
omega_for_gs_with_9point_sor = 1.97

# omega_for_gs_with_5point_sor, _, _ = find_optimal_omega(
#     gauss_seidel_with_5point_sor,
#     length_x,
#     length_y,
#     nx,
#     ny,
#     convergence_threshold,
#     T_bottom,
#     T_top,
#     T_left,
#     T_right,
#     1,
#     2,
#     0.01,
# )

# omega_for_gs_with_9point_sor, _, _ = find_optimal_omega(
#     gauss_seidel_with_9point_sor,
#     length_x,
#     length_y,
#     nx,
#     ny,
#     convergence_threshold,
#     T_bottom,
#     T_top,
#     T_left,
#     T_right,
#     1,
#     2,
#     0.01,
# )

_, jacobi_error_history, _ = jacobi(
    length_x,
    length_y,
    nx,
    ny,
    convergence_threshold,
    T_bottom,
    T_top,
    T_left,
    T_right,
    True,
    True,
)

_, gs_error_history, _ = gauss_seidel(
    length_x,
    length_y,
    nx,
    ny,
    convergence_threshold,
    T_bottom,
    T_top,
    T_left,
    T_right,
    True,
    True,
)

_, gs_with_5point_sor_error_history, _ = gauss_seidel_with_5point_sor(
    length_x,
    length_y,
    nx,
    ny,
    convergence_threshold,
    omega_for_gs_with_5point_sor,
    T_bottom,
    T_top,
    T_left,
    T_right,
    True,
    True,
)

_, gs_with_9point_sor_error_history, _ = gauss_seidel_with_9point_sor(
    length_x,
    length_y,
    nx,
    ny,
    convergence_threshold,
    omega_for_gs_with_9point_sor,
    T_bottom,
    T_top,
    T_left,
    T_right,
    True,
    True,
)

_, cg_error_history, _ = conjugate_gradient(
    length_x,
    length_y,
    nx,
    ny,
    convergence_threshold,
    T_bottom,
    T_top,
    T_left,
    T_right,
    True,
    True,
)

plot_convergence_curves(
    jacobi_error_history,
    gs_error_history,
    gs_with_5point_sor_error_history,
    gs_with_9point_sor_error_history,
    cg_error_history,
    labels=[
        "Jacobi Iterative Method",
        "Gauss-Seidel Iterative Method",
        "Gauss-Seidel Iterative Method with 5-Point SOR",
        "Gauss-Seidel Iterative Method with 9-Point SOR",
        "Conjugate Gradient Method",
    ],
)
