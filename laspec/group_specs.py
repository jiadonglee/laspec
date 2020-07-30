# -*- coding: utf-8 -*-
"""

Author
------
Jiadong Li

Email
-----
jdli@nao.cas.cn

Created on
----------
- Tue Jul 14 17:24:00 2020  groupSpec

Aims
----
- read goups of spectra

"""
import os
import numpy as np
from astropy.io import fits
from .read_spectrum import read_spectrum


class groupSpec():

    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.spec_names = os.listdir(root_dir)
        # remove hidden file of MacOS
        self.spec_names = [f for f in os.listdir(root_dir) if not f.startswith('.')]
        self.spec_names.sort()
        
    def __len__(self):
        length = len(self.spec_names)
        return length

    def __getitem__(self, idx):
        spec_name = os.path.join(self.root_dir, self.spec_names[idx])
        self.spec = read_spectrum(spec_name, filesource='lamost_dr3')
        return self.spec

    def obsid2spec(self, obsid_group, obsid):
        obsids = []
        # for i, spec_name in enumerate(self.spec_names):
        #     spec_name = os.path.join(self.root_dir, self.spec_names[i])
        #     self.spec = read_spectrum(spec_name, filesource='lamost_dr3')
        #     obsids += [self.spec['obsid']]
        # obsids = np.array(obsids)
        idx = np.argwhere(obsid_group == obsid)
        if len(idx)== 1:
            idx = np.asscalar(idx)
        else: 
            return None
        spec_name = os.path.join(self.root_dir, self.spec_names[idx])
        self.spec = read_spectrum(spec_name, 
                                  filesource='lamost_dr3')
        return self.spec

def _test_read_spectrum():
    fp = '/share/data/jdli/preMS/'
    print(fp)
    GroupSpec = groupSpec(fp)
    # print(GroupSpec[1000])
    # return GroupSpec[1000]

if __name__ == "__main__":
    _test_read_spectrum()