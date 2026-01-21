num_1={1,2,3,4,5}
num_2={"a","b","c","d","e"}
User_Zip=zip("The combined list of the lists above are: ",num_1,num_2)
print(list(User_Zip))

User_List=[10,20,30,40,50]
User_List2=[60,70,80,90,100]
for x,y in zip(User_List,User_List2[::-1]):
    print(x,y)

stocks=["Reliance","NVDA""AAPL","TSLA"]
prices=[2200,500,150,700]
new_dict={stocks:price for stocks,
          price in zip(stocks,prices)}
print("\n{}".format(new_dict))
