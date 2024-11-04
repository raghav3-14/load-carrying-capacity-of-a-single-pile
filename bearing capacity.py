import math

def pile_capacity(d, L, gamma_c, gamma_s, phi, alpha, c):
    """
    Calculate the load-carrying capacity of a single pile.

    Parameters:
    d (float): Diameter of the pile in meters.
    L (float): Length of the pile in meters.
    gamma_c (float): Unit weight of concrete in kN/m³.
    gamma_s (float): Unit weight of soil in kN/m³.
    phi (float): Angle of internal friction in degrees.
    alpha (float): Adhesion factor.
    c (float): Cohesion in kPa.

    Returns:
    float: Load-carrying capacity of the pile in kN.
    """
    A = math.pi * (d / 2)**2
    P = math.pi * d
    sigma_v = gamma_s * L
    tau = alpha * c
    Q_skin = tau * P * L
    Nq = math.exp(math.pi * math.tan(math.radians(phi))) * (math.tan(math.radians(45 + phi / 2)))**2
    Q_base = A * Nq * sigma_v
    Q_total = Q_skin + Q_base
    
    return Q_total

def number_of_piles(P_total, Q_single):
    """
    Calculate the number of piles required to support the total load.

    Parameters:
    P_total (float): Total load on the foundation in kN.
    Q_single (float): Load-carrying capacity of a single pile in kN.

    Returns:
    int: Number of piles required.
    """
    return math.ceil(P_total / Q_single)

# Manual input from the user
try:
    P_total = float(input("Enter the total load on the foundation (in kN): "))
    d = float(input("Enter the diameter of the pile (in meters): "))
    L = float(input("Enter the length of the pile (in meters): "))
    gamma_c = float(input("Enter the unit weight of concrete (in kN/m³): "))
    gamma_s = float(input("Enter the unit weight of soil (in kN/m³): "))
    phi = float(input("Enter the angle of internal friction (in degrees): "))
    alpha = float(input("Enter the adhesion factor: "))
    c = float(input("Enter the cohesion (in kPa): "))
    
    Q_single = pile_capacity(d, L, gamma_c, gamma_s, phi, alpha, c)
    num_piles = number_of_piles(P_total, Q_single)
    
    print(f"The load-carrying capacity of a single pile is: {round(Q_single, 2)} kN")
    print(f"The number of piles required is: {num_piles}")
except ValueError:
    print("Please enter valid numerical values.")
