import csv,sys,os

project_dir =""

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from meters.models import Energy

file=open('user/chart.csv','r') 
for line in file:       
        line = line.replace(",", " ")
        words =line.split()
        inst=Energy()
        inst.date= words[0]
        inst.time= words[1]
        inst.energy = words[2]
        inst.save()
