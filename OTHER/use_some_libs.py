import requests
import os
import sys
import glob
import shutil
from datetime import datetime
import random
r = requests.get('http://ya.ru')
r.status_code	# -> 200, if ok
r.text			# -> html page

sys.argv # входящие параметры для запуска исполняемого файла из терминала [0 - имя самого файла, 1 - первый параметр, ...]
sys.path # [list of PATH directories]
os.getcwd() # current work directory
sys.path.append(os.getcwd()) # insert into PATH current work directry
os.mkdir('new_dir') # создаёт директорию в .
os.rmdir('new_dir')

os.path.join('C:/Games/','NEO Scavenger') # правильно добавляет файловые пути

glob.glob('*') # show all files in work directory

shutil.copy('src', 'dest')

now = datetime.now() # текущая дата
d.date() # only date

r = int(random.random()*10)
rr = random.randrange(1,40)
rc = random.choise([0,1,2,3,4,5,6,7,8,9,10,11,12]) # random choise from sequence
