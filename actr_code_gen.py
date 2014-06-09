# ACT-R Model Generator. Author: Kam Kwok, 2013/09, 2014
from Tkinter import *
#import tkMessageBox
import Tkinter,tkFileDialog
#import math
#import pylab  # matplotlib

# global variables and utilities section
md=[] # the act-r model list
hdr=[]
env=[]
dm=[]
agt=[]
main=[]
mD={} # to store env var names

myFormats = [
    ('Model file', '*.py')
    ]

#****************
# Utilities
#****************
def outwin(mlab,msg):
   tkMessageBox.showinfo(mlab, msg)


def donothing():
   filewin = Toplevel(root)
   msg = Label(filewin, text="Not implemented yet!!!")
   msg.pack()

def onclick():
   pass

def author():
    outwin('About',' Python ACT-R Lab\n Author: Kam Kwok\n Copyright 2013')

def loadf1():
    loadf()

def saveas1():
    saveas()

def new():
    clearall()

#****************
# GUI definition 
#
# standard
root = Tk(className=" Python ACT-R Lab")
master = root
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=loadf1)
filemenu.add_command(label="Save", command=saveas1)
#filemenu.add_command(label="Save as...", command=saveas1)
#filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=author)
menubar.add_cascade(label="Help", menu=helpmenu)
#--- header editor -----
##import ccm      
##log=ccm.log(html=True)   
##from ccm.lib.actr import *
frame = Frame(master)
frame.pack()
##L01 = Label(frame, text="ACT-R Modeling Editor")
##L01.pack( side = TOP)
L02 = Label(frame, text="Header Editor",fg="red")
L02.pack( side = TOP)
text_h = Text(frame, height = 5)
text_h.pack(fill=BOTH)
def badd_h():
    global hdr
    hdr =[]
    hdr.append('import ccm')
    hdr.append('from ccm.lib.actr import * ')
    line ='log=ccm.log(html=True)' if Ohtml.get() else 'log=ccm.log(html=False)'
    hdr.append(line)
    for l in hdr:
        text_h.insert(INSERT, l+'\n')
#buttons        
btn01 = Button(frame, text="Add header", fg="red", command=badd_h)
btn01.pack(side=LEFT)
def clr_h():
    text_h.delete(1.0, END)
btn_clrh = Button(frame, text="clear_hdr", command=clr_h)
btn_clrh.pack(side=LEFT)

# options
Ohtml = IntVar(value = 1)
opt_html = Checkbutton(frame, text = "html log", variable=Ohtml)
opt_html.pack(side=LEFT)
#---------------------
#--- header editor end-----

#---------------------

#--- env editor -----
# example:
#class Subway(ccm.Model):
# items in the environment look and act like chunks - but note the syntactic differences
# e.g bread=ccm.Model(isa='bread',location='on_counter')
frame1 = Frame(master)
frame1.pack()
L11 = Label(frame1, text="Env Editor",fg="red")
L11.pack( side = TOP)
text_e = Text(frame1, height = 5)
text_e.pack(fill=BOTH)
L12 = Label(frame1, text="Env name:")
L12.pack( side = LEFT)
E_e = Entry(frame1, bd =5, width=10)
E_e.pack(side = LEFT)
def baddenv():
    global env
    env =[]
    en = E_e.get()
    line ="class %s(ccm.Model):" % en if en else "#class ???(ccm.Model):"
    env.append(line) 
    env.append("# add chunk in env: bread=ccm.Model(isa='bread',location='on_counter')")
    mD['Env']=E_e.get()
    for l in env:
        text_e.insert(INSERT, l+'\n')
btn11 = Button(frame1, text="Add Env", fg="red", command=baddenv)
btn11.pack(side=LEFT)
L13 = Label(frame1, text="chunk name:")
L13.pack( side = LEFT)
E_cn = Entry(frame1, bd =5, width=10)
E_cn.pack(side = LEFT)
L14 = Label(frame1, text="slot name:")
L14.pack( side = LEFT)
E_sn = Entry(frame1, bd =5, width=10)
E_sn.pack(side = LEFT)
L15 = Label(frame1, text="slot value:")
L15.pack( side = LEFT)
E_sv = Entry(frame1, bd =5, width=10)
E_sv.pack(side = LEFT)
frame11 = Frame(master)
frame11.pack()
#buttons        
def clr_e():
    text_e.delete(1.0, END)
    E_e.delete(0,END)
    E_cn.delete(0,END)
    E_sn.delete(0,END)
    E_sv.delete(0,END)
btn_clre = Button(frame11, text="clear_env", command=clr_e)
btn_clre.pack(side=LEFT)
def add_c():
    l = "#    %s=ccm.Model(%s='%s')" % (E_cn.get(),E_sn.get(),E_sv.get())
    env.append(l)
    text_e.insert(INSERT, l+'\n')
    l = "# DM.add('slotname:value')"
    env.append(l)
    text_e.insert(INSERT, l+'\n')
btn_addc = Button(frame11, text="add chunk", command=add_c)
btn_addc.pack(side=LEFT)

#
#--- env editor end-----

#---------------------

#--- Agent editor -----
##class MyAgent(ACTR):    
##    focus=Buffer()
##    motor=MotorModule()
frame2 = Frame(master)
frame2.pack()
Len = Label(frame2, text="Agent Editor",fg="red")
Len.pack( side = TOP)
text_agt = Text(frame2, height = 12)
text_agt.pack(fill=BOTH)
Lani = Label(frame2, text="Agent:")
Lani.pack( side = LEFT)
E_agt = Entry(frame2, bd =5, width=10)
E_agt.pack(side = LEFT)
#option
Omotor = IntVar(value = 1)
o_mtr = Checkbutton(frame2, text = "motor", variable=Omotor)
o_mtr.pack(side=LEFT)
def add_agt():
    global agt
    agt =[]
    if Omotor.get():
        line = "class MotorModule(ccm.Model):\n    pass"
        agt.append(line)
    agtn = E_agt.get()
    mD['Agent']=agtn
    line ="class %s(ACTR):" % agtn if len(agtn)>1 else "class MyAgent(ACTR):"
    agt.append(line)
    line = "    focus=Buffer()\n    DMbuffer=Buffer()\n    DM=Memory(DMbuffer)"
    agt.append(line)
    if Omotor.get():
       line = "    motor=MotorModule()"
       agt.append(line)
       mD['Motor']='motor'
    for l in agt:
        text_agt.insert(INSERT, l+'\n')
b_addagt = Button(frame2, text="add agent", fg="red", command=add_agt)
b_addagt.pack(side=LEFT)
Lcn = Label(frame2, text="chunk:")
Lcn.pack( side = LEFT)
E_dcn = Entry(frame2, bd =5, width=10)
E_dcn.pack(side = LEFT)
Lsn = Label(frame2, text="slot name:")
Lsn.pack( side = LEFT)
E_dsn = Entry(frame2, bd =5, width=10)
E_dsn.pack(side = LEFT)
Lsv = Label(frame2, text="slot value:")
Lsv.pack( side = LEFT)
E_dsv = Entry(frame2, bd =5, width=10)
E_dsv.pack(side = LEFT)
#new frame
frame21 = Frame(master)
frame21.pack()
Lblank= Label(frame21, text="")
Lblank.pack( side = TOP)
#buttons        
def add_dc():
    l = "#    %s.add('%s:%s')" % ("DM",E_dsn.get(),E_dsv.get())
    text_agt.insert(INSERT, l+'\n')
b_adddc = Button(frame2, text="add chunk",fg="red",command=add_dc)
b_adddc.pack(side=LEFT)
#production frame <------------------------------------
##   def bread_bottom(focus='sandwich bread'):
##        print "tim - I have a piece of bread"     
##        focus.set('sandwich cheese')
framePE = Frame(master)
framePE.pack()
Lrn = Label(framePE, text="rule name")
Lrn.pack( side = LEFT)
E_rn = Entry(framePE, bd =5, width=10)
E_rn.pack(side = LEFT)
Lbc = Label(framePE, text="conditions")
Lbc.pack( side = LEFT)
E_bc = Entry(framePE, bd =5, width=20)
E_bc.pack(side = LEFT)
Lact = Label(framePE, text="actions:")
Lact.pack( side = LEFT)
E_act = Entry(framePE, bd =5, width=20)
E_act.pack(side = LEFT)
def add_rule():
    global agt
    l ="#    def %s(%s):" % (E_rn.get()if E_rn.get() else "#???", E_bc.get() if E_bc.get() else "#focus='???'")
    agt.append(l)
    text_agt.insert(INSERT, l+'\n')
    l = r"#        %s" % E_act.get() if E_act.get() else r"#        action ???"
    agt.append(l)
    text_agt.insert(INSERT, l+'\n')
    l = r"#        %s" % E_act.get() if E_act.get() else r"#        focus.set('???')"
    agt.append(l)
    text_agt.insert(INSERT, l+'\n')
b_addrule = Button(framePE, text="add rules", fg="red", command=add_rule)
b_addrule.pack(side=LEFT)
def clr_agt():
    global agt
    text_agt.delete(1.0, END)
    E_agt.delete(0,END)
    E_dcn.delete(0,END)
    E_dsn.delete(0,END)
    E_dsv.delete(0,END)
    E_rn.delete(0,END)
    E_bc.delete(0,END)
    E_act.delete(0,END)
    agt= []
b_clragt = Button(framePE, text="clear", command=clr_agt)
b_clragt.pack(side=LEFT)
#
#--- agent editor end-----
#---------------------------------
# standard ends

#------------------------------------------------ 
#  File (handlers are defined before the buttons)
#------------------------------------------------     
frameF = Frame(master)
frameF.pack(fill=BOTH)
text_f = Text(frameF,height = 15)
text_f.pack(fill=BOTH)
# frame for file btns
frameFB = Frame(master)
frameFB.pack(fill=BOTH)
L2 = Label(frameFB, text="Commands: ")
L2.pack( side = LEFT)
def bgen():
    try:
        global rs, hdr, env, agt
        rs=[]
        rs.extend(hdr)
        rs.extend(env)
        rs.extend(agt)
        m = "model="+mD['Agent']+"()"
        e = "env="+mD['Env']+"()"
        main= [m,e,"env.agent=model","ccm.log_everything(env)","env.run()","ccm.finished()"]
        rs.extend(main)
        for s in rs:
            text_f.insert(INSERT, s+'\n')
    except:
        print "Parts are missing, cannot generate model!"
bgen= Button(frameFB, text="Gen model", fg="red", command=bgen)
bgen.pack(side=LEFT)
# entry 
Lmfn = Label(frameFB, text="Model/file spec.")
Lmfn.pack( side = LEFT)
Emfn = Entry(frameFB, bd =5)
Emfn.pack(side = LEFT)

# file dialogs
def loadf():
    try:
        global rs
        # on loading a new file/model reset text, entry and global result list
        text_f.delete(1.0, END)
        Emfn.delete (0,END)
        rs=[]
        if Emfn.get() == '':
            f = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
            if f != None:
                Emfn.insert(0,f.name)
        else:
            f = open (Emfn.get(),'r')
        text_f.delete(1.0, END)
        text_f.insert(INSERT, f.read())
        f.close
    except:
        print "No file is loaded!"

        
def saveas():
    fn = tkFileDialog.asksaveasfilename(parent=root,filetypes=myFormats ,title="Save the image as...")
    if len(fn) >0:
       f = open(fn,'w')
       f.write(text_f.get(0.0, END))
       f.close
       print 'File %s is saved.' % fn
    else:
       print 'zero file name! file not saved'
    

def savef():
    try:
        f = open (Emfn.get(),'w')
        f.write(text_f.get(0.0, END))
        f.close
        outwin('File','%s is saved!!!' % Emfn.get())
##        print 'Model is saved.'
    except:
##        print 'cannot save file!!!'
        outwin('Error','Please enter model filename!!!')

# buttons to load and save text
b_load = Button(frameFB, text="load model", fg="red", command=loadf)
b_load.pack(side=LEFT)
b_save = Button(frameFB, text="save text", fg="red", command=saveas)
b_save.pack(side=LEFT)
    
#**************** GUI ends *************

    
#****** run GUI and main
root.config(menu=menubar)
root.mainloop()
