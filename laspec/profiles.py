#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
'''
Edited by @Jiadong LI

Email
-----
jdli@nao.cas.cn

Created on
----------
- Tue Jul 28 14:33 2020

Line Index organized by Chao Liu
Spectral classification of stars based on LAMOST spectra
RAA 2015 Vol. 15 No. 8, 1137–1153 doi: 10.1088/1674–4527/15/8/004

Aims

----
collect line index
'''
class Lines_info():
    def __init__(self):
        self.Hgamma = { 'line_center':          4342.13,
                        'line_range':          (4319.75, 4363.50),
                        'line_shoulder_left':  (4283.50, 4319.75),
                        'line_shoulder_right': (4367.25, 4419.75)}

        self.G4300 = { 'line_center':          4300.13,
                        'line_range':          (4282.625, 4317.625),
                        'line_shoulder_left':  (4267.625, 4283.875),
                        'line_shoulder_right': (4320.125, 4336.375)}

        self.Fe4383 = { 'line_center':          4396.0,
                        'line_range':          (4370.375, 4421.625),
                        'line_shoulder_left':  (4360.375, 4371.625),
                        'line_shoulder_right': (4444.125, 4456.625)}
        
        self.Fe4531 = { 'line_center':          4538.0,
                        'line_range':          (4515.50, 4560.50),
                        'line_shoulder_left':  (4505.50, 4515.50),
                        'line_shoulder_right': (4561.75, 4580.50)}

        self.Fe4668 = { 'line_center':          4678.375,
                        'line_range':          (4635.250, 4721.500),
                        'line_shoulder_left':  (4612.750, 4631.500),
                        'line_shoulder_right': (4744.000, 4757.750)}

        self.Fe5015 = { 'line_center':          5015.875,
                        'line_range':          (4977.750, 5054.000),
                        'line_shoulder_left':  (4946.500, 4977.750),
                        'line_shoulder_right': (5054.000, 5065.250)}

        self.Fe5270 = { 'line_center':          5265.65,
                        'line_range':          (5245.650, 5285.650),
                        'line_shoulder_left':  (5233.150, 5248.150),
                        'line_shoulder_right': (5285.650, 5318.150)}

        self.Fe5335 = { 'line_center':          5332.125,
                        'line_range':          (5312.125, 5352.125),
                        'line_shoulder_left':  (5304.625, 5315.875),
                        'line_shoulder_right': (5353.375, 5363.375)}

        self.Fe5406 = { 'line_center':          5401.25,
                        'line_range':          (5387.500, 5415.000),
                        'line_shoulder_left':  (5376.250, 5387.500),
                        'line_shoulder_right': (5415.000, 5425.000)}

        self.Fe5709 = { 'line_center':          5710.25,
                        'line_range':          (5698.375, 5722.125),
                        'line_shoulder_left':  (5674.625, 5698.375),
                        'line_shoulder_right': (5724.625, 5738.375)}

        self.Fe5782 = { 'line_center':          5788.375,
                        'line_range':          (5778.375, 5798.375),
                        'line_shoulder_left':  (5767.125, 5777.125),
                        'line_shoulder_right': (5799.625, 5813.375)}

        self.Mg1 = { 'line_center':          5101.625,
                     'line_range':          (5069.125, 5134.125),
                     'line_shoulder_left':  (4895.125, 4957.625),
                     'line_shoulder_right': (5301.125, 5366.125)}

        self.Mg2 = { 'line_center':          5175.375,
                     'line_range':          (5154.125, 5196.625),
                     'line_shoulder_left':  (4895.125, 4957.625),
                     'line_shoulder_right': (5301.125, 5366.125)}

        self.Mgb = { 'line_center':          5176.375,
                     'line_range':          (5160.125, 5192.625),
                     'line_shoulder_left':  (5142.625, 5161.375),
                     'line_shoulder_right': (5191.375, 5206.375)}
        
        self.TiO2 = { 'line_center':          6232.625,
                      'line_range':          (6191.375, 6273.875),
                      'line_shoulder_left':  (6068.375, 6143.375),
                      'line_shoulder_right': (6374.375, 6416.875)}
        
        self.Fe = [self.Fe4383, self.Fe4531, self.Fe4668, self.Fe5015, 
                   self.Fe5270, self.Fe5335, self.Fe5406, self.Fe5709, 
                   self.Fe5782]
        
        self.Mg = [self.Mg1, self.Mg2, self.Mgb]