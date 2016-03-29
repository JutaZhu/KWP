#!/usr/bin/env python
# encoding: utf-8

import math
import sys
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
    args=sys.argv[1:]
    if '-s' in args:
        start=args[1+args.index('-s')].strip()
    else:
        start='1'
    if '-e' in args:
        end=args[1+args.index('-e')].strip()
    else:
        end='/'
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
    r = getr(start,end,d)
    for x in xrange(len(r)):
        print(lettors[r[x]])


    total = []
    for x in xrange(46):
        for y in xrange(46):
            if x != y:
                z = getr(lettors[x],lettors[y],d)
                if len(z)==4:
                    #lettorsz = [ lettors[z[0]], lettors[z[1]], lettors[z[2]], lettors[z[3]],]
                    total.append(z)
    xnyn = []
    for x in xrange(len(total)):
        x1 = total[x]
        for y in xrange(len(total)):
            if len(getp(total[x][3],total[y][0],d))==2:
                y1=total[y]
                xnyn.append([x1[0],x1[1],x1[2],x1[3],y1[0],y1[1],y1[2],y1[3]])
    fl=open('list.txt', 'w')
    for x in xrange(len(xnyn)):
        i = xnyn[x]
        fl.write( lettors[i[0]]+lettors[i[1]]+lettors[i[2]]+lettors[i[3]]+lettors[i[4]]+lettors[i[5]]+lettors[i[6]]+lettors[i[7]])
        fl.write("\n")
    fl.close()
