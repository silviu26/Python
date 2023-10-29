
def ex1(a,b):
    return [set(a) & set(b), set(a) | set(b), set(a)-set(b), set(b)-set(a)]

#print(ex1([1,2,3],[3,4,5]))

def ex2(sir):
    dictionar={}
    for ch in sir:
        if ch==' ':
            continue
        if ch in dictionar:
            dictionar[ch]+=1
        else:
            dictionar[ch]=1
    return dictionar

#print(ex2("Ana has apples"))

def ex3(dict1, dict2):
    
    if isinstance(dict1, dict) and isinstance(dict2, dict):
       
        if set(dict1.keys()) != set(dict2.keys()):
            return False
       
        for key in dict1:
            if not ex3(dict1[key], dict2[key]):
                return False
        return True
    
    else:
        return dict1 == dict2

#print(ex3({'a': 1, 'b': [1, 2, 3], 'c': {'x': 1, 'y': 2}}, {'a': 1, 'b': [1, 2, 3], 'c': {'x': 1, 'y': 2}}))

#ex4
def build_xml_element(tag, content, **kwey_value):
    xml_element = "<"+tag+" "

    for key, value in kwey_value.items():
        xml_element += key +"="+ "\""+ value +"\" "


    xml_element += ">" + content + "</"+tag+">"

    return xml_element


#print( build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))

def ex5(reguli,dictionar):
    
    for key,pre,mij,suf in reguli:
        if dictionar.get(key) == None:
            return False
        
        valoare=dictionar[key]
        if valoare[:len(pre)] != pre:
            return False
        a=valoare[len(valoare)-len(suf):]
        if valoare[len(valoare)-len(suf):]!= suf:
            return False
        
        if valoare.find(mij)==0 or valoare.find(mij)==len(valoare)-len(suf):
            return False
        
    return True

s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} 

#print(ex5(s, d))

def ex6(lista):
    unic=0
    la_fel=0
    lista_sort=sorted(lista)

    ok=True
    for i in range(len(lista_sort)-1):
        if lista_sort[i]==lista_sort[i+1]:
            if ok:
                ok=False
                la_fel+=1
        else:
            if ok:
                unic+=1
            else:
                ok=True
    if ok:
        unic+=1
    return (unic,la_fel)        
            
#print(ex6([1,2,3,4,5,1,7,8,4,3,8,1,8,9,1]))


def ex7(*var):
    dictionar={}
    for i in range(len(var)-1):
        for j in range(i+1,len(var)):
            key1=""+ str(set(var[i]))+"|" +str(set(var[j]))
            dictionar[key1]= set(var[i]) | set(var[j])
            key1=""+ str(set(var[i]))+"&" +str(set(var[j]))
            dictionar[key1]= set(var[i]) & set(var[j])
            key1=""+ str(set(var[i]))+"-" +str(set(var[j]))
            dictionar[key1]= set(var[i]) - set(var[j])
            key1=""+ str(set(var[j]))+"-" +str(set(var[i]))
            dictionar[key1]= set(var[j]) - set(var[i])
    return dictionar

#print(ex7([1,2],[2,3]))


def ex8(mapping):
    rezultat=[]
    curent=mapping['start']
    while mapping[curent] not in rezultat:
        rezultat.append(curent)
        curent=mapping[curent]
    return rezultat

#print(ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

def ex9(*arg,**key_value):
    nr=0
    for a in arg:
        if a in [value for _,value in key_value.items()]:
            nr+=1
    return nr

#print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))