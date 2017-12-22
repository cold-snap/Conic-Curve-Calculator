from sympy import *
from math import  *
from Tkinter import *
from tkMessageBox import *
from tkSimpleDialog import *

All={}
Oval={}
Hyperbola={}
Parabola={}
Line={}
all_count=0
oval_count=0
hyperbola_count=0
parabola_count=0  
line_count=0               #some global variables to use

class oval:
    def __init__(self,a,b,c,e):
        self.a=float(a)
        self.b=float(b)
        self.c=float(c)
        self.e=float(e)
        self.key=1
        if self.a==0 and self.e==0:
            self.withBAndC()
        if self.c==0 and self.e==0:
            self.withAAndB()
        if self.b==0 and self.e==0:
            self.withAAndC()
        if self.b==0 and self.c==0:
            self.withAAndE()
        if self.a==0 and self.c==0:
            self.withBAndE()
        if self.a==0 and self.b==0:
            self.withCAndE()
    def withBAndC(self):
        self.a=(self.c**2+self.b**2)**0.5
        self.e=self.c/self.a
    def withAAndB(self):
        self.c=(self.a**2-self.b**2)**0.5
        self.e=self.c/self.a
    def withAAndC(self):
        self.b=(self.a**2-self.c**2)**0.5
        self.e=self.c/self.a
    def withAAndE(self):
        self.c=self.a*self.e
        self.b=(self.a**2-self.c**2)**0.5
    def withBAndE(self):
        self.a=self.b/((1-self.e**2)**0.5)
        self.c=(self.a**2-self.b**2)**0.5
    def withCAndE(self):
        self.a=self.c/self.e
        self.b=(self.a**2-self.c**2)**0.5
    def __str__(self):
        return 'Oval:a=%.3f,b=%.3f,c=%.3f,e=%.3f' % (self.a,self.b,self.c,self.e)

class hyperbola:
    def __init__(self,a,b,c,e):
        self.a=float(a)
        self.b=float(b)
        self.c=float(c)
        self.e=float(e)
        self.key=2
        if self.a==0 and self.e==0:
            self.withBAndC()
        if self.c==0 and self.e==0:
            self.withAAndB()
        if self.b==0 and self.e==0:
            self.withAAndC()
        if self.b==0 and self.c==0:
            self.withAAndE()
        if self.a==0 and self.c==0:
            self.withBAndE()
        if self.a==0 and self.b==0:
            self.withCAndE()
    def withBAndC(self):
        self.a=(self.c**2-self.b**2)**0.5
        self.e=self.c/self.a
    def withAAndB(self):
        self.c=(self.a**2+self.b**2)**0.5
        self.e=self.c/self.a
    def withAAndC(self):
        self.b=(-self.a**2+self.c**2)**0.5
        self.e=self.c/self.a
    def withAAndE(self):
        self.c=self.a*self.e
        self.b=(-self.a**2+self.c**2)**0.5
    def withBAndE(self):
        self.a=self.b/((-1+self.e**2)**0.5)
        self.c=(self.a**2+self.b**2)**0.5
    def withCAndE(self):
        self.a=self.c/self.e
        self.b=(-self.a**2+self.c**2)**0.5
    def __str__(self):
        return 'Hyperbola:a=%.3f,b=%.3f,c=%.3f,e=%.3f.' % (self.a,self.b,self.c,self.e)

class parabola:
    def __init__(self,p):
        self.p=float(p)
        self.e=float(1)
        self.key=3
    def __str__(self):
        return 'Parabola:p=%.3f,e=%.3f.' % (self.p,self.e)

class line():
    def __init__(self,k,n):
        self.k=float(k)
        self.n=float(n)
        self.key=4
    def __str__(self):
        return 'Line:y=%.3fx+%.3f' % (self.k,self.n)
class var_oval():
    def __init__(self,e):
        self.e=float(e)
        self.key=5
    def __str__(self):
        return ' Variable oval:e=%.3f.' % (self.e)

