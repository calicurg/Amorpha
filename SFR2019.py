#!/usr/bin/python

#import Refsi
import os
import pickle  as PI



##SourceDI = {0:'Telaprevir_2011_2019.txt',
##            1:'PaliperidonSafetySummary.txt'
##            }

Accs = {0:[],
        1:[],
        2:[]
        }

ParamDI = {'f':'',
           'finx':15
			 ## file index in
                          ## D:\__May2019\NewSources\ directory
           }

SE = {}

AntPoints  = ['(', '[', '{', '<']
PostPoints = [')', ']', '}', '>', ',', ';', ':', '"']

Refsi = {}
Refinxx = {}
Ol    = []

Reffrs = {}
FrOl    = []

RiFR = {}

#### syntax

PrepLI = []
ConjLI = []
ModVerbsLI = []
#AllSeps = []
ArtLI  = ['a', 'an', 'the']



AllSeparators = []
##PrepLI + ConjLI + ModVerbsLI + ArtLI+\
##                         AntPoints + PostPoints


def DumpSE():

    fi = open('SE.li', 'wb')
    PI.dump(SE, fi)
    fi.close()

    print 'DumpSE: done'


def FillRiFR():

    for fr in Reffrs.keys():
        if ' ' in fr:
            slfr = fr.split()
            risi = slfr[-1]
        else:
            risi = fr

        if risi in RiFR:
            RiFR[risi].append(fr)
        else:
            RiFR[risi] = [fr]
            
    print 'FillRiFR: done'

        

def ReadSeparators():

    dna = 'D:/__May2019/syntax/'

    fn = dna + 'mono_conjunctions.txt' 
    fi = open(fn, 'r')
    rl = fi.readlines()
    fi.close()
    
    for si in rl:
        si = si.strip()
        ConjLI.append(si)
        Accs[1].append(si)
        
    fn = dna + 'mono_preposition.txt'
    fi = open(fn, 'r')
    rl = fi.readlines()
    fi.close()

    for si in rl:
        si = si.strip()
        PrepLI.append(si)
        Accs[1].append(si)

    fn = dna + 'modal_verbs.txt' 
    fi = open(fn, 'r')
    rl = fi.readlines()
    fi.close()

    for si in rl:
        si = si.strip()
        ModVerbsLI.append(si)
        Accs[1].append(si)


    Accs[1]  +=  ArtLI
    Accs[1]  += AntPoints
    Accs[1]  += PostPoints   

    print 'ReadSeparators: done'   


def FillReffrs():

    FragmentSeparators = PrepLI + ConjLI + ModVerbsLI + ArtLI+\
                         AntPoints + PostPoints
#    AllPoints = AntPoints + PostPoints

    AllFrs = []
    
    fr = []
    for seinx, v in SE.items():
        ss = v['ss']
        for si in ss:
##            if si in AllPoints:
##                continue
            if si in FragmentSeparators:
                if len(fr) > 1:
                    linfr = ' '.join(fr)
                    AllFrs.append(linfr)
                fr = []
            else:
                fr.append(si)

                
    for linfr in AllFrs:
        
        if linfr in Reffrs:
            Reffrs[linfr] += 1
        else:
            Reffrs[linfr] = 1
                    
    print 'Reffrs filled'

    for linfr, inci in Reffrs.items():
        ol = [inci, linfr]
        FrOl.append(ol)

    FrOl.sort()
    FrOl.reverse()

    for olinx in range(45):
        ol = FrOl[olinx]
        print ol



def FillRefsi():

    for seinx, v in SE.items():
        ss = v['ss']
        for sinx in range(len(ss)):
            si = ss[sinx]
            if si in Accs[1]:
                continue
            
            if si in Refsi:
                Refsi[si] += 1
                Refinxx[si].append([sinx, seinx])                
                
            else:
                Refsi[si] = 1
                Refinxx[si] = [
                                [sinx, seinx]
                               ]
                
    print 'Refsi filled'

    for si, inci in Refsi.items():
        ol = [inci, si]
        Ol.append(ol)

    Ol.sort()
    Ol.reverse()

    for olinx in range(15):
        ol = Ol[olinx]
        print ol

    

def ReplacePoints(source_line):

    line = source_line
    for point in AntPoints:
        if point in line:
            filler = point + ' '
            line = line.replace(point, filler)
            
    for point in PostPoints:
        if point in line:
            filler = ' '+point
            line = line.replace(point, filler)

    return line

def PrepareSE():

    seinx = 0
    
    for seinx, v in SE.items():
        rawls = v['raw']
        line = rawls.strip()
##        if len(line) < 3:
##            continue
        
        line = line.lower()
        ls = ReplacePoints(line)
        ss = ls.split()
        SE[seinx]['ls'] = ls
        SE[seinx]['ss'] = ss
                     
        
    print 'FillSE: done'

    
def FillSE():

    seinx = 0
    
    for rawls in Accs[0]:
        line = rawls.strip()
        if len(line) < 3:
            continue
        
        line = line.lower()
        ls = ReplacePoints(line)
        ss = ls.split()
        SE[seinx] = {'ls':ls,
                     'ss':ss
                     }
        seinx += 1
        
    print 'FillSE: done'

def ReadSource():

    dna = 'D:/__May2019/NewSources/'
    FiLI = os.listdir(dna)
##    for fn in FiLI:
##        print fn


    finx = ParamDI['finx']    
    fn = FiLI[finx]##2]
    ParamDI['f'] = fn
    #LL.TKDI['la'][0]
    print 'SELECTED:', fn
    
    fn  = dna+fn
    fi = open(fn, 'r')
    line = fi.read()
    fi.close()

    line = line.replace('vs.', 'vs')
    line = line.replace('.\n', '. ')
    line = line.replace('\n', '. ')
    rl = line.split('. ')

    Accs[0] = rl

    print 'Total: ', len(Accs[0]), 'raw sents'
    
    print 'ReadSource: done'

    
def Start():

    ReadSource()
    ReadSeparators()
    FillSE()
#    DumpSE()
    FillRefsi()
    FillReffrs()
    FillRiFR()

#Start()

    
