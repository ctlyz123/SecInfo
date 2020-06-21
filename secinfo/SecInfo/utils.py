SearchClass = {}

def loadSearch(name):
    def inner(search):
        SearchClass[name] = search
        return search
    return inner
