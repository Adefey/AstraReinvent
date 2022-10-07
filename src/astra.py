from mendeleev import element
from chemparse import parse_formula

known_valences = {
    element("H"): 1,
    element("C"): 4,
    element("N"): 0,
    element("O"): -2,
}


class ChemicalCompound:
    def __init__(self, formulas: list[str]):
        self.formula = ""
        self.elements = {}  # {element : count, ... }
        for formula in formulas:
            self.formula += f"{formula} "
            parsed = parse_formula(formula)
            for key, value in parsed.items():
                elem = element(key)
                elem.oxidation_states = known_valences[elem]
                if elem in self.elements:
                    self.elements[elem] += value
                else:
                    self.elements[elem] = value

    def __iter__(self):
        return iter(self.elements.items())

    def __str__(self):
        return "".join(
            [
                f"{key.symbol}_{str(value)}{{{key.oxidation_states}}}"
                for key, value in self.elements.items()
            ]
        )


class Astra:
    def __init__(self, **kwargs):
        self.oxidizer = ChemicalCompound(kwargs["oxidizer"])
        self.fuel = ChemicalCompound(kwargs["fuel"])
        self.__k_0 = 0

    def __str__(self):
        return f"{self.oxidizer} + {self.fuel}"

    def k_0(self):
        k_0_nom = 0
        for key_value_pair in self.fuel:
            k_0_nom += key_value_pair[0].oxidation_states * key_value_pair[1]

        k_0_denom = 0
        for key_value_pair in self.oxidizer:
            k_0_denom += key_value_pair[0].oxidation_states * key_value_pair[1]

        m_fuel = 0
        for key_value_pair in self.fuel:
            m_fuel += key_value_pair[0].atomic_weight * key_value_pair[1]

        m_oxidizer = 0
        for key_value_pair in self.oxidizer:
            m_oxidizer += key_value_pair[0].atomic_weight * key_value_pair[1]

        self.__k_0 = -m_oxidizer / m_fuel * k_0_nom / k_0_denom
        return self.__k_0
