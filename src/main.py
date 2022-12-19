from nozzle_tools import Nozzle
import numpy as np
import pandas as pd


def main():
    n = Nozzle(T=3710.19, p=7.78e6, k=1.20693, R=339.251, m=2335.23)
    data = n.calculate_gas_params_p(
        np.array([7.7, 7.1, 6.5, 5.9, 4.4, 3.8, 2.2, 1.6, 1.0, 0.4, 0.05])*1e6)
    df = pd.DataFrame(data, columns=[
                      "lambda", "Mach", "w, m/s", "p, Pa", "T, K", "rho, kg/m^3", "F, m^2"])
    print(df)
    print(f"{n.F_critical=}m^2")
    df.to_csv("data.csv")


if __name__ == "__main__":
    main()
