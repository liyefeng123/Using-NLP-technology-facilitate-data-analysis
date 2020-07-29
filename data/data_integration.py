import openpyxl
import pandas as pd
import csv
import files_reader as fr
path_output = r'C:\Users\Alienware\PycharmProjects\Msc-twitter-data\data\output.csv'
def data_acquiring(path_output):
    columns_journey1 = []
    columns_time1 = []
    time_values1 = []
    time_values2 = []
    journey_values1 = []
    speed_values1 = []
    columns_speed1 = []
    sensor_info1 = []
    # for output file
    csvFile = open(path_output, "r")
    dict_reader = csv.DictReader(csvFile)
    # print(dict_reader)
    i = 1
    for row in dict_reader:
        dictionary = row
    date, time = dictionary['time'].split(' ')
    latitude = dictionary['latitude']
    longitude = dictionary['longitude']
    year, month, day = date.split('-')
    hour_output,minute_output,second_output = time.split(':')
    minute_output = round(int(minute_output)/10)*10
    print(hour_output,minute_output)
    loca = 11+int(hour_output)*4 + int(minute_output)//15
    list_path = fr.get_senser_data(latitude,longitude,year,month)
    # creat list for output file
    length = 12
    location = list(range(length))
    reason = list(range(length))
    status = list(range(length))
    latitude = list(range(length))
    longitude = list(range(length))
    Accident_time = list(range(length))

    location.insert(0, dictionary['location'])
    reason.insert(0, dictionary['reason'])
    status.insert(0, dictionary['status'])
    latitude.insert(0, dictionary['latitude'])
    longitude.insert(0, dictionary['longitude'])
    Accident_time.insert(0, dictionary['time'])

    for i in range(length):
        location[i + 1] = None
        reason[i + 1] = None
        status[i + 1] = None
        latitude[i + 1] = None
        longitude[i + 1] = None
        Accident_time[i + 1] = None
    dict = {'location': location, 'reason': reason, 'status': status, 'latitude': latitude, 'longitude': longitude,
         'Accident_time': Accident_time}
    print('success')
##############################################################
    flag = 0
    for a in range(0,len(list_path),2):
        # for journey time
        flag+=1
        workbook1 = openpyxl.load_workbook(list_path[a])
        print(list_path[a])
        sheet_journey = workbook1.active
        for cell in list(sheet_journey.columns)[int(day)]:
            columns_journey1.append(cell.value)
        for i in columns_journey1[loca-3:loca+10]:
            journey_values1.append(i)
        #for time
        for cell in list(sheet_journey.columns)[0]:
            columns_time1.append(cell.value)
        for i in columns_time1[loca - 3:loca + 10]:
            time_values1.append(i)
        for i in columns_time1[5:7]:
            sensor_info1.append(i)
        for i in range(11):
            sensor_info1.append(None)
        #for speed
        workbook2 = openpyxl.load_workbook(list_path[a+1])
        print(list_path[a+1])
        sheet_speed = workbook2.active
        for cell in list(sheet_speed.columns)[int(day)]:
            columns_speed1.append(cell.value)
        for i in columns_speed1[loca-3:loca+10]:
            speed_values1.append(i)
        dict['Info_sensor' + str(flag)] = sensor_info1
        dict['Time of sensor'+ str(flag)] = time_values1
        dict['journey_time of sensor'+ str(flag)] = journey_values1
        dict['speed of sensor'+ str(flag)] = speed_values1
        test = pd.DataFrame(dict)
        test.to_csv('./Msc-twitter-data/data/test.csv', encoding='gbk', index=False)
        journey_values1.clear()
        sensor_info1.clear()
        time_values1.clear()
        speed_values1.clear()
        columns_journey1.clear()
        columns_time1.clear()
        columns_speed1.clear()

    return 0
data_acquiring(path_output)