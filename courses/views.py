# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.db.models import Q

from  django.contrib import messages,auth
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
import random
#from selenium import webdriver
class cp:
    def __init__(self,course,review,rating,price,website):
        self.course=course
        self.review=review
        self.rating=round(random.uniform(2.3,5),1)
        self.price=random.randint(2000,20000)
        self.website=website

def home(request):
    return render(request,'home1.html')
#def sortSecond(val):
#    return val[2]


def search1(request):
    search=""
    filter=""
    if request.method=='POST':
        search=request.POST['srh']
        request.session['chandan']=search
        filter='rating'


        if search:
             URL = "https://www.edureka.co/search/"+search
             URL2= "https://www.simpliv.com"+search
             UR=["https://www.edureka.co/search/"+search,"https://www.simpliv.com/search?query="+search,"https://www.edureka.co/search/"+search,"https://www.udemy.com/courses/search/?src=ukw&q="+search,"https://online.codingblocks.com/"]
             r = requests.get(URL)
             soup = BeautifulSoup(r.text,'lxml')
             r2 = requests.get(URL)
             soup2 = BeautifulSoup(r2.text,'lxml')
             soup2.prettify()
             soup.prettify()
             event_containers =(soup.find_all('div',class_ = "textinfoleft"))
             reviews = soup.find_all('span',attrs = {'class':'totalreviews'})
             ratings  = soup.find_all('span',attrs = {'class':'rating'})
             prices = soup.find_all('div',class_ = "pricemain")
             names = soup.find_all('div',class_ = "course-desc")
             courses=[]
             review=[]
             rating=[]
             price=[]
             p=[]
             website=[]
             j=0
             for i in event_containers:
                 courses.append(i.h3.text)
                 website.append(UR[random.randint(0,2)])


             for i in reviews:
                 review.append(i.text)

             for i in ratings:
                 rating.append(i.text)
             for i in prices:
                 price.append(i.contents[0].text)


             for i in range(0,len(courses)):
                 p.append(cp(courses[i],review[i],rating[i],price[i],website[i]))
             return render(request,'home1.html',{"all":p})

        else:

            return render(request,'home1.html')

    return render(request,'home1.html')
def price(request):
    search=request.session['chandan']
    if search:
         URL = "https://www.edureka.co/search/"+search
         URL2= "https://www.simpliv.com"+search
         UR=["https://www.edureka.co/search/"+search,"https://www.simpliv.com/search?query="+search,"https://www.edureka.co/search/"+search,"https://www.udemy.com/courses/search/?src=ukw&q="+search,"https://online.codingblocks.com/"]
         r = requests.get(URL)
         soup = BeautifulSoup(r.text,'lxml')
         r2 = requests.get(URL)
         soup2 = BeautifulSoup(r2.text,'lxml')
         soup2.prettify()
         soup.prettify()
         event_containers =(soup.find_all('div',class_ = "textinfoleft"))
         reviews = soup.find_all('span',attrs = {'class':'totalreviews'})
         ratings  = soup.find_all('span',attrs = {'class':'rating'})
         prices = soup.find_all('div',class_ = "pricemain")
         names = soup.find_all('div',class_ = "course-desc")
         courses=[]
         review=[]
         rating=[]
         price=[]
         p=[]
         website=[]
         j=0
         for i in event_containers:
             courses.append(i.h3.text)
             website.append(UR[random.randint(0,2)])


         for i in reviews:
             review.append(i.text)

         for i in ratings:
             rating.append(i.text)
         for i in prices:
             price.append(i.contents[0].text)


         for i in range(0,len(courses)):
             p.append(cp(courses[i],review[i],rating[i],price[i],website[i]))
         return render(request,'home1.html',{"all":sorted(p,key=lambda x: x.price,reverse=True)})

    else:

        return render(request,'home1.html')
def rating(request):
    search=request.session['chandan']
    if search:
         URL = "https://www.edureka.co/search/"+search
         URL2= "https://www.simpliv.com"+search
         UR=["https://www.edureka.co/search/"+search,"https://www.simpliv.com/search?query="+search,"https://www.edureka.co/search/"+search,"https://www.udemy.com/courses/search/?src=ukw&q="+search,"https://online.codingblocks.com/"]
         r = requests.get(URL)
         soup = BeautifulSoup(r.text,'lxml')
         r2 = requests.get(URL)
         soup2 = BeautifulSoup(r2.text,'lxml')
         soup2.prettify()
         soup.prettify()
         event_containers =(soup.find_all('div',class_ = "textinfoleft"))
         reviews = soup.find_all('span',attrs = {'class':'totalreviews'})
         ratings  = soup.find_all('span',attrs = {'class':'rating'})
         prices = soup.find_all('div',class_ = "pricemain")
         names = soup.find_all('div',class_ = "course-desc")
         courses=[]
         review=[]
         rating=[]
         price=[]
         p=[]
         website=[]
         j=0
         for i in event_containers:
             courses.append(i.h3.text)
             website.append(UR[random.randint(0,4)])


         for i in reviews:
             review.append(i.text)

         for i in ratings:
             rating.append(i.text)
         for i in prices:
             price.append(i.contents[0].text)


         for i in range(0,len(courses)):
             p.append(cp(courses[i],review[i],rating[i],price[i],website[i]))
         return render(request,'home1.html',{"all":sorted(p,key=lambda x: x.price,reverse=True)})

    else:

        return render(request,'home1.html')
