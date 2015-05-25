# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

import os
import numpy as np
import nibabel as nib

# The path of FreeROI should be configured first.
# For example: 
# freeroi_path = r'D:\software\freeroi'
freeroi_path = r'/Users/sealhuang/repo/FreeROI/froi'

# voxel coordinates file
# For example: 
# coord_file = r'D:\voxel_coord.csv'
coord_file = r'/Users/sealhuang/repo/python-tutorial/data/voxel_coord.csv'

# Read csv file
coord_info = open(coord_file).readlines()
coord_info = [line.strip().split(',') for line in coord_info]
coord_info = [[int(line[0]), int(line[1]), int(line[2])] for line in coord_info]

mni_template = os.path.join(freeroi_path, 'data', 'standard',
                            'MNI152_T1_2mm_brain.nii.gz')

img = nib.load(mni_template)
header = img.get_header()

# generate a new data, data size is 91x109x91
data = np.zeros((91, 109, 91))

# write each voxel into data matrix
for line in coord_info:
    data[line[0], line[1], line[2]] = 1

# save data matrix as nifti file
header['cal_max'] = data.max()
header['cal_min'] = 0
img = nib.Nifti1Image(data, None, header)
nib.save(img, 'data.nii.gz')

