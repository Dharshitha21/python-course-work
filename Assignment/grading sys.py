data={
    1:{'name':'Dinesh','exam status':True,'Python':100,'SQL':95,'css':98},
    2:{'name':'Shivani','exam status':True,'Python':80,'SQL':45,'css':68},
    3:{'name':'Arun','exam status':False,'Python':None,'SQL':None,'css':None},
    4:{'name':'Sushmitha','exam status':True,'Python':30,'SQL':15,'css':25},
    5:{'name':'Dharshitha','exam status':True,'Python':80,'SQL':75,'css':65},
}

for i in data.keys():
    
    print(f'{i}.{data[i]["name"]}')
stuid=int(input("Enter the student id:"))
if stuid in data:
    if data[stuid]['exam status']:
        total=(data[stuid]["Python"]+data[stuid]["SQL"]+data[stuid]["css"])/3
        if total>90:
            print(f'excellent!!!\n{data[stuid] ["name"]} got "A" grade')
        elif total>75:
            print(f'Average!!!\n{data[stuid] ["name"]} got "B" grade')
        elif total>50:
            print(f'improve better nexttime !!!\n{data[stuid] ["name"]} got "C" grade')
        elif total>35:
            print(f'Just paased!!!\n{data[stuid] ["name"]} got "D" grade')
        else:
            print(f'{data[stuid] ["name"]}-Fail, Better luck next time!!!')
    else:
        print(f"{data[stuid] ['name']}-Fail, Not attempted")
else:
    print(f"The id is not present Try Again")
            