class var_hyperbola():
    def __init__(self,e):
        self.e=float(e)
        self.key=6
    def __str__(self):
        return ' Variable hyperbola:e=%.3f.' % (self.e)
class var_parabola():
    def __init__(self):
        self.key=7
    def __str__(self):
        return 'Variable parabola'

class var_line_loc:
    def __init__(self,location):
        self.location=location
        self.key=8
    def __str__(self):
        return 'Variable line which has point (%.3f,%.3f)' % (self.location[0],self.location[1])
class var_line_k:
    def __init__(self,k):
        self.k=k
        self.key=9
    def __str__(self):
        return 'Variable line whose k is %.3f' % (self.k)

def cal_al(item_1,item_2):
    con_1=0
    con_2=0
    if item_1.key>item_2.key:
        con_1=item_1
        con_2=item_2
        item_1=con_2
        item_2=con_1       #make the former is lower than the latter
    blanket=[]
    aset=set()
    if item_1.key==1:
        if item_2.key==1:
            x,y=symbols('x,y',real=True)
            aset=nonlinsolve([x**2/item_1.a**2+y**2/item_1.b**2-1,x**2/item_2.a**2+y**2/item_2.b**2-1],[x,y])
        if item_2.key==2:
            x,y=symbols('x,y',real=True)
            aset=nonlinsolve([x**2/item_1.a**2+y**2/item_1.b**2-1,x**2/item_2.a**2-y**2/item_2.b**2-1],[x,y])
        if item_2.key==3:
            x,y=symbols('x,y',real=True)
            aset=nonlinsolve([x**2/item_1.a**2+y**2/item_1.b**2-1,y**2-2*item_2.p*x],[x,y])
        if item_2.key==4:
            x,y=symbols('x,y',real=True)
            aset=nonlinsolve([x**2/item_1.a**2+y**2/item_1.b**2-1,y-item_2.k*x-item_2.n],[x,y])
        
    if item_1.key==2:
        if item_2.key==2:
            x,y=symbols('x,y',real=True)
            aset=nonlinsolve([x**2/item_1.a**2-y**2/item_1.b**2-1,x**2/item_2.a**2-y**2/item_2.b**2-1],[x,y])
        if item_2.key==3:
            x,y=symbols('x,y',real=True)
            aset=nonlinsolve([x**2/item_1.a**2-y**2/item_1.b**2-1,y**2-2*item_2.p*x],[x,y])
        if item_2.key==4:
            x,y=symbols('x,y',real=True)
            aset=nonlinsolve([x**2/item_1.a**2-y**2/item_1.b**2-1,y-item_2.k*x-item_2.n],[x,y])
    if item_1.key==3:
        if item_2.key==3:
            x,y=symbols('x,y',real=True)
            aset=nonlinsolve([y**2-2*item_1.p*x,y**2-2*item_2.p*x],[x,y])
        if item_2.key==4:
            x,y=symbols('x,y',real=True)
            aset=nonlinsolve([y**2-2*item_1.p*x,y-item_2.k*x-item_2.n],[x,y])
