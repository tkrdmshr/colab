#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[36]:


def intensity_ratio_to_temperature():
    temperature = pd.read_csv('intensity_increase_ratio.csv')['temperature']
    increase_ratio = pd.read_csv('intensity_increase_ratio.csv')['intensity_ratio']
    z = np.polyfit(increase_ratio, temperature, 3)
    p = np.poly1d(z)
    xp = np.linspace(0.2, 1.2 ,800)
    plt.plot(increase_ratio, temperature, '.', xp, p(xp), '-')
    plt.show()
    return p


# In[37]:


def temperature_to_intensity_ratio():
    temperature = pd.read_csv('intensity_increase_ratio.csv')['temperature']
    increase_ratio = pd.read_csv('intensity_increase_ratio.csv')['intensity_ratio']
    z = np.polyfit(temperature, increase_ratio, 3)
    p = np.poly1d(z)
    xp = np.linspace(19, 39 ,800)
    plt.plot(temperature, increase_ratio, '.', xp, p(xp), '-')
    plt.show()
    return p


# In[38]:


def temperature_to_lifetime():
    temperature = pd.read_csv('lifetime.csv')['temperature']
    increase_ratio = pd.read_csv('lifetime.csv')['lifetime']
    z = np.polyfit(temperature, increase_ratio, 3)
    p = np.poly1d(z)
    xp = np.linspace(19, 39 ,800)
    plt.plot(temperature, increase_ratio, '.', xp, p(xp), '-')
    plt.show()
    return p


# In[43]:


def lifetime_to_temperature():
    temperature = pd.read_csv('lifetime.csv')['temperature']
    lifetime = pd.read_csv('lifetime.csv')['lifetime']
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    xp = np.linspace(4, 9.5 ,800)
    plt.plot(lifetime, temperature, '.', xp, p(xp), '-')
    plt.show()
    return p

