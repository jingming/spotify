
UNSET = 'UNSET'


def of(values):
    return {k: v for k, v in values.items() if v != UNSET}
