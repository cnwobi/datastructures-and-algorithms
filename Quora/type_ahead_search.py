from functools import cmp_to_key


def typeaheadSearch(queries):
    db = {}
    result = []
    for query in queries:
        if query[0] == 'ADD':
            add(query, db)
        if query[0] == 'QUERY':
            query_db(db, query[2], result, query[1])
        if query[0] == 'DEL':
            delete(db, query[1])
    return result


def delete(db, key):
    if key in db: del db[key]


def add(entry, db):
    db[entry[2]] = entry


def takeSecond(elem):
    return elem[1]


def compare(item1, item2):
    if item1[0] > item2[0]:
        return -1
    if item1[0] < item2[0]:
        return 1
    if item1[2] < item2[2]:
        return 1
    if item1[2] > item2[2]:
        return -1


def query_db(db, token, result, limit):
    collection = []
    index = 0
    for key, value in db.items():
        words = token.lower().split(" ")
        append = False
        for word in words:
            append = word in value[4].lower()
            if not append:
                break
        if append:
            collection.append([value[3], key, index])
            index += 1

    transformed = list(map(takeSecond, sorted(collection, key=cmp_to_key(compare))))

    result.append(transformed[0:int(limit)])
