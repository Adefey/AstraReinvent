from nozzle_tools import Nozzle
import numpy as np


def main():
    n = Nozzle(T=3200, p=6e6, k=1.4, R=300, m=2300, rho=1.5)
    data = n.calculate_gas_params_p(np.arange(6e6, 0.1, -5e3))
    for row in data:
        for cell in row:
            print(cell, end="\t\t")
        print("", end="\n")


if __name__ == "__main__":
    main()
