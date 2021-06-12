def reverse_reversed(items):
    if type(items) != list:
        return items
    else:
        res = []
        for e in items:
            item = reverse_reversed(e)
            res.append(item)

        res.reverse()
        return res
