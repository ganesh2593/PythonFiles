import os
from datetime import datetime
current_dir=os.getcwd()
print(current_dir)

os.chdir('/Users/Admin/Desktop/')
print(os.getcwd())
# md_time=(os.stat('10thMArkSheet.jpg').st_mtime)
# print(datetime.fromtimestamp(md_time))
#print(os.listdir())
# print(md_time )
# print(os.environ.get('HOME'))
# print(os.path.('/tmp/test.txt'))

for dirpath,dirname,filenames in os.walk('/Users/Admin/Desktop/'):
    print('currentpath:',dirpath)
    print('directories:',dirname)
    print('Filename:',filenames)
