import random
import csv

def generator():
    data_dict={}
    dt=random.randint(1, 100)
    dp=random.randint(1, 100)
    dw=random.randint(1, 100)
    dh=random.randint(1, 100)
    dhu=random.randint(1, 100)
    data_dict['T']=dt
    data_dict['P']=dp
    data_dict['W']=dw
    data_dict['H']=dh
    data_dict['HU']=dhu
     # Write data_dict to a CSV file
    with open('data.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data_dict.keys())
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(data_dict)


    return data_dict

#//generator()