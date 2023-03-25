def contains(lst1, lst2):
    for x in lst1:
        flag = True
        for i in range(len(x)):
            if x[i] != lst2[i]:
                flag = False
                break
        if flag:
            return True
    return False


def delete_duplicate(lst):
    out = []
    for x in lst:
        if not contains(out, x):
            out.append(x)
    return out


def glue(first_constituent, second_constituent):
    diff = 0
    pos = -1

    for idx, (var1, var2) in enumerate(zip(first_constituent, second_constituent)):
        if diff > 1:
            break
        else:
            if var1 != var2:
                diff += 1
                pos = idx

    return first_constituent[:pos] + [2] + second_constituent[pos + 1:] if diff == 1 else None


def start_glue(constituents):
    out, final = [], []
    for i in range(len(constituents)):
        used = False
        for j in range(len(constituents)):
            glue_res = glue(constituents[i], constituents[j])
            if glue_res is not None:
                out.append(glue_res)
                used = True
        if not used:
            final.append(constituents[i])
    return out, final


def get_glued(constituents: list) -> list:
    out = []

    if not len(constituents):
        return []

    for i in range(len(constituents[0])):
        curr = start_glue(constituents)
        constituents = delete_duplicate(curr[0])
        out += curr[1]

    return out + constituents
