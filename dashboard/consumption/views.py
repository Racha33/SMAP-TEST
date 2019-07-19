# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from consumption.models import (User, Consumption)
from consumption.forms import FormName
from django.http import HttpResponseRedirect
import csv
import pandas as pd
import os
import datetime

# Create your views here.

#### boring homepage with a list of instructions
def HomepageView(request):
    context = {
    }
    return render(request, 'consumption/Homepage.html', context)


### summary view the retruns a table for the under of users and their total consumption
def summary(request):
	dataSource = {}
	dataSource['data'] = []
	Total_sum = 0
	Total_mean = 0
	for key in Consumption.objects.all():
		data = {}
		data['sum'] = key.aggregate
		data['avg'] = 1000*key.average 
		data['user_id'] = key.id_user
		dataSource['data'].append(data)
		Total_sum = Total_sum  + key.aggregate
		Total_mean = Total_mean + key.average
		dataSource['data'].append(data)


	Total_users = User.objects.count()
	Total_mean = int(Total_mean /Total_users)
	query_results = User.objects.all() 
	user_list = [item['user_id'] for item in dataSource['data']]
	sum_list = [item['sum'] for item in dataSource['data']]
	average_list = [item['avg'] for item in dataSource['data']]
	context = locals()
	return render(request, 'consumption/summary.html', context=context)




# Create your views here.
##### The detail view takes in a user ID and in return plots the consumption per day graph for this user. 

def detail(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():

            print("\n\n\n")
            print("Validation SUCCESS!!")
            user_id = int(form.cleaned_data['user_id'])
            print("Name: "+str(user_id))

            data_folder  = os.path.dirname(os.path.dirname(os.path.abspath("data")))
            
            with open(os.path.join(data_folder , "data/user_data.csv"), encoding='utf-8') as data_file:
            	data =pd.read_csv(data_file, index_col = False)
            	if min(data.id) <= user_id  <= max(data.id):

                    #### reading the user's data file from the storage
                    data_file=  data_folder +"/data/consumption/"+str(user_id) +".csv"
                    data =pd.read_csv(data_file, index_col = False)
                    dates = list(data.datetime)
                    consumptions = list(data.consumption)
                    date= list(data .datetime)
                    consumption= list(data.consumption)
                    consumption_bucket = 0
                    result = []
                    ##### converting the dates of this user to readable timestamps from strings and storing them in a list
                    dates_list = [datetime.datetime.strptime(d, '%Y-%m-%d %H:%S:%M').date() for d in date]
                    ##### figuring out how many unique dates exist within this list
                    mylist = list(set(dates_list))
                    mylist.sort()
                    current = (datetime.datetime.strptime(date[0], '%Y-%m-%d %H:%S:%M')).date()
                    i =0
                    # forloop to aggregate the consumption for this user per each day
                    for j in range(len(mylist)):
                        datetime_obj = mylist[j]
                        while ((current == datetime_obj)&(j<len(mylist))&(i<len(dates_list))):
                            current = (datetime.datetime.strptime(date[i], '%Y-%m-%d %H:%S:%M')).date()
                            if current != datetime_obj:
                                continue
                            consumption_obj = consumption[i]
                            consumption_bucket = consumption_obj + consumption_bucket
                            i = i+1

                        result.append(consumption_bucket)
                        consumption_bucket = 0

                    ##### dates and consumptions are the lists that we will use to plot the graph as x and y respectfully 
                    dates = mylist
                    consumptions = result
            	else :
                    return HttpResponseRedirect('http://127.0.0.1:8000/detail/')



    dict = {'form':form}
    ### all the local valuables to be rendered in the detail html page.
    context = locals()
    return render(request,'consumption/detail.html',context=locals())













