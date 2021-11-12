import LightLinter as LL
import pickle as PI
import SFR2019 as SFR
import CC

SFR.ReadSeparators()


Frinxx = {0:[]}

TK = LL.TK

fi = open('ManualInputForParsing.txt', 'r')
line = fi.read()
fi.close()

ContLI = line.split('==== >>>>')
ContDI = {}
ArtLsDI = {}
LsArtDI = {}

Accs = {0:[],
        1:[]
        }

SE = {}

SelinxxLI = []



LL.Create__root('Amorpha Content Viewer')
LL.Add__one__frame(0, 'root', 1, 1)

LL.Add__one__frame(1, 0, 1, 1)

LL.Add__lx('refsi', 1, 1, 1, 20, 8, 'Courier 15 bold')
LL.TKDI['lx']['refsi']['bg'] = 'black'
LL.TKDI['lx']['refsi']['fg'] = 'yellow'


LL.Add__lx('ainxx', 1, 1, 2, 5, 10, 'Arial 12')
lena = len(ContLI)
array = range(lena)
LL.Fill__lx(array, 'ainxx')


LL.Add__lx('sents', 1, 1, 3, 70, 10, 'Courier 12')

LL.Add__one__frame(2,  0, 2, 1)
LL.Add__lx('selected', 2, 1, 3, 90, 5, 'Courier 14 bold')
LL.TKDI['lx']['selected']['bg'] = 'white'
LL.TKDI['lx']['selected']['fg'] = 'magenta'


LL.Add__one__frame(3, 0, 3, 1)
LL.Add__tx(0, 3, 1, 1, 70, 7, 'black', 'orange', 'Courier 14 bold')
LL.Add__tx(1, 3, 3, 1, 70, 5,  'white', 'black', 'Verdana 12')

CiteDI = {}

#### Content management ))))))


def Refresh__selected():

    array = []
    for seinx in SelinxxLI:
        ls = SE[seinx]['ls']
        array.append(ls)


    LL.Fill__lx(array, 'selected')        

    

def Up():


    cs = int(LL.TKDI['lx']['selected'].curselection()[0])
    value = SelinxxLI.pop(cs)
    prev_pos = cs - 1
    SelinxxLI.insert(prev_pos , value)

    Refresh__selected()

    
def Down():


    cs = int(LL.TKDI['lx']['selected'].curselection()[0])
    value = SelinxxLI.pop(cs)
    next_pos = cs + 1
    SelinxxLI.insert(next_pos , value)

    Refresh__selected()

    
def Del__ls():

    cs = int(LL.TKDI['lx']['selected'].curselection()[0])
    seinx = SelinxxLI.pop(cs)
    ls = SE[seinx]['ls']
    print 'DELETION:\n', ls

    Refresh__selected()
   

def Get__citation(artinx):

    art_inx = artinx

    journal = ContDI[art_inx]['journal']
    ##            ContDI[art_inx]['doi']   = line_1[5:]
    title   = ContDI[art_inx]['title']
    authors = ContDI[art_inx]['authors']
    PMID = ContDI[art_inx]['PMID']
    PMID_line = 'PMID:'+ PMID
    AutiSL = [authors,
                  title,
                  journal,
                  PMID_line]
    auti__line = '. '.join(AutiSL )

    return auti__line



def WriteOverview():

    UN = []
    outfi = open('PreclinicalOverview.txt', 'w')

    for seinx in SelinxxLI:
        
        artinx = SE[seinx]['artinx']

        if artinx not in UN:
            UN.append(artinx)
            CiteDI[artinx] = len(UN)
            
        
    for seinx in SelinxxLI:
        
        ls = SE[seinx]['ls']
        artinx = SE[seinx]['artinx']

        cite_inx = CiteDI[artinx]

        ls += ' ['+str(cite_inx)+'].\n'
        outfi.write(ls)
        
    print '\n\n References:\n\n'
    
    for z in range(len(UN)):
        artinx = UN[z]
        citeline = Get__citation(artinx)
        cite_line = str(z+1)+'. '+citeline+'\n'
        outfi.write(cite_line)

    outfi.close()
    
    print 'WriteOverview: done'



def PrintOverview():

    UN = []

    for seinx in SelinxxLI:
        
        artinx = SE[seinx]['artinx']

        if artinx not in UN:
            UN.append(artinx)
            CiteDI[artinx] = len(UN)
            
        
    for seinx in SelinxxLI:
        
        ls = SE[seinx]['ls']
        artinx = SE[seinx]['artinx']

        cite_inx = CiteDI[artinx]

        ls += ' ['+str(cite_inx)+'].\n'
        print ls
        
    print '\n\n References:\n\n'
    
    for z in range(len(UN)):
        artinx = UN[z]
        citeline = Get__citation(artinx)
        cite_line = str(z+1)+'. '+citeline+'\n'
        print cite_line
    
#################################################

###################################################        


def PrintSelinxxLI():

    for seinx in SelinxxLI:
        print seinx
        ls = SE[seinx]['ls']
        print ls
        print '\n===============\n'
        

