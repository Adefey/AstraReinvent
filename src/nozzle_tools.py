import math


class gas_functions:
    def gdf_T_lambda(lamb, k):
        tau = 1-lamb**2*(k-1)/(k+1)
        return tau

    def gdf_T_mach(mach, k):
        tau = 1/(1+(k-1)/2*mach**2)
        return tau

    def gdf_p_lambda(lamb, k):
        pi = (1-lamb**2*(k-1)/(k+1))**(k/(k-1))
        return pi

    def gdf_p_mach(mach, k):
        pi = (1/(1+(k-1)/2*mach**2))**(k/(k-1))
        return pi

    def gdf_eps_lambda(lamb, k):
        eps = (1-lamb**2*(k-1)/(k+1))**(1/(k-1))
        return eps

    def gdf_eps_mach(mach, k):
        eps = (1/(1+(k-1)/2*mach**2))**(1/(k-1))
        return eps

    def gas_speed_critical(R, T_chamber, k):
        w_critical = math.sqrt(2*R*T_chamber*k/(k+1))
        return w_critical

    def gas_speed(R, T_chamber, k, p, p_chamber):
        w = math.sqrt(2*R*T_chamber*k/(k-1)*(1-(p/p_chamber)**((k-1)/k)))
        return w

    def get_lambda_by_p(R, T_chamber, k, p, p_chamber):
        w_critical = gas_functions.gas_speed_critical(R, T_chamber, k)
        w = gas_functions.gas_speed(R, T_chamber, k, p, p_chamber)
        return w/w_critical

    def get_mach_by_p(R, T_chamber, k, p, p_chamber):
        lamb = gas_functions.get_lambda_by_p(R, T_chamber, k, p, p_chamber)
        T = gas_functions.gdf_T_lambda(lamb, k) * T_chamber
        a = math.sqrt(k*R*T)
        w = gas_functions.gas_speed(R, T_chamber, k, p, p_chamber)
        return w/a

    def get_q_by_p(R, T_chamber, k, p, p_chamber):
        lamb = gas_functions.get_lambda_by_p(R, T_chamber, k, p, p_chamber)
        eps = gas_functions.gdf_eps_lambda(lamb, k)
        return lamb*eps*((k+1)/2)**(1/(k-1))


class Nozzle:
    def __init__(self, **kwargs):
        self.T_chamber = kwargs["T"]
        self.p_chamber = kwargs["p"]
        self.k = kwargs["k"]
        self.R = kwargs["R"]
        self.m = kwargs["m"]
        self.rho = self.p_chamber / (self.R * self.T_chamber)

    def calculate_A_k(self):
        self.A_k = math.sqrt(self.k*(2/(self.k+1))**((self.k+1)/(self.k-1)))
        return self.A_k

    def calculate_F_critical(self):
        self.F_critical = (math.sqrt(self.R*self.T_chamber)
                           * self.m)/(self.A_k*self.p_chamber)
        return self.F_critical

    def calculate_gas_params_p(self, p_outers):
        '''Result: lambda, Mach, W, p, T, rho, q, F'''
        result = []
        A_k = self.calculate_A_k()
        F_critical = self.calculate_F_critical()
        for p in p_outers:
            lamb = gas_functions.get_lambda_by_p(
                self.R, self.T_chamber, self.k, p, self.p_chamber)
            mach = gas_functions.get_mach_by_p(
                self.R, self.T_chamber, self.k, p, self.p_chamber)
            w = gas_functions.gas_speed(
                self.R, self.T_chamber, self.k, p, self.p_chamber)
            p_a = p
            T = gas_functions.gdf_T_lambda(lamb, self.k) * self.T_chamber
            rho = gas_functions.gdf_eps_lambda(lamb, self.k) * self.rho
            F = 1/gas_functions.get_q_by_p(self.R, self.T_chamber,
                                           self.k, p, self.p_chamber)*F_critical
            result += [[lamb, mach, w, p_a, T, rho, F]]
        return result
