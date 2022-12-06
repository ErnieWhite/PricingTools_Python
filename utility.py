def calculate_multiplier(formula: str) -> float:
    """
    Converts a string formula to a float multiplier

    :param formula:
    :return:
    :raises ValueError: when the formula cannot be converted into a multiplier
    """
    # if the formula is left blank it defaults to *1
    if formula == '':
        formula = '*1'

    formula = formula.upper()

    # discount formula
    if formula[0] in '+-':
        return 1 + float(formula) / 100

    # markup formula
    if formula[0] == 'D':
        return 1 / float(formula[1:])

    # gross profit formula
    if formula.startswith('GP'):
        number = float(formula[2:])
        # GP100 is not a valid formula in eclipse
        if number > 99.99:
            raise ValueError(f'GP Formulas must be below 100: {formula}')
        multiplier = 1 / (1 - float(formula[2:]) / 100)
        return multiplier

    # multiplier formula
    if formula[0] in '*X':
        return float(formula[1:])

    raise ValueError(f'{formula} is not a valid formula')


def find_multiplier_formula(multiplier):

    return f'*{multiplier:.6}'


def find_markup_formula(multiplier):
    return f'D{1/multiplier:.6}'


def find_discount_formula(multiplier):
    return f'{(multiplier - 1)*100:+.6}'


def find_gross_profit_formula(multiplier):
    return f'GP{(1-1/multiplier) * 100:.6}'


def valid_formula(formula):
    if formula == '':
        return True