def Select__sentence():

    pair = LL.reflect__lx__in__entry('sents')
    frinx = pair[0]
    
    if len(CC.Frinxx[0]) > 0:    
        seinx    = CC.Frinxx[0][frinx]
        SelinxxLI.append(seinx)
        ls = SE[seinx]['ls']
        LL.TKDI['lx']['selected'].insert(TK.END, ls)
        
    

def ShowCC():

    limit = len(SE)
    Accs[1] = []
    
    for y in range(limit):
        ls = SE[y]['ls']              
        Accs[1].append(ls) 

   # line = LL.TKDI['en']['frs'].get()
    line = LL.TKDI['en']['refsi'].get()
    si = line.split('__')[1]
    si = si.strip()

    CC.TargetDI[0] = si
    CC.rl = Accs[1]
    CC.Cc(25, 45)
    LL.TKDI['tx'][0].delete('1.0', TK.END)
    for ls in CC.Accs[0]:
        ls += '\n'
        LL.TKDI['tx'][0].insert(TK.END,  ls)
        

    LL.Fill__lx(CC.Accs[0], 'sents')


def AdjustSE():

    
    #for rawls in Accs[0]:
    for seinx in SE.keys():
        rawls = SE[seinx]['raw']        
        line = rawls.strip()
        if len(line) < 3:
            continue
        
        line = line.lower()
        ls = SFR.ReplacePoints(line)
        ss = ls.split()
        SE[seinx] = {'ls':ls,
                     'ss':ss
                     }
        
    SFR.SE = SE
    print 'AdjustSE: done'
    

def FillArtLsDI():

    seinx = 0
    
    for art_inx in ContDI.keys():
        SentsLI = ContDI[art_inx]['sents']

        for aseinx in range(len(SentsLI)):
            raw_ls = SentsLI[aseinx]

            SE[seinx] = {'raw':raw_ls,
                         'artinx':art_inx,
                         'aseinx':aseinx
                         }
            
            seinx += 1
            
    

def Get__sents():

    ##ContDI[art_inx]['content']

    for art_inx in ContDI.keys():

        content = ContDI[art_inx]['content']

        while content.count('\n\n') > 0:
            content = content.replace('\n\n', '\n')

        content = content.replace('\n', ' ')
        
        while content.count('  ') > 0:            
            content = content.replace('  ', ' ')

        SentsLI = content.split('. ')

        ContDI[art_inx]['sents'] = SentsLI

        


def Get__abstract(SentsLI):

    ab__ls = ''   
    for seinx in range(len(SentsLI)):
        ls = SentsLI[seinx]
        
        if 'Abstract' in ls:

            AbstrSL = SentsLI[seinx+2:]
            ab__ls = '\n'.join(AbstrSL)
            ab__ls = ab__ls.strip()

            break

    return ab__ls


def Get__PMID(SentsLI):

    PMID = ''
    
    for ls in SentsLI:
        if 'PMID:' in ls:
            PMID = ls.split(':')[1]
            PMID = PMID.strip()

            break

    return PMID
            
            

def Get__titles():

    for art_inx in range(len(ContLI)):
        keta = ContLI[art_inx]
        SentsLI = keta.split('\n')

        if len(SentsLI) < 5:

            continue
        
        HeaderLI = SentsLI[:5]

        ContDI[art_inx] = {}
#        print art_inx
        ContDI[art_inx]['journal'] = HeaderLI[1]
##        print ContDI[art_inx]['journal']
##        print '\n============'

        line_2 = HeaderLI[2]
##        print art_inx
##        print line_2
        if 'doi:' in line_2:
            ContDI[art_inx]['doi']   = line_2[5:]
            ContDI[art_inx]['title'] = HeaderLI[3]
            ContDI[art_inx]['authors']= HeaderLI[4]
            
        else:
            ContDI[art_inx]['title'] = HeaderLI[2]
            ContDI[art_inx]['authors']= HeaderLI[3]

        ContDI[art_inx]['PMID'] = Get__PMID(SentsLI)
        ContDI[art_inx]['content'] = Get__abstract(SentsLI)
            
    print 'Get__titles: done'
        

def reflect__selected(event):

    pair = LL.reflect__lx__in__entry('selected')
    sel_inx = pair[0]
    
    seinx = SelinxxLI[sel_inx]
    art_inx = SE[seinx]['artinx']
    
    journal = ContDI[art_inx]['journal']
    ##            ContDI[art_inx]['doi']   = line_1[5:]
    title   = ContDI[art_inx]['title']
    authors = ContDI[art_inx]['authors']
    PMID = ContDI[art_inx]['PMID']
    PMID_line = 'PMID:'+ PMID
    AutiSL = [authors,
                  title,
                  journal,
                  PMID_line]
    auti__line = '\n'.join(AutiSL )

    LL.TKDI['tx'][1].delete('1.0', TK.END)         
    LL.TKDI['tx'][1].insert('1.0', auti__line)

    ls = SE[seinx]['ls']
    LL.TKDI['tx'][0].delete('1.0', TK.END)         
    LL.TKDI['tx'][0].insert('1.0', ls)
    
    

    




