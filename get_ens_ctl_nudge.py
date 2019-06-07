#!/usr/bin/env python
import os, os.path, sys, datetime
from lib.get_data import get_ctl_data
from itertools import product

expname = 'nudgeclimo_all_model_CTL1860_tigercpu_intelmpi_18_576PE'
compname = 'atmos_month'
datanames = ['netrad_toa', 't_surf', 'precip']
year_start = 111
n_ens = 10
n_years = 5

for dataname in datanames:
    get_ctl_data(expname=expname, compname=compname, dataname=dataname, 
        year_start=year_start, n_ens=n_ens, n_years=n_years)


