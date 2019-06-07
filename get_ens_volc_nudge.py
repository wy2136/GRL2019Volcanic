#!/usr/bin/env python
import os, os.path, sys, datetime
from lib.get_data import get_volc_data
from itertools import product

expnames = [f'{volc}_ens_noleap_nudgeclimo_all_model1860' 
    for volc in ('Agung', 'StMaria', 'Pinatubo')]
compname = 'atmos_month'
datanames = ['netrad_toa', 't_surf', 'precip']
ens = range(1, 11)
for expname, dataname in product(expnames, datanames):
    get_volc_data(expname=expname, compname=compname, dataname=dataname, ens=ens)


