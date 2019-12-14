def switch_sp(argument):
    """
    sample number switcher for sample name

    :param argument:
    :return:
    """

    switcher = {
        1: 'E. Coli (Nutrient+)',
        2: 'Cider 4.0%',
        3: 'Cider 7.0%',
        4: 'White',
        5: 'Vinegar',
        6: 'E. Coli (Starvation)',
    }

    return switcher.get(argument, 'Invalid Time point')