#'''Only type int can be thrown into nonlinsolve'''
    if item_1.key==4: # a line and variable conic corve
        if item_2.key==4:
            x,y=symbols('x,y',real=True)
            k_1=int(item_1.k)
            n_1=int(item_1.n)
            k_2=int(item_1.k)
            n_2=int(item_2.n)
            aset=linsolve([y-k_1*x-n_1,y-k_2*x-n_2],[x,y])
        if item_2.key==5:  # not invalid now
            x,y,a=symbols('x,y,a',real=True)
            k=int(item_1.k)
            n=int(item_1.n)
            aset=nonlinsolve([y-k*x-n,x**2/a**2+y**2/((1-item_2.e**2)*a**2)-1],[x,y])
        if item_2.key==6:  # not invalid
            k=int(item_1.k)
            n=int(item_1.n)
            x,y,a=symbols('x,y,a',real=True)
            aset=nonlinsolve([y-k*x-n,x**2/a**2-y**2/((item_2.e**2-1)*a**2)-1],[x,y])
        if item_2.key==7:
            x,y,p=symbols('x,y,p',real=True)
            k=int(item_1.k)
            n=int(item_1.n)
            aset=nonlinsolve([y-k*x-n,y**2-2*p*x],[x,y])
        if item_2.key==8:
            x,y,k=symbols('x,y,k',real=True)
            k=int(item_1.k)
            n=int(item_1.n)
            location=[int(item_2.location[0]),int(item_2.location[1])]
            aset=linsolve([y-k*x-n,y-location[1]-k*x-k*location[0]],[x,y])
        if item_2.key==9:
            x,y,b==symbols('x,y,n',real=True)
            k=int(item_1.k)
            n=int(item_1.n)
            k_2=int(item_2.k)
            aset=linsolve([y-k*x-n,y-k_2*x-n],[x,y])
    if item_2.key==8:# a variable line with a set location and coniccurve
        if item_1.key==1:
            x,y,k=symbols('x,y,k',real=True)
            a=int(item_1.a)
            b=int(item_1.b)
            location=[int(item_2.location[0]),int(item_2.location[1])]
            aset=nonlinsolve([x**2/a**2+y**2/b**2-1,y-location[1]-k*x-k*location[0]],[x,y])
        if item_1.key==2:
            x,y,k=symbols('x,y,k',real=True)
            a=int(item_1.a)
            b=int(item_1.b)
            location=[int(item_2.location[0]),int(item_2.location[1])]
            aset=nonlinsolve([x**2/a**2-y**2/b**2-1,y-location[1]-k*x-k*location[0]],[x,y])
        if item_1.key==3:
            x,y,k=symbols('x,y,k',real=True)
            location=[int(item_2.location[0]),int(item_2.location[1])]
            p=item_1.p
            aset=nonlinsolve([y**2-2*p*x,y-location[1]-k*x-k*location[0]],[x,y])
    if item_2.key==9:# a variable line with a set 'k' and coniccurve
        if item_1.key==1:
            x,y,n=symbols('x,y,n',real=True)
            a=int(item_1.a)
            b=int(item_1.b)
            k=int(item_2.k)
            aset=nonlinsolve([x**2/a**2+y**2/b**2-1,y-k*x-n],[x,y])
        if item_1.key==2:
            x,y,n=symbols('x,y,n',real=True)
            a=int(item_1.a)
            b=int(item_1.b)
            k=int(item_2.k)
            aset=nonlinsolve([x**2/a**2-y**2/b**2-1,y-k*x-n],[x,y])
        if item_1.key==3:
            x,y,n=symbols('x,y,n',real=True)
            p=int(item_1.p)
            k=int(item_2.k)
            aset=nonlinsolve([y**2-2*p*x,y-k*x-n],[x,y])
    
    for item in aset:
        blanket.append(item)
    return blanket                      

def length(loc_1,loc_2):  #calaulate the length of line
    length=0
    if loc_1!=loc_2:
        length=((loc_1[0]-loc_2[0])**2+(loc_1[1]-loc_2[1])**2)**0.5
    return length   #calculate the distance of a location to a line

def highth(loc,line):
    if line.key==4:
        highth=abs(line.k*loc[0]-loc[1]+line.n)/sqrt(line.k**2+1)
    if line.key==8: # error code can't convert expression to float
        k=symbols('k')
        location=[int(line.location[0]),int(line.location[1])]
        highth=Abs(loc[0]*k-loc[1]+location[0]*k-location[1])/(k**2+1)**0.5
    if line.key==9:
        n=symbols('n')
        highth=abs(line.k*loc[0]-loc[1]+n)/sqrt(line.k**2+1)
    return highth

