g=['pic1','pic2','pic3','pic4','pic5']
for i in range(len(g)):
    print(f'(g[i])')
#(g[i])
#(g[i])
#(g[i])
#(g[i])
#(g[i])




data={
    1:{'name':'Dinesh','exam_status':True,'python':100,'sql':95,'html':98},
    2:{'name':'Shivani','exam_status':True,'python':80,'sql':45,'html':68},
    3:{'name':'Arun','exam_status':False,'python':None,'sql':None,'html':None},
    4:{'name':'Sushmitha','exam_status':True,'python':30,'sql':15,'html':25},
    5:{'name':'Dharshitha','exam_status':True,'python':80,'sql':75,'html':65},
}
for i in data.keys() :
    print(f'{i}.{data[i]["name"]}')
    stuid=int(input("Enter the student id:"))
    if stuid in data:
        if data[stuid]["exam_status"]:
            total=(data[stuid]["python"]+data[stuid]["sql"]+data[stuid]["html"])/3
            if total>90:
                print(f'Congrats!!!\n{data[stuid]["name"]}got "A" grade')
            elif total>75:
                print(f'Good!!!\n{data[stuid]["name"]}got "B" grade')
            elif total>50:
                print(f'Need improvement!!!\n{data[stuid]["name"]}got "C" grade')
            elif total>35:
                print(f'Just Passed!!!\n{data[stuid]["name"]}got "D" grade')
            else:
                print(f'{data[stuid]["name"]}-Fail,Better luck next time!!!')
        else:
            print(f"{data[stuid]["name"]}is not attempted the exam")
    else:
        print("The id is not present.Try Again")
        #1.Dinesh Enter the student id:1 Congrats!!! Dineshgot "A" grade
        #2.Shivani Enter the student id:2 Need improvement!!! Shivanigot "C" grade
        #3.Arun Enter the student id:3 Arunis not attempted the exam
        #4.Sushmitha Enter the student id:4 Sushmitha-Fail,Better luck next time!!!
        #5.Dharshitha Enter the student id:5 Need improvement!!! Dharshithagot "C" grade
         #command not found: 6






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
        