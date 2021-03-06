#!/usr/bin/env python
# encoding: utf-8

import math
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
_=float('inf')

#最短路径算法(Dijkstra) 
def dijkstra(graph,n,k):  
    dis=[0]*n  
    flag=[False]*n
    flag[0]=True  
    k=k
    for i in range(n):  
        dis[i]=graph[k][i]  
  
    for j in range(n-1):  
        mini=_  
        for i in range(n):  
            if dis[i]<mini and not flag[i]:  
                mini=dis[i]  
                k=i  
        if k==0:
            return  
        flag[k]=True  
        for i in range(n):  
            if dis[i]>dis[k]+graph[k][i]:  
                dis[i]=dis[k]+graph[k][i]
    return dis

def getd():
    d=[_]*46
    for a in xrange(46):
        d[a] = dijkstra(graph,46,a)
    return d

def getp(i,j,d):
    p = []
    for a1 in xrange(46):
        if d[i][a1]+d[j][a1]==d[i][j]:
            p.append(a1)
    return p

def getr(i,j,d):
    i = lettors.find(i)
    j = lettors.find(j)
    r = [i]
    newi = i
    t = True
    while t:
        t = False
        for a1 in xrange(46):
            if d[newi][a1]+d[j][a1]==d[newi][j]:
                if len(getp(newi,a1,d))==2:
                    r.append(a1)
                    newi = a1
                    t = True
                    #print a1
    return r

if __name__=='__main__':
    starttime = time.time()
    lettors = "1234567890-=\qwertyuiop[]asdfghjkl;'zxcvbnm,./"
    xy = [[0,0]]*46
    y = 0
    r = 0
    i = 0
    for x in xrange(46):
        xy[x]=[i+r,y]
        i+=1
        if x==12 or x==24 or x==35:
            y+=-1
            r+=0.5
            i=0
    graph = [[_]*46]*46

    for i in xrange(46):
        listd = [_]*46
        x0 = xy[i][0]
        y0 = xy[i][1]
        for j in xrange(46):
            x1 = xy[j][0]
            y1 = xy[j][1]
            if abs(x1-x0)<=1 and abs(y1-y0)<=1:
                d = math.sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0))
                listd[j]=d
        graph[i] = listd

    d = getd()
    
    total = []
    for x in xrange(46):
        for y in xrange(46):
            if x != y:
                z = getr(lettors[x],lettors[y],d)
                if len(z)==4 or len(z)==3:
                    total.append(z)
    xnyn = []
    for x in xrange(len(total)):
        x1 = total[x]
        xend = len(x1)-1
        for y in xrange(len(total)):

            if len(getp(total[x][xend],total[y][0],d))<=2 or len(getp(total[x][0],total[y][0],d))<=2:
                y1=total[y]
                x1y1=[]
                for i in xrange(len(x1)):
                    x1y1.append(x1[i])
                for j in xrange(len(y1)):
                    x1y1.append(y1[j])
                xnyn.append(x1y1)
    fl=open('list.txt', 'w')

    for x in xrange(len(xnyn)):
        i = xnyn[x]
        line = ""
        for j in xrange(len(i)):
            line += lettors[i[j]]
        fl.write(line)
        fl.write("\n")
    fl.close()
    endtime = time.time()
    print(u"共生成了"+str(len(xnyn))+u"条字典,共用时"+str(endtime-starttime)+u"秒")
