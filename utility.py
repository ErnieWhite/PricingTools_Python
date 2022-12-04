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
