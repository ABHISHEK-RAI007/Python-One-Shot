cost_price = int(input("Enter the cost price:"))
selling_price = int(input("Enter the selling price:"))

# if SP is more than CP -> Profit
if(selling_price > cost_price):
    profit = selling_price - cost_price,
    print("We have made a profit of", profit)
# if SP is less than CP -> Profit
elif (selling_price < cost_price):
    loss = cost_price - selling_price
    print("We have incurred loss of", loss)
else:
    print("We have made no profit and no loss")
