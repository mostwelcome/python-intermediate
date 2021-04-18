# import os
# print(os.listdir())
# print(os.getcwd())
# # os.chdir(r'D:\python-workspace\Projects\PythonIntermediate\reading_writing_files')


# It will close the file automatically . No need to close it manually


with open('my_file.txt') as file:
    content = file.read()
    print(content)

with open('my_file.txt',mode='a') as file:
    file.write('new text')


#if the file not found in write mode it will create that file 

# file.close()
