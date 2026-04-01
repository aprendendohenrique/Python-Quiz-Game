def yes_no(txt):
    try:
        t = str(input(txt))
    except KeyboardInterrupt:
        return False
    if t.lower() == 'y':
        return True
    elif t.lower() == 'n':
        return False
    else:
        return None