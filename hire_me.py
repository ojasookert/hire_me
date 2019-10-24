#!/usr/bin/python

from datetime import date, timedelta
from time import sleep
from subprocess import call


today = date.today()
start_date = today - timedelta(days=today.weekday()+2, weeks=52)

# should correspond to the first contribution box on github
# print start_date.ctime()

matrix = """
....................................................
....................................................
.........#        #   #                       #    #
.........### ###  #   #  ###     # # ### ###  #  ###
.........# # ##   #   #  # #     ### # # #    #  # #
.........# # ###  ##  ## ###     ### ### #    ## ###
....................................................

"""

lines = matrix.strip().split("\n")
columns = zip(*lines)

counter = 0


call(['rm','-rf','.git','delta.txt'])
call(['git','init'])

def write_delta(d):
  f = open('delta.txt', 'w')
  f.write(str(d))
  f.close()


call(['git','add','-A'])
call(['git','commit','-am','Initial commit','--author','Kert Ojasoo <ojasookert@gmail.com>'])

for c in columns:
  for d in c:
    counter += 1
    if d != "#":
	  continue
    write_delta(counter)
    call(['git','add','-A'])
    call(['git','commit','--date',(start_date + timedelta(days=counter)).ctime(),'-am',str(counter),'--author','Kert Ojasoo <ojasookert@gmail.com>'])
