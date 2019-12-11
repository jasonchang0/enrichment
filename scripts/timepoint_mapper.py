def switch_tp(argument):
    """
    time point switcher for number of hours after start of experiment

    :param argument:
    :return:
    """

    switcher = {
        0: 0.0,
        1: 2.0,
        2: 4.5,
        3: 6.0,
        4: 24.0,
        5: 26.0,
        6: 48.0,
        7: 50.5,
        8: 54.0,
        9: 148.5,
        10: 172.5
    }

    return switcher.get(argument, 'Invalid Time point')

