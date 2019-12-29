def percentage(score):
    full = 40
    return (score / full) * 100


def check(score):
    value = percentage(score)
    print(value)
    if value <= 39:
        answer = "ndst"
    elif value <= 49:
        answer = "dop"
    elif value <= 69:
        answer = "dst"
    elif value <= 84:
        answer = "db"
    elif value <= 99:
        answer = "bdb"
    else:
        answer = "cel"
    print(answer)


check(39)
