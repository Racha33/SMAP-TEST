from django.core.management.base import BaseCommand
import os
import csv
import pandas as pd
from consumption.models import (User, Consumption)
from django.core.management.base import BaseCommand

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath("user_data.csv")))



class Command(BaseCommand):
    def import_user_from_csv_file(self):

        data_folder = os.path.join(BASE_DIR, 'data')
        print(data_folder, 'data_folder')
        with open(os.path.join(data_folder, "user_data.csv"), encoding='utf-8') as data_file:
        	data = csv.reader(data_file)
        	for data_object in data:
        		id_user = data_object[0]
        		area = data_object[1]
        		tariff= data_object[2]

        		try:
        			user, created = User.objects.get_or_create(
        				id_user = id_user ,
        				area = area,
        				tariff= tariff
        				)
        			if created:

        				user.save()
        				display_format = "\nUser, {}, has been saved."
        				print(display_format.format(user))
        		except Exception as ex:
        			print(str(ex))
        			msg = "\n\nSomething went wrong saving this user: {}\n{}".format(title, str(ex))
        			print(msg)


    def import_consumption_from_csv_file(self):
        data_folder = os.path.join(BASE_DIR, 'data/consumption')
        print(data_folder, 'data_folder')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = pd.DataFrame.from_csv(data_file)
                id_user= (data_file.name.split("consumption/")[1].split(".")[0])
                aggregate = int(data.sum())
                average = int(data.mean())

                try:
                	consumption, created = Consumption.objects.get_or_create(
                		id_user= id_user,
                		aggregate =aggregate,
                		average = average
                		)
                	if created:
                		consumption.save()
                		display_format = "\nConsumption, {}, has been saved."
                		print(display_format.format(consumption))
                except Exception as ex:
                	print(str(ex))
                	msg = "\n\nSomething went wrong saving consumption data: {}\n{}"
                	print(msg)


    def handle(self, *args, **options):
        """
        Call the function to import data
        """
        self.import_user_from_csv_file()
        self.import_consumption_from_csv_file()





