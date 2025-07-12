data= {

    1:{'name':'Rice','Price':60},
    2:{'name':'Wheat Flour','Price':45},
    3:{'name':'Sugar','Price':40},
    4:{'name':'Milk','Price':25},
    5:{'name':'Egg(12 pcs)','Price':70},
    6:{'name':'Cooking Oil','Price':130}, 
    7:{'name':'Tea Powder','Price':90},
    8:{'name':'Salt','Price':20},
    9:{'name':'Bread','Price':30},
    10:{'name':'Soap','Price':50},      
}
for i in range(1,11) :
    print(f'{i}. {(data[i]["name"]).ljust(15," ")}:{data[i]["price"]}')


items=list(map(int,input("Enter the item index: ").split()))
print(items)

total=0
ids=set()
for i in items:
    if i not in ids:
        co=items.count(i)
        total+=(data[i]["price"]*co)
        print(f'{data[i]["name"]}-{co}*{data[i]["price"]} = {data[i]["price"]}')
        ids.add(i)
        print("Total Bill:",total)