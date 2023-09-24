import os

#file_path = input("Enter file path:") 

def file_data_to_str(file_path):
    if os.path.isfile(file_path):
        text_file = open(file_path, "r")

        data = text_file.read()

        text_file.close()
        return data
    
def count_each_char(data):
    file_str = data
    print(type(data))
 
    res = {}
 
    for keys in file_str:
        res[keys] = res.get(keys, 0) + 1
 
    return res