from mendeleev import element
from chemparse import parse_formula
from functools import reduce


def parse_to_list(formula):
    parsed = parse_formula(formula)
    return [(elem, quantity) for elem, quantity in parsed.items()]

def parse_to_element_list(formula):
    parsed = parse_formula(formula)
    return [elem for elem, quantity in parsed.items()]

class Astra:
    def __init__(self, **kwargs):
        self.components = [parse_to_list(x) for x in kwargs["components"]]
        product_raw = reduce(lambda x, y: x+y, self.components)
        self.product_elements = set()
        for element in product_raw:
            self.product_elements.add(element[0])
        self.product = []
        for element in self.product_elements:
            sum = 0
            for pair in product_raw:
                if pair[0] == element:
                    sum += pair[1]
            self.product += [(element, sum)]
