import os
import csv
import nltk,re, pprint
import pandas as pd
from geopy import distance
from geopy.geocoders import GoogleV3
def get_senser_data_file():
    filePath = r'C:\Users\Alienware\Desktop\master-project\ThessalonikiSharedFolder\TrafficData\Data'
    List_file = []
    List_name_loc = []
    for i in os.listdir(filePath):
        List_file.append(i)
    print(List_file)
    geolocator = GoogleV3(api_key='AIzaSyDjafRf1OLCAy3FzWjxfUse0VjMJSjy6ao')
    for i in range(len(List_file)):
        I = List_file[i].split("_")
        location = geolocator.geocode(I[2]+ ' ' + 'UK')
        #print(location.latitude,location.longitude)
        temp = 'C:\\Users\Alienware\Desktop\master-project\ThessalonikiSharedFolder\TrafficData\Data\\'+List_file[i]
        List_name_loc.append((I[2],location.latitude, location.longitude,temp.replace('\\','/')))
    print(List_name_loc)
    return List_name_loc

def output_information():
    path_output = r'C:\Users\Alienware\PycharmProjects\Msc-twitter-data\data\output.csv'
    csvFile = open(path_output, "r")
    dict_reader = csv.DictReader(csvFile)
    for row in dict_reader:
        dictionary = row
    date, time = dictionary['time'].split(' ')
    latitude = dictionary['latitude']
    longitude = dictionary['longitude']
    year, month, day = date.split('-')
    return latitude,longitude,year,month

def get_senser_data(latitude,longitude,year,month):
    List_month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    list_distance = []
    list_path = []
    List_name_loc = get_senser_data_file()
    for i in List_name_loc:
        lat_road = i[1]
        lung_road = i[2]
        two_points_distance = distance.distance((latitude,longitude), (lat_road,lung_road)).miles
        print(two_points_distance)
        list_distance.append(two_points_distance)
    ######calculate distance
    for i in range(len(list_distance)):
        if list_distance[i] < 1:
            list_path.append(List_name_loc[i][3])
    print('num of area: ',len(list_path))
    #path = List_name_loc[list_distance.index(min(list_distance))][3]
    output_list = []
    for each_path in list_path:
        filePath = each_path
        List_file = []
        List_detail_file=[]
        for i in os.listdir(filePath):
            List_file.append((filePath + '\\' + i).replace('\\','/'))
        num_route = len(List_file)
        num_file = []
        a = 0
        num_file.append(a)
        for i in List_file:
            for j in os.listdir(i):
                a+=1
                List_detail_file.append(j)
            num_file.append(a)

        for i in range(num_route):
            for j in List_detail_file[num_file[i]:num_file[i+1]]:
                if (j.split('.'))[1] == 'xlsx':
                    if j.split('_')[-1][3:7]==year:
                        if j.split('_')[-1][0:3] == List_month[int(month)-1]:
                            output_list.append((List_file[i] + '\\' + j).replace('\\','/'))
    return output_list
latitude,longitude,year,month = output_information()
print(get_senser_data(latitude,longitude,year,month))

