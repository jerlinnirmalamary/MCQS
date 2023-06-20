from django.shortcuts import render,redirect
from .databasedj import use,a,q

# Create your views here.


def home(req):
    return render(req,'home.html')


def sign(req):
    
    if(req.method=="POST"):
        nm=req.POST.get('name1')
        em=req.POST.get('email1')
        pd=req.POST.get('pwd1')
        data1 ={"name":nm,"email":em,"pwd1":pd}
        print(data1)
        use.insert_one(data1)
        return redirect('home')
         
        
    return render(req,"signup.html", {'mydj':True})

 
def log(req):
    if(req.method == "POST"):
        em=req.POST.get("email1")
        print(em)
        
        data=use.find_one({"emails":em})
        print(data)
        return redirect("ans")
 
    return render(req,"signup.html",{'mydj':False})

def que(req):
    print(req.method)
    if(req.method == "POST"):
        quess=req.POST.get("quest")
        print(quess)  
        option1 = req.POST.get("opt1")
        print(option1) 
        
        option2=req.POST.get("opt2")
        print(option2)
        
        option3=req.POST.get("opt3")
        print(option3) 
        
        answer=req.POST.get("ans")
        print(answer)
        
        d={"question":quess,"options":[option1,option2,option3],"ans":option3}
        
        q.insert_one(d)
        
        return redirect("admi")
    
    return render(req,"admin.html")


def answer(req):
    import random
    dbData=list(q.find())
    data=[]
    
    for j in range(len(dbData)):
        i=dbData[j]
        
        
        o=i.get ("options")
        random.shuffle(o)
        
        i["options"]=o
        
        i["ind"]=f"{j+1}"
        print(i)
        data.append(i)
    
    
    return render(req,'answer.html',{"data":data})