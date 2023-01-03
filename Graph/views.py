from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from Graph.models import FileDir,FileAxis
import pandas as pd
import os
import plotly.express as px

def Startup(request):
    if request.method =='POST':
        myfile = request.FILES['myfile']
        XAxis = request.POST['XAxis']
        YAxis = request.POST['YAxis']
        print('csv',myfile)
        if myfile.name.endswith('.csv'):
            save_myfile=FileSystemStorage()
        
            name = save_myfile.save(myfile.name,myfile)
        
            d = os.getcwd()
            fd = d+'\media\\'+name

            input = FileDir(FileDir=fd)
            input2 = FileAxis(XAxis=XAxis,YAxis=YAxis)
            input.save()
            input2.save()
    return render(request,'index.html')

def histogram(request):
        mylist=[]
        xmas=FileAxis.objects.all().last()
        xmas=str(xmas)
        mylist=xmas.split()
        myxaxis=mylist[0]
        myyaxis=mylist[1]
        fd = FileDir.objects.all().last()
        fd=str(fd)
        df = pd.read_csv(fd)
        fig1 = px.histogram(df, x=df[myxaxis], y=df[myyaxis]).show
        return render(request,'index.html',context={'fig1':fig1})
def scatterPlot(request):
        mylist=[]
        xmas=FileAxis.objects.all().last()
        xmas=str(xmas)
        mylist=xmas.split()
        myxaxis=mylist[0]
        myyaxis=mylist[1]
        fd = FileDir.objects.all().last()
        fd=str(fd)
        df = pd.read_csv(fd)
        fig1 = px.scatter(df, x=df[myxaxis], y=df[myyaxis]).show
        return render(request,'index.html',context={'fig1':fig1})
def barGraph(request):
        mylist=[]
        xmas=FileAxis.objects.all().last()
        xmas=str(xmas)
        mylist=xmas.split()
        myxaxis=mylist[0]
        myyaxis=mylist[1]
        fd = FileDir.objects.all().last()
        fd=str(fd)
        df = pd.read_csv(fd)
        fig1 = px.bar(df, x=df[myxaxis], y=df[myyaxis]).show
        return render(request,'index.html',context={'fig1':fig1})
def lineGraph(request):
        mylist=[]
        xmas=FileAxis.objects.all().last()
        xmas=str(xmas)
        mylist=xmas.split()
        myxaxis=mylist[0]
        myyaxis=mylist[1]
        fd = FileDir.objects.all().last()
        fd=str(fd)
        df = pd.read_csv(fd)
        fig1 = px.line(df, x=df[myxaxis], y=df[myyaxis]).show
        return render(request,'index.html',context={'fig1':fig1})
def GraphView(request):
        mylist=[]
        xmas=FileAxis.objects.all().last()
        xmas=str(xmas)
        mylist=xmas.split()
        myxaxis=mylist[0]
        myyaxis=mylist[1]
        fd = FileDir.objects.all().last()
        fd=str(fd)
        df = pd.read_csv(fd)
        fig1 = px.density_heatmap(df, x=df[myxaxis], y=df[myyaxis]).show
        return render(request,'index.html',context={'fig1':fig1})

