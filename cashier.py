pricebeforetax= int(input("enter the price before tax of the product: "))
category = input("enter the category of the product, A, B or C: ")

if category == "A" :
    priceaftertax = (pricebeforetax*0.07) + pricebeforetax
    print(priceaftertax)
elif category == "B" :
    priceaftertax = (pricebeforetax*0.2) + pricebeforetax
    print(priceaftertax)
elif category == "C" :
    priceaftertax = (pricebeforetax*0.25) + pricebeforetax
    print(priceaftertax)