#some functions to add items
def add_oval():
    global text_1,All,Oval,all_count,oval_count,canvas
    value_1,value_2,value_3,value_4=text_1.get().split(',')
    value_1=eval(value_1)
    value_2=eval(value_2)
    value_3=eval(value_3)
    value_4=eval(value_4)
    anoval=oval(value_1,value_2,value_3,value_4)
    All[all_count]=anoval
    Oval[oval_count]=anoval
    all_count+=1
    oval_count+=1
    canvas.delete('all')
    canvas.create_text(150,30,text='Adding '+anoval.__str__()+'\n'+' '*27+'Completed')
   
def add_hyperbola():
    global text_2,All,Hyperbola,all_count,hyperbola_count,canvas
    value_1,value_2,value_3,value_4=text_2.get().split(',')
    value_1=eval(value_1)
    value_2=eval(value_2)
    value_3=eval(value_3)
    value_4=eval(value_4)
    ahyperbola=hyperbola(value_1,value_2,value_3,value_4)
    All[all_count]=ahyperbola
    Hyperbola[hyperbola_count]=ahyperbola
    all_count+=1
    hyperbola_count+=1
    canvas.delete('all')
    canvas.create_text(150,30,text='Adding '+ahyperbola.__str__()+'\n'+' '*27+'Completed')
    
def add_parabola():
    global text_3,All,Parabola,all_count,parabola_count,canvas
    value_1=text_3.get()
    value_1=eval(value_1)
    aparabola=parabola(value_1)
    All[all_count]=aparabola
    Parabola[parabola_count]=aparabola
    all_count+=1
    parabola_count+=1
    canvas.delete('all')
    canvas.create_text(150,30,text='Adding '+aparabola.__str__()+'\n'+' '*23+'Completed')
   
def add_line():
    global text_4,All,Line,all_count,line_count,canvas
    value_1,value_2=text_4.get().split(',')
    value_1=eval(value_1)
    value_2=eval(value_2)
    aline=line(value_1,value_2)
    All[all_count]=aline
    Line[line_count]=aline
    all_count+=1
    line_count+=1
    canvas.delete('all')
    canvas.create_text(150,30,text='Adding '+aline.__str__()+'\n'+' '*15+'Completed')

root=Tk()
root.title('Conic curve calculater')

#Adding part
Label_up=Label(root,text='Choose the type and input the value(normal)')
Label_up.grid(row=0,column=0,columnspan=11,sticky=W+E)
Label_1=Label(root,text='Oval(a,b,c,e)')
Label_1.grid(row=1,column=0,columnspan=2,sticky=W+E)
text_1=StringVar()
Entry_1=Entry(root,textvariable=text_1)
text_1.set('0,0,0,0')
Entry_1.grid(row=1,column=2,columnspan=8)
Button_1=Button(root,text='Submit',command=add_oval)
Button_1.grid(row=1,column=10,columnspan=2,sticky=W+E)

Label_2=Label(root,text='Hyperbola(a,b,c,e)')
Label_2.grid(row=2,column=0,columnspan=2,sticky=W+E)
text_2=StringVar()
Entry_2=Entry(root,textvariable=text_2)
text_2.set('0,0,0,0')
Entry_2.grid(row=2,column=2,columnspan=8)
Button_2=Button(root,text='Submit',command=add_hyperbola)
Button_2.grid(row=2,column=10,columnspan=2,sticky=W+E)

Label_3=Label(root,text='Parabola(p)')
Label_3.grid(row=3,column=0,columnspan=2,sticky=W+E)
text_3=StringVar()
Entry_3=Entry(root,textvariable=text_3)
text_3.set('0')
Entry_3.grid(row=3,column=2,columnspan=8)
Button_3=Button(root,text='Submit',command=add_parabola)
Button_3.grid(row=3,column=10,columnspan=2,sticky=W+E)

Label_4=Label(root,text='Line(k,n)')
Label_4.grid(row=4,column=0,columnspan=2,sticky=W+E)
text_4=StringVar()
Entry_4=Entry(root,textvariable=text_4)
text_4.set('0,0')
Entry_4.grid(row=4,column=2,columnspan=8)
Button_4=Button(root,text='Submit',command=add_line)
Button_4.grid(row=4,column=10,columnspan=2,sticky=W+E)

#functions to show all items
def show_all():
    global canvas
    canvas.delete('all')
    alllist=All.keys()
    leng=len(alllist)
    for i in range(leng):
        canvas.create_text(150,12*i+10,text=str(i)+':'+All[i].__str__())
    canvas.create_text(150,12*leng+10,text='In all:'+str(leng)+' items.')
    
def show_oval():
    global canvas
    canvas.delete('all')
    alllist=Oval.keys()
    leng=len(alllist)
    for i in range(leng):
        canvas.create_text(150,12*i+10,text=str(i)+':'+Oval[i].__str__())
    canvas.create_text(150,12*leng+10,text='In all:'+str(leng)+' items.')
           
def show_hyperbola():
    global canvas
    canvas.delete('all')
    alllist=Hyperbola.keys()
    leng=len(alllist)
    for i in range(leng):
        canvas.create_text(150,12*i+10,text=str(i)+':'+Hyperbola[i].__str__())
    canvas.create_text(150,12*leng+10,text='In all:'+str(leng)+' items.')
        
def show_parabola():
    global canvas
    canvas.delete('all')
    alllist=Parabola.keys()
    leng=len(alllist)
    for i in range(leng):
        canvas.create_text(150,12*i+10,text=str(i)+':'+Parabola[i].__str__())
    canvas.create_text(150,12*leng+10,text='In all:'+str(leng)+' items.')
        
def show_line():
    global canvas
    canvas.delete('all')
    alllist=Line.keys()
    leng=len(alllist)
    for i in range(leng):
        canvas.create_text(150,12*i+10,text=str(i)+':'+Line[i].__str__())
    canvas.create_text(150,12*leng+10,text='In all:'+str(leng)+' items.')

#show what you have
Label_5=Label(root,text='Show all items')
Label_5.grid(row=5,column=0,columnspan=3)
Button_5=Button(root,text='ALL',command=show_all)
Button_5.grid(row=5,column=3,columnspan=2)
Button_6=Button(root,text='OVAL',command=show_oval)
Button_6.grid(row=5,column=5,columnspan=2)
Button_7=Button(root,text='HYPERBOLA',command=show_hyperbola)
Button_7.grid(row=5,column=7,columnspan=2)
Button_8=Button(root,text='PARABOLA',command=show_parabola)
Button_8.grid(row=5,column=9,columnspan=2)
Button_9=Button(root,text='LINE',command=show_line)
Button_9.grid(row=5,column=11,columnspan=2)

#functions fo menus
def me_cal_inter():
    cal_inter=Toplevel()
    text_inter=StringVar()
    alabel=Label(cal_inter,text='Choose the item to calculate from ALL')
    alabel.grid(row=0,column=0,columnspan=25)
    aentry=Entry(cal_inter,textvariable=text_inter)
    text_inter.set('0,0')
    aentry.grid(row=1,column=0,columnspan=12)
    def core_cal():
        acanvas.delete('all')
        id_1,id_2=text_inter.get().split(',')
        id_1=int(id_1)
        id_2=int(id_2)
        result=cal_al(All[id_1],All[id_2])
        for i in range(len(result)):
            result[i]=str(result[i])
        result='\n'.join(result)        #make it a string and be able to change line
    
        acanvas.create_text(400,50,text=result)
    abutton=Button(cal_inter,text='Sure',command=core_cal)
    abutton.grid(row=1,column=12,columnspan=13,sticky=W+E)
    acanvas=Canvas(cal_inter,width=800,height=100)
    acanvas.grid(row=2,column=0,columnspan=25)

def me_cal_len():
    cal_len=Toplevel()
    text_len=StringVar()
    alabel=Label(cal_len,text='Choose the item to calculate from ALL')
    alabel.grid(row=0,column=0,columnspan=8)
    aentry=Entry(cal_len,textvariable=text_len)
    text_len.set('0,0')
    aentry.grid(row=1,column=0,columnspan=4)
    def core_cal():
        acanvas.delete('all')
        id_1,id_2=text_len.get().split(',')
        id_1=int(id_1)
        id_2=int(id_2)
        result=cal_al(All[id_1],All[id_2])
        try:
            result=str(length(result[0],result[1]))
            text_sh=result
            if len(text_sh)>173:
                acanvas.create_text(150,25,text=text_sh[:55])
                acanvas.create_text(150,45,text=text_sh[55:120])
                acanvas.create_text(150,65,text=text_sh[120:173])
                acanvas.create_text(150,85,text=text_sh[173:])
            elif len(text_sh)<=173 and len(text_sh)>110:
                acanvas.create_text(150,35,text=text_sh[:55])
                acanvas.create_text(150,55,text=text_sh[55:120])
                acanvas.create_text(150,75,text=text_sh[120:])
            elif len(text_sh)<=110 and len(text_sh)>50:
                acanvas.create_text(150,35,text=text_sh[:50])
                acanvas.create_text(150,65,text=text_sh[50:])
            else:
                acanvas.create_text(150,50,text=text_sh)
                acanvas.create_text(150,50,text=result)
        except IndexError:
            acanvas.create_text(150,50,text='No enough solutions')
    abutton=Button(cal_len,text='Sure',command=core_cal)
    abutton.grid(row=1,column=4,columnspan=4,sticky=W+E)
    acanvas=Canvas(cal_len,width=300,height=100)
    acanvas.grid(row=2,column=0,columnspan=8)
    

def me_cal_area():   
    area=0

    
    def Sure():
        acanvas.delete('all')
        id_1,id_2=text_area.get().split(',')
        id_1=int(id_1)
        id_2=int(id_2)
        item_1=All[id_1]
        item_2=All[id_2]
        if item_1.key>item_2.key:
            acanvas.i_1=item_1
            acanvas.i_2=item_2
            item_1=acanvas.i_2
            item_2=acanvas.i_1       #make the former is lower than the latter
        result_1=cal_al(All[id_1],All[id_2])
        acanvas.result=result_1
        try:
            acanvas.line=line(0,0)
            if item_2.key==8 and (item_1.key==1 or item_1.key==2 or item_1.key==3):
                acanvas.line=item_2 
            if item_2.key==7 and (item_1.key==1 or item_1.key==2 or item_1.key==3):
                acanvas.line=item_2 
            else:
                acanvas.line.k=(result_1[0][1]-result_1[1][1])/(result_1[0][0]-result_1[1][0])
                acanvas.line.n=result_1[0][1]-acanvas.line.k*result_1[0][0]
        except ZeroDivisionError:
            acanvas.create_text(280,50,text='No supported line')
        except IndexError:
            acanvas.create_text(280,50,text='No enough solutions')
            
    def core_cal():
        acanvas.delete('all')
        location_1,location_2=text_area_2.get().split(',')
        location_1=float(location_1[1:])
        location_2=float(location_2[:-1])
        location=(location_1,location_2)
        leng=length(acanvas.result[0],acanvas.result[1])
        area=leng*highth(location,acanvas.line)/2
        text_sh=str(area)
        if len(text_sh)>173:
            acanvas.create_text(150,25,text=text_sh[:55])
            acanvas.create_text(150,45,text=text_sh[55:120])
            acanvas.create_text(150,65,text=text_sh[120:173])
            acanvas.create_text(150,85,text=text_sh[173:])
        elif len(text_sh)<=173 and len(text_sh)>110:
            acanvas.create_text(150,35,text=text_sh[:55])
            acanvas.create_text(150,55,text=text_sh[55:120])
            acanvas.create_text(150,75,text=text_sh[120:])
        elif len(text_sh)<=110 and len(text_sh)>50:
            acanvas.create_text(150,35,text=text_sh[:50])
            acanvas.create_text(150,65,text=text_sh[50:])
        else:
            acanvas.create_text(150,50,text=text_sh)
            
    cal_area=Toplevel()
    text_area=StringVar()
    alabel=Label(cal_area,text='Choose the item to calculate from ALL')
    alabel.grid(row=0,column=0,columnspan=8)
    aentry=Entry(cal_area,textvariable=text_area)
    text_area.set('0,0')
    aentry.grid(row=1,column=0,columnspan=4)
    blabel=Label(cal_area,text='Location:')
    blabel.grid(row=2,column=0,columnspan=3)
    text_area_2=StringVar()
    bentry=Entry(cal_area,textvariable=text_area_2)
    text_area_2.set('(0,0)')
    bentry.grid(row=2,column=3,columnspan=3)
    bbutton=Button(cal_area,text='Calculate',command=core_cal)
    bbutton.grid(row=2,column=6,columnspan=2)
    abutton=Button(cal_area,text='Sure',command=Sure)
    abutton.grid(row=1,column=4,columnspan=4,sticky=W+E)
    acanvas=Canvas(cal_area,width=300,height=100)
    acanvas.grid(row=3,column=0,columnspan=8)

def add_var_oval():
    new_e=askfloat(title='Variable oval',prompt='Please input the value of e:')
    new_oval=var_oval(new_e)
    global All,Oval,all_count,oval_count
    All[all_count]=new_oval
    Oval[oval_count]=new_oval
    all_count+=1
    oval_count+=1
    canvas.delete('all')
    canvas.create_text(150,30,text='Adding '+new_oval.__str__()+'\n'+' '*27+'Completed')
    
def add_var_hyperbola():
    new_e=askfloat(title='Variable hyperbola',prompt='Please input the value of e:')
    new_hyperbola=var_hyperbola(new_e)
    global All,Hyperbola,all_count,hyperbola_count
    All[all_count]=new_hyperbola
    Hyperbola[hyperbola_count]=new_hyperbola
    all_count+=1
    hyperbola_count+=1
    canvas.delete('all')
    canvas.create_text(150,30,text='Adding '+new_hyperbola.__str__()+'\n'+' '*27+'Completed')

def add_var_parabola():
    askokcancel('Variable parabola','Complete in adding a variable parabola',default =CANCEL,icon =INFO)
    new_parabola=var_parabola()
    global All,Parabola,all_count,parabola_count
    All[all_count]=new_parabola
    Parabola[parabola_count]=new_parabola
    parabola_count+=1
    all_count+=1
    canvas.delete('all')
    canvas.create_text(150,30,text='Adding '+new_parabola.__str__()+'\n'+' '*27+'Completed')

def add_var_line_by_loca():
    new_loc=askstring(title='Variable Line By Location',prompt='Please input the value of location:')
    string_1,string_2=new_loc.split(',')
    string_1=float(string_1[1:])
    string_2=float(string_2[:-1])
    new_loc=(string_1,string_2)
    new_line=var_line_loc(new_loc)
    global All,Line,line_count,all_count
    All[all_count]=new_line
    Line[line_count]=new_line
    all_count+=1
    line_count+=1
    canvas.delete('all')
    canvas.create_text(150,30,text='Adding '+new_line.__str__()+'\n'+' '*27+'Completed')

def add_var_line_by_k():
    new_k=askfloat(title='Variable Line By K',prompt='Please input the value of k:')
    new_line=var_line_k(new_k)
    global All,Line,all_count,line_count
    All[all_count]=new_line
    Line[all_count]=new_line
    all_count+=1
    line_count+=1
    canvas.delete('all')
    canvas.create_text(150,30,text='Adding '+new_line.__str__()+'\n'+' '*27+'Completed')
    
 #give user a help file to look up 
def write_help_file():
    fil='''1.1  Common inputing
  In the main window,there are the entries where you can add a new item.For a certain type conic curve,you must follow certain format,or the programme would go wrong,the format is as follow,
         Oval as a,b,c,e (x**2/a**2+y**2/b**2=1)
         Hyperbola as a,b,c,e (x**2/a**2-y**2/b**2=1)
         Parabola as p  (y**2=2*P*x)
         Line as k,n  (y=k*x+n)
  For type oval and hyperbola,they both allow you to input default value,in fact,just any two of them is OK,if not given,just put 0.For instance,you kown a=2,b=1,you will input 2,1,0,0
1.2  Show all items
  There five buttons you can click,once you click it,a list of items will be showed in the below.For example,if you choose the 'ALL',all items you have added will be showed(with the number of it.)
  2 Menu
2.1  Operation
2.1.1 Calculating Intersection
   You are required to input two numbers of item of ALL,for emample,if you want to calculate 1(an oval) and 4(a line),you can input '1,4'('4,1'is also available)
2.1.2  Calculating Length
   Just input two numbers of item and it will show you the length of two intersections.
2.1.3 Calculating Area
   Only triangle is avaialable.
    Input:two numbers of item and one location.For example,'1,2' and '(2,5)'
   Output:the area of the triangle made of two intersections and the location you input.
   ATTENTION:If there are less than two intersections or the line can't be shown in the form of y=k*x
+n ,it will tell you an error code.
2.2 Set variable item
This module will allow you to set an item with variable attributes,thus enabling you to do some more
complex operations.
2.2.1 Oval
  Just input the value of the oval,the 'a' is variable,and all of the results will include the variable 'a'.
2.2.2 Hyperbola
  The same as oval,the only difference is the value of e is higher(greater than 1).
2.2.3 Parabola
  Nothing is to be inputed,and the result will include the variable 'p'.
2.2.4 Line By Location
  Enable you to add a line which goes through a set location all the time,you just need to input the location,and 'k' is variable.
2.2.5 Line By K
  Enable you to add a line which has the same attribute 'k',you need to input the value if it,and 'n' is variable(as y=k*x+n).
ATTENTION : INTERSECTION,LENGTH,AREA FO VARIABLE OVAL(HYPERBOLA) AND SET LINE IS NOT AVAILABLE'''
    des=open('D:/help_file_for_calculater.txt','w')
    des.write(fil)
    des.close()
    askokcancel('Saving Comlpeted','''The help file has been saved into
                \n  D:/help_file_for_calculater.txt 
                \n  PLEASE READ IT CAREFULLY.''',default =CANCEL,icon =INFO)


#A menu to make operation
menu_up=Menu(root)
root.config(menu=menu_up)

menu_op=Menu(menu_up)
menu_op.add_command(label='Calculating Intersection',command=me_cal_inter)
menu_op.add_command(label='Calculating Length',command=me_cal_len)
menu_op.add_command(label='Calculating Area',command=me_cal_area)
menu_up.add_cascade(label='Operation',menu=menu_op)

menu_se=Menu(menu_up)
menu_se.add_command(label='Oval',command=add_var_oval)
menu_se.add_command(label='Hyperbola',command=add_var_hyperbola)
menu_se.add_command(label='Parabola',command=add_var_parabola)
menu_se.add_command(label='Line by location',command=add_var_line_by_loca)
menu_se.add_command(label='Line by k',command=add_var_line_by_k)
menu_up.add_cascade(label='Set variable item',menu=menu_se)


menu_up.add_command(label='Help',command=write_help_file)


#a canvas to show results
canvas=Canvas(root,height=300,width=280)
canvas.grid(row=6,column=0,columnspan=11,sticky=W+E)
root.mainloop()
