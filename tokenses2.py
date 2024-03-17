
 
 


def is_digit(n):
    try:
        x=int(n)
        return True
    except:
        return False

file=open("code.txt","r")
listfile=[]
for i in file.readlines():
    listfile.append(i)
file.close()
val=""
name=""
for i in listfile:
    if "define" in i:
        for j in range(len("#define"),len(i)):
            if is_digit(i[j]) or i[j]==".":
                val=val+i[j]
            elif i[j]!=" " and i[j]!="\n":
                name=name+i[j]
                
file=open("preprocess.txt","w")
for i in listfile:
    line=""
    if name in i and  "#" not in i:
        j=0
        while j<len(i)-1:
            st=""
            for k in range(0,len(name)):
                st=st+i[j]
                j=j+1  
            
            if st==name:
                line=line+val
              
            else:
                line=line+st
                
        
            
            
    else:       
        line=i
    file.write(line)
file.close()                
             
      
Keyword = [ "int","float","while","do","void","define","return","swtich","break","case","float" ,"main", "cout", "cin", "include","for","using", "namespace","endl","std"]
Libraries =["iostream","cmath","string","radom","stdio" ,"graphic"]
Punctuation=[";", ",", ")", "(" ,"{","}","#","$","@"]
oprator=["+","^","-","/","&","|","*","<",">",">=","<=","=","!=","==","%"]
lowercase=[ "a", "b", "c", "d", "d", "e", "f", "g", "h", "i", "j" 
            ,"k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N"
            ,"O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def checkers(word,klist):
    c=False
    for i in klist:
        if word==i:
            c=True
    return c
        
        
    
            
file2=open("preprocess.txt","r")
            
for i in file2.readlines():
    st=""
    for j in i:
        if j!=" " and checkers(j,uppercase) or checkers(j,lowercase):
            st=st+j
        else:
           if checkers(st,Keyword):
                print(st," :keyword")
                st=""
           elif checkers(st, Libraries):
                print(st," :Libraries")
                st=""
           elif st!="":               
               print(st," :identifiers")
               st=""
           if checkers(j,oprator):
               print(j," :opreator")
           elif  checkers(j,Punctuation):
               print(j," :punctuation")  
           elif is_digit(j):
               print(j," :Digits.")
           elif j==" ":
               continue      
            
         
            
     
         
        
