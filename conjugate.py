def verbAR():
    print(">>>>")
    ll=[]
    ll.append(verb)
    ll.append(stem+"ando")
    ll.append(stem+"ado")
    print(*ll)
    
    ll=[]
    ll.append(stem+"o")
    ll.append(stem+"as")
    ll.append(stem+"a")
    ll.append(stem+"amos")
    ll.append(stem+"ásh")
    ll.append(stem+"an")
    print(*ll)

    ll=[]
    ll.append(stem+"í")
    ll.append(stem+"ates")
    ll.append(stem+"ó")
    ll.append(stem+"imos")
    ll.append(stem+"atesh")
    ll.append(stem+"aron")
    print(*ll)

    ll=[]
    ll.append(stem+"ava")
    ll.append(stem+"avas")
    ll.append(stem+"ava")
    ll.append(stem+"ávamos")
    ll.append(stem+"avash")
    ll.append(stem+"avan")
    print(*ll)

    ll=[]
    ll.append(stem+"aré")
    ll.append(stem+"arás")
    ll.append(stem+"ará")
    ll.append(stem+"aremos")
    ll.append(stem+"arésh")
    ll.append(stem+"arán")
    print(*ll)

    ll=[]
    ll.append(stem+"aría")
    ll.append(stem+"arías")
    ll.append(stem+"aría")
    ll.append(stem+"aríamos")
    ll.append(stem+"aríash"),
    ll.append(stem+"arían")
    print(*ll)

    ll=[]
    ll.append(stem+"e")
    ll.append(stem+"es")
    ll.append(stem+"e")
    ll.append(stem+"emos")
    ll.append(stem+"ésh")
    ll.append(stem+"en")
    print(*ll)

    ll=[]
    ll.append(stem+"ara")
    ll.append(stem+"aras")
    ll.append(stem+"ara")
    ll.append(stem+"áramos")
    ll.append(stem+"arash")
    ll.append(stem+"aran")
    print(*ll)

    ll=[]
    ll.append(stem+"a")
    ll.append(stem+"ad")
    ll.append(stem+"es")
    ll.append(stem+"ésh")
    print(*ll)

def verbER():
    print(">>>>")
    ll=[]
    ll.append(verb)
    ll.append(stem+"iendo")
    ll.append(stem+"ido")
    print(*ll)

    ll=[]
    ll.append(stem+"o")
    ll.append(stem+"es")
    ll.append(stem+"e")
    ll.append(stem+"emos")
    ll.append(stem+"ésh")
    ll.append(stem+"en")
    print(*ll)

    ll=[]   
    ll.append(stem+"í")
    ll.append(stem+"ites")
    ll.append(stem+"ió")
    ll.append(stem+"imos")
    ll.append(stem+"itesh")
    ll.append(stem+"ieron")
    print(*ll)

    ll=[]    
    ll.append(stem+"ía")
    ll.append(stem+"ías")
    ll.append(stem+"ía")
    ll.append(stem+"íamos")
    ll.append(stem+"íash")
    ll.append(stem+"ían")
    print(*ll)

    ll=[]
    ll.append(stem+"eré")
    ll.append(stem+"erás")
    ll.append(stem+"erá")
    ll.append(stem+"eremos")
    ll.append(stem+"erésh")
    ll.append(stem+"erán")
    print(*ll)

    ll=[]    
    ll.append(stem+"ería")
    ll.append(stem+"erías")
    ll.append(stem+"ería")
    ll.append(stem+"eríamos")
    ll.append(stem+"eríash")
    ll.append(stem+"erían")
    print(*ll)

    ll=[]    
    ll.append(stem+"a")
    ll.append(stem+"as")
    ll.append(stem+"a")
    ll.append(stem+"amos")
    ll.append(stem+"ásh")
    ll.append(stem+"an")
    print(*ll)

    ll=[]    
    ll.append(stem+"iera")
    ll.append(stem+"ieras")
    ll.append(stem+"iera")
    ll.append(stem+"iéramos")
    ll.append(stem+"ierash")
    ll.append(stem+"ieran")
    print(*ll)

    ll=[]    
    ll.append(stem+"e")
    ll.append(stem+"ed")
    ll.append(stem+"as")
    ll.append(stem+"ásh")
    print(*ll)

def verbIR():
    print(">>>>")
    ll=[]
    ll.append(verb)
    ll.append(stem+"iendo")
    ll.append(stem+"ido")
    print(*ll)

    ll=[]
    ll.append(stem+"o")
    ll.append(stem+"es")
    ll.append(stem+"e")
    ll.append(stem+"imos")
    ll.append(stem+"ísh")
    ll.append(stem+"en")
    print(*ll)

    ll=[]
    ll.append(stem+"í")
    ll.append(stem+"ites")
    ll.append(stem+"ió")
    ll.append(stem+"imos")
    ll.append(stem+"itesh")
    ll.append(stem+"ieron")
    print(*ll)

    ll=[]    
    ll.append(stem+"ía")
    ll.append(stem+"ías")
    ll.append(stem+"ía")
    ll.append(stem+"íamos")
    ll.append(stem+"íash")
    ll.append(stem+"ían")
    print(*ll)

    ll=[]    
    ll.append(stem+"iré")
    ll.append(stem+"irás")
    ll.append(stem+"irá")
    ll.append(stem+"iremos")
    ll.append(stem+"irésh")
    ll.append(stem+"irán")
    print(*ll)

    ll=[]    
    ll.append(stem+"iría")
    ll.append(stem+"irías"),
    ll.append(stem+"iría")
    ll.append(stem+"iríamos")
    ll.append(stem+"iríash")
    ll.append(stem+"irían")
    print(*ll)

    ll=[]    
    ll.append(stem+"a")
    ll.append(stem+"as")
    ll.append(stem+"a")
    ll.append(stem+"amos")
    ll.append(stem+"ásh")
    ll.append(stem+"an")
    print(*ll)

    ll=[]    
    ll.append(stem+"iera")
    ll.append(stem+"ieras")
    ll.append(stem+"iera")
    ll.append(stem+"iéramos")
    ll.append(stem+"ierash")
    ll.append(stem+"ieran")
    print(*ll)

    ll=[]    
    ll.append(stem+"e")
    ll.append(stem+"id")
    ll.append(stem+"as")
    ll.append(stem+"ásh")
    print(*ll)

#=======================================================================

print("Enter a verb")
verb=input()

if len(verb)<3 and verb != "ir":
    print("Stem of the verb is empty")
    exit()
stem=verb[:-2]

# Test if verb is ar, er, ir 
if verb.endswith("ar"):
    verbAR()
elif verb.endswith("er"):
    verbER()
elif verb.endswith("ir"):
    verbIR()
else:
    print("Verb does not end with ar, er or ir")
    exit()