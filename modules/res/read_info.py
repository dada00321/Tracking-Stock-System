def read():
    inf = []
    with open('modules//res//info.txt',encoding='cp950') as fp:
        data = fp.readlines()
        inf.append(data[0].rstrip())
        inf.append(data[1])
    
    with open('modules//res//info3.txt') as fp:
        inf[1]+=fp.readline().strip()  
    with open('modules//res//info2.txt') as fp:
        inf[1]+=fp.readline().strip()  
    return tuple(inf)
