from django.shortcuts import render
from django.http import HttpResponse

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv


def home(request):

    aa = request.user

    a = {
        'a': aa,
    }
    rhks_y = pd.read_csv("./static/csv/rhks_y.csv")
    plt.figure(figsize=(30,6))
    plt.xlabel("year")
    plt.ylabel("The number of viewer")
    plt.plot(rhks_y['year'], rhks_y['a'], label='Domestic')
    plt.plot(rhks_y['year'], rhks_y['b'], label='Overseas')
    plt.plot(rhks_y['year'], rhks_y['c'], label='Sum')
    plt.xticks([i for i in range(2004, 2022)])
    plt.yticks([i for i in range(0, 250000001, 50000000)])
    plt.legend()
    plt.grid(True, axis='y')
    plt.savefig("./static/image/Total.png")

    return render(request, 'index.html', a)


def M2004(request):

    plot = pd.read_csv("./static/csv/2004.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2004.png")

    m_m = pd.read_csv("./static/csv/m2004.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2004.png")

    
    path = "./static/csv/m2004.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2004.html', tuples)


def M2005(request):

    plot = pd.read_csv("./static/csv/2005.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2005.png")

    m_m = pd.read_csv("./static/csv/m2005.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2005.png")

    
    path = "./static/csv/m2005.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2005.html', tuples)


def M2006(request):

    plot = pd.read_csv("./static/csv/2006.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2006.png")

    m_m = pd.read_csv("./static/csv/m2006.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2006.png")

    
    path = "./static/csv/m2006.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2006.html', tuples)


def M2007(request):

    plot = pd.read_csv("./static/csv/2007.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2007.png")

    m_m = pd.read_csv("./static/csv/m2007.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2007.png")

    
    path = "./static/csv/m2007.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2007.html', tuples)


def M2008(request):

    plot = pd.read_csv("./static/csv/2008.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2008.png")

    m_m = pd.read_csv("./static/csv/m2008.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2008.png")

    
    path = "./static/csv/m2008.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2008.html', tuples)


def M2009(request):

    plot = pd.read_csv("./static/csv/2009.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2009.png")

    m_m = pd.read_csv("./static/csv/m2009.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2009.png")

    
    path = "./static/csv/m2009.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2009.html', tuples)


def M2010(request):

    plot = pd.read_csv("./static/csv/2010.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2010.png")

    m_m = pd.read_csv("./static/csv/m2010.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2010.png")

    
    path = "./static/csv/m2010.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2010.html', tuples)

def M2011(request):

    plot = pd.read_csv("./static/csv/2011.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2011.png")

    m_m = pd.read_csv("./static/csv/m2011.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2011.png")

    
    path = "./static/csv/m2011.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2011.html', tuples)

def M2012(request):

    plot = pd.read_csv("./static/csv/2012.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2012.png")

    m_m = pd.read_csv("./static/csv/m2012.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2012.png")

    
    path = "./static/csv/m2012.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2012.html', tuples)

def M2013(request):

    plot = pd.read_csv("./static/csv/2013.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2013.png")

    m_m = pd.read_csv("./static/csv/m2013.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2013.png")

    
    path = "./static/csv/m2013.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2013.html', tuples)

def M2014(request):

    plot = pd.read_csv("./static/csv/2014.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2014.png")

    m_m = pd.read_csv("./static/csv/m2014.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2014.png")

    
    path = "./static/csv/m2014.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2014.html', tuples)

def M2015(request):

    plot = pd.read_csv("./static/csv/2015.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2015.png")

    m_m = pd.read_csv("./static/csv/m2015.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2015.png")

    
    path = "./static/csv/m2015.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2015.html', tuples)

def M2016(request):

    plot = pd.read_csv("./static/csv/2016.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2016.png")

    m_m = pd.read_csv("./static/csv/m2016.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2016.png")

    
    path = "./static/csv/m2016.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2016.html', tuples)

def M2017(request):

    plot = pd.read_csv("./static/csv/2017.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2017.png")

    m_m = pd.read_csv("./static/csv/m2017.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2017.png")

    
    path = "./static/csv/m2017.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2017.html', tuples)

def M2018(request):

    plot = pd.read_csv("./static/csv/2018.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2018.png")

    m_m = pd.read_csv("./static/csv/m2018.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2018.png")

    
    path = "./static/csv/m2018.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2018.html', tuples)

def M2019(request):

    plot = pd.read_csv("./static/csv/2019.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2019.png")

    m_m = pd.read_csv("./static/csv/m2019.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2019.png")

    
    path = "./static/csv/m2019.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2019.html', tuples)

def M2020(request):

    plot = pd.read_csv("./static/csv/2020.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2020.png")

    m_m = pd.read_csv("./static/csv/m2020.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2020.png")

    
    path = "./static/csv/m2020.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2020.html', tuples)

def M2021(request):

    plot = pd.read_csv("./static/csv/2021.csv")
    plt.figure(figsize=(14,7))
    plt.xlabel("month")
    plt.ylabel("The number of viewer")
    plt.plot(plot['year'], plot['a'], 'o-',label='Domestic')
    plt.plot(plot['year'], plot['b'], 'o-', label='Overseas')
    plt.plot(plot['year'], plot['c'], 'o:', label='Sum')
    plt.xticks([i for i in range(1, 13)])
    plt.yticks([i for i in range(0, 32000001, 2000000)])
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig("./static/image/2021.png")

    m_m = pd.read_csv("./static/csv/m2021.csv")
    plt.figure(figsize=(14,7))
    plt.ylabel("The number of viewer")
    plt.bar(m_m['c'], m_m['e'], color=['cornflowerblue'], width=0.3)
    plt.savefig("./static/image/m2021.png")

    
    path = "./static/csv/m2021.csv"
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print(reader)

    list = []
    for row in reader:
        list.append(row)

    list[1]
    tuples = {'m_m1' : list[1],
            'm_m2' : list[2],
            'm_m3' : list[3],
            'm_m4' : list[4],
            'm_m5' : list[5],
            'm_m6' : list[6],
            'm_m7' : list[7],
            'm_m8' : list[8],
            'm_m9' : list[9],
            'm_m10' : list[10]}

    return render(request, 'm2021.html', tuples)