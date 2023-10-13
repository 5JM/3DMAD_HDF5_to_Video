# 3DMAD_HDF5_to_Video
HDF5 file conversion code for 3DMAD dataset


---
# The official conversion code for the 3DMAD dataset uses the bob library, but the installation of this library is very unfriendly, so h5py and opencv are used instead.

Reference site: `https://blog.csdn.net/commander_ye/article/details/129327762?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-3-129327762-blog-103137636.235%5Ev38%5Epc_relevant_sort_base1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-3-129327762-blog-103137636.235%5Ev38%5Epc_relevant_sort_base1&utm_relevant_index=6`

---
## How to Use
1. Specify the directory(absolute path) where the data is located in `data_path`. 
2. Just run `main.py`

---
# 3DMAD Dataset Structure
```
..
├── Data # genuine (real face)
│   │   
│   ├── 01_01_01.hdf5
|   ├── 01_01_02.hdf5
│   └── ...
├── Data 2 # genuine (real face)
│   │   
│   ├── 01_02_01.hdf5
|   ├── 01_02_02.hdf5
│   └── ...
└── Data 3 # imposter (mask attack)
    │   
    ├── 01_03_01.hdf5
    ├── 01_03_02.hdf5
    └── ...
```