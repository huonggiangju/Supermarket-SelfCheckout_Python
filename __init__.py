try: 
    file = open('products.txt', 'rt')
    lines = file.readlines()
    productList = []
    # spliting word in each line
    for line in lines:
        word = line.strip().split(",")
        # removing whitespace in single word
        barcode, productName, desc, price = [code.strip() for code in word]

        # create a new product object
        # product = Product(barcode, productName, desc, float(price))
        
        # append product code into product list
        productList.append(barcode)
        # productList.append(product)
        
    print(productList)
    file.close()
except FileNotFoundError:
    print("File can not find")