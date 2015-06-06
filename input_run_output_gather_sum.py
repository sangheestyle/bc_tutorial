
# coding: utf-8

# In[108]:

from time import sleep
import multiprocessing
import os


# In[109]:

# energy plus
def ep(uid):
    val = 0
    with open('config' + str(uid) + '.idf') as fp:
        val = float(fp.readline())
    output = val * val
    output = os.popen("echo " + str(output)).read()
    sleep(5)
    fp = open('result' + str(val) + '.txt', 'w')
    fp.write(str(output))
    fp.close()
    return float(output)


# In[110]:

# generate unique configuration with temperature
def gen_config(uid, temp):
    fp = open('config' + str(uid) + '.idf', 'w')
    fp.write(str(temp))
    fp.close()


# In[111]:

# generate idf with temp
input_param = range(1, 7)
for uid, temp in enumerate(input_param):
    gen_config(uid, temp)


# In[112]:

p = multiprocessing.Pool(7)
uids = range(len(input_param))
sum(p.map(ep, uids))


# In[113]:

# gather and sum
total  = 0
for val in input_param:
    fp = open('result' + str(float(val)) + '.txt', 'r')
    for value in fp:
        total += float(value)
    fp.close()
print total

