#!/usr/bin/env python
# coding: utf-8

# In[24]:


import os
import shutil
from glob import glob
import random
import keras
from keras.preprocessing.image import ImageDataGenerator


# In[2]:


get_ipython().system('mkdir "../Breast-Cancer-Detection/split-data"')


# In[3]:


get_ipython().system('mkdir "../Breast-Cancer-Detection/split-data/train"')
get_ipython().system('mkdir "../Breast-Cancer-Detection/split-data/test"')
get_ipython().system('mkdir "../Breast-Cancer-Detection/split-data/valid"')


# In[4]:


get_ipython().system('mkdir "../Breast-Cancer-Detection/split-data/train/zero"')
get_ipython().system('mkdir "../Breast-Cancer-Detection/split-data/train/one"')


# In[5]:


get_ipython().system('mkdir "../Breast-Cancer-Detection/split-data/test/zero"')
get_ipython().system('mkdir "../Breast-Cancer-Detection/split-data/test/one"')


# In[6]:


get_ipython().system('mkdir "../Breast-Cancer-Detection/split-data/valid/zero"')
get_ipython().system('mkdir "../Breast-Cancer-Detection/split-data/valid/one"')


# In[7]:


zero_patch = glob("../Breast-Cancer-Detection/master-dataset/zero/*.png", recursive = True)


# In[8]:


for i in zero_patch[0:3]:
    print(i)


# In[9]:


one_patch = glob("../Breast-Cancer-Detection/master-dataset/one/*.png", recursive = True)


# In[10]:


for i in one_patch[0:3]:
    print(i)


# In[18]:


print(len(zero_patch))


# In[19]:


print(len(one_patch))


# In[34]:


split_1_zero = int(0.7*(len(zero_patch)))
split_2_zero = int(0.85*(len(zero_patch)))


# In[39]:


split_1_one = int(0.7*(len(one_patch)))
split_2_one = int(0.85*(len(one_patch)))


# In[36]:


train_zero = zero_patch[:split_1_zero]
test_zero = zero_patch[split_1_zero:split_2_zero]
valid_zero = zero_patch[split_2_zero:]


# In[37]:


len(train_zero) + len(test_zero) + len(valid_zero)


# In[40]:


train_one = one_patch[:split_1_one]
test_one = one_patch[split_1_one:split_2_one]
valid_one = one_patch[split_2_one:]


# In[41]:


len(train_one) + len(test_one) + len(valid_one)


# In[42]:


for file in train_zero:
    shutil.move(file, "../Breast-Cancer-Detection/split-data/train/zero")
for file in train_one:
    shutil.move(file, "../Breast-Cancer-Detection/split-data/train/one")


# In[43]:


for file in test_zero:
    shutil.move(file, "../Breast-Cancer-Detection/split-data/test/zero")
for file in test_one:
    shutil.move(file, "../Breast-Cancer-Detection/split-data/test/one")


# In[44]:


for file in valid_zero:
    shutil.move(file, "../Breast-Cancer-Detection/split-data/valid/zero")
for file in valid_one:
    shutil.move(file, "../Breast-Cancer-Detection/split-data/valid/one")


# In[ ]:




