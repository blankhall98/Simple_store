import csv

def product_reader(path):
    f = open(path)
    products = csv.reader(f,dialect=...)
    headers = next(products) #headers
    products = [x for x in products]
    categories = []
    for product in products:
        categories.append(product[1])
    categories = set(categories)
    token = {}
    for category in categories:
        token[category] = []
        for product in products:
            if product[1] == category:
                prod = {}
                for i in range(1,len(headers)):
                    prod[headers[i]] = product[i]
                token[category].append(prod)    
    return token

