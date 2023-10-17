from googlesearch import search


def link_with_information(name):
    obj = search(name + " характеристики", num_results=5)
    item = 0
    result = []
    while item != 5:
        result.append(next(obj))
        item+=1

    return result
