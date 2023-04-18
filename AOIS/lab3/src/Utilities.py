def print_normal_forms(normal_forms):
    try:
        return '\n'.join([x[0] + ': ' + x[1] for x in normal_forms])
    except TypeError:
        return '\n'.join([x[0] + ':\n' + x[1].get_string() for x in normal_forms])
