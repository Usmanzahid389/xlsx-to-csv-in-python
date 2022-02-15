



import pandas as pd
import os

path = input('Please enter source path')
# foldername = input('Please enter Destination Folder Name')

x = path.split("\\")
foldername = x[6]
 


os.mkdir(foldername) 

# path ="C:/Users/One Call/Desktop/Data/Old/12ApparelGarments"
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        #append the file name to the list
        filelist.append(file)


  
for fi in filelist:
  data = pd.read_excel(os.path.join(root,fi), sheet_name=None)

# loop through the dictionary and save csv
  for sheet_name, df in data.items():
     path_to_output = r'C:/python/Converted'
     temp = path_to_output + foldername+'/';

     filename = temp + fi+sheet_name+'.csv';
     df.to_csv(r''+filename)

   
   
    
