coastprice=[80,90,100,120,150]
sellingprice=[85,74,95,140,180]
e=zip(coastprice,sellingprice)
for coastprice,sellingprice in e:
    if coastprice>sellingprice:
        print("totalloss:",coastprice-sellingprice)
    elif coastprice<sellingprice:
        print("totalprofit:", sellingprice-coastprice)



