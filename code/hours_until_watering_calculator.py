import csv


def read_soil_moisture(filename):
    soil_moisture_list = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            soil_moisture_list.append(int(row['Soil_Moisture']))
    return soil_moisture_list


def replace_soil_moisture(filename, soil_moisture_list):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    for i in range(1, len(data)): 
        data[i][-1] = soil_moisture_list[i - 1] 

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

filename = 'Irrigation_scheduling_ML\dataset.csv'
soil_moisture_list = read_soil_moisture(filename)


hours_until_watering = [69,]

soil_hourly_rate= 69/50

i=1

while i < (len(soil_moisture_list)-1):
    temp_value=hours_until_watering[i-1]-((soil_moisture_list[i-1]-soil_moisture_list[i])*soil_hourly_rate)
    hours_until_watering.append(round(temp_value, 3))
    i=i+1

bruh=len(soil_moisture_list)

last_item = hours_until_watering[bruh-2]-((soil_moisture_list[bruh-2]-soil_moisture_list[bruh-1])*soil_hourly_rate)
hours_until_watering.append(round(last_item, 2))

#newfilename = 'Irrigation_scheduling_ML\dataset(new).csv'

replace_soil_moisture(filename, hours_until_watering)

print(soil_moisture_list)
print(hours_until_watering)
    