def reflect__sent(event):

    pair = LL.reflect__lx__in__entry('sents')
    frinx = pair[0]

    print '\n===== >>>>'
    print 'curr. frinx:', frinx
    
    if len(CC.Frinxx[0]) > 0:
    
        seinx    = CC.Frinxx[0][frinx]
        print 'seinx:', seinx
        
        ls      = SE[seinx]['ls']
        art_inx = SE[seinx]['artinx']
        aseinx  = SE[seinx]['aseinx']
        print 'art_inx:', art_inx
        print 'aseinx', aseinx
        
        LL.TKDI['tx'][0].delete('1.0', TK.END)    
        LL.TKDI['tx'][0].insert('1.0', ls)
        
################### >>>  ###################################

   # if art_inx in ContDI:
        journal = ContDI[art_inx]['journal']
    ##            ContDI[art_inx]['doi']   = line_1[5:]
        title   = ContDI[art_inx]['title']
        authors = ContDI[art_inx]['authors']
        PMID = ContDI[art_inx]['PMID']
        PMID_line = 'PMID:'+ PMID
        AutiSL = [PMID_line,
                  authors,
                  title,
                  journal]
        auti__line = '\n'.join(AutiSL )

        LL.TKDI['tx'][1].delete('1.0', TK.END)         
        LL.TKDI['tx'][1].insert('1.0', auti__line)




def reflect__refsi(event):

    pair = LL.reflect__lx__in__entry('refsi')
    refsi = pair[1].split('__')[0]

    ShowCC()
    
    



def reflect__ainxx(event):

    pair = LL.reflect__lx__in__entry('ainxx')
    art_inx = pair[0]
##    keta = ContLI[art_inx]
##    keta = keta.strip()
    
    LL.TKDI['tx'][0].delete('1.0', TK.END)#    LL.TKDI['tx'][0].insert('1.0', keta)
    LL.TKDI['tx'][1].delete('1.0', TK.END)
    
    if art_inx in ContDI:
        journal = ContDI[art_inx]['journal']
    ##            ContDI[art_inx]['doi']   = line_1[5:]
        title   = ContDI[art_inx]['title']
        authors = ContDI[art_inx]['authors']
        PMID = ContDI[art_inx]['PMID']
        PMID_line = 'PMID:'+ PMID
        AutiSL = [PMID_line,
                  authors,
                  title,
                  journal]
        auti__line = '\n'.join(AutiSL )
        
        LL.TKDI['tx'][1].insert('1.0', auti__line)

        content = ContDI[art_inx]['content']
        LL.TKDI['tx'][0].insert('1.0', content)

#################################################
        SentsLI = ContDI[art_inx]['sents']
        LL.Fill__lx(SentsLI, 'sents')


################################################        

LL.TKDI['lx']['ainxx'].bind('<KeyRelease>',    reflect__ainxx)
LL.TKDI['lx']['ainxx'].bind('<ButtonRelease>', reflect__ainxx)

LL.TKDI['lx']['refsi'].bind('<KeyRelease>',    reflect__refsi)
LL.TKDI['lx']['refsi'].bind('<ButtonRelease>', reflect__refsi)

LL.TKDI['lx']['sents'].bind('<KeyRelease>',    reflect__sent)
LL.TKDI['lx']['sents'].bind('<ButtonRelease>', reflect__sent)

LL.TKDI['lx']['selected'].bind('<KeyRelease>',    reflect__selected)
LL.TKDI['lx']['selected'].bind('<ButtonRelease>', reflect__selected)

def Create__menu():

    LL.Create__menu()

    LL.TKDI['me'][1] = LL.TK.Menu(LL.TKDI['me'][0])    
    LL.TKDI['me'][1].add_command(label = 'Select__sentence', command = Select__sentence)
    LL.TKDI['me'][1].add_command(label = 'PrintSelinxxLI',   command = PrintSelinxxLI)
    LL.TKDI['me'][1].add_separator()
    LL.TKDI['me'][1].add_command(label = 'PrintOverview',   command = PrintOverview)
    LL.TKDI['me'][1].add_command(label = 'WriteOverview',   command = WriteOverview)
    

    LL.TKDI['me'][2] = LL.TK.Menu(LL.TKDI['me'][0])
    LL.TKDI['me'][2].add_command(label = '^^ Up',   command = Up)
    LL.TKDI['me'][2].add_command(label = 'vv Down',   command = Down)
    LL.TKDI['me'][2].add_command(label = 'Delete',   command = Del__ls)
####    
####

    LL.TKDI['me'][0].add_cascade(label = 'Select',    menu = LL.TKDI['me'][1])
    LL.TKDI['me'][0].add_cascade(label = 'Content',   menu = LL.TKDI['me'][2])

def Start():

    Get__titles()
    Get__sents()
    FillArtLsDI()
    #AdjustSE()
    SFR.SE = SE
    SFR.PrepareSE()
    SFR.FillRefsi()

    RefsiOL = [str(ol[0])+'__'+ol[1] for ol in SFR.Ol]
    LL.Fill__lx(RefsiOL, 'refsi')
    
    Create__menu()
    
    

    LL.TKDI['fr']['root'].mainloop()            

Start()

