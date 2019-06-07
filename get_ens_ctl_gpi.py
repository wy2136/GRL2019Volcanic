#!/usr/bin/env python
import os, os.path, sys, datetime
from lib.get_gpi import get_ctl_gpi
from itertools import product

expname = 'CTL1860_noleap_tigercpu_intelmpi_18_576PE'
datanames = ['GPI', 'eta', 'H', 'Vpot', 'Vshear']
year_start = 11
n_ens = 30
n_years = 5

for dataname in datanames:
    get_ctl_gpi(expname=expname, dataname=dataname, 
        year_start=year_start, n_ens=n_ens, n_years=n_years)


