def organizeOrder(order):
    identifier, content = order.split(":")

    organized = {"id" : identifier,
                 "items" : list()}

    for item in content.split("|"):
        item_name, tmp = item.split(",")
        have, need = map(int, tmp.split("/"))
        organized["items"].append({"name" : item_name,
                                   "have" : have,
                                   "need" : need})

    return organized

def deorganizeOrder(order):
    deorganized = order["id"] + ':'
    for item in order["items"]:
        deorganized += (item["name"] + "," + str(item["have"]) + "/" + str(item["need"]) + "|")
    return deorganized[:-1]

def isReady(order):
    for product in order["items"]:
        if product["have"] < product["need"]:
            return False
    return True

def askForSupply(order, provider):
    for product in order["items"]:
        left = product["need"] - product["have"]
        if left > 0:
            provider.supply(product["name"], left)
