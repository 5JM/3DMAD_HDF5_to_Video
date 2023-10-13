# import torch
import h5py
import os
from tqdm import tqdm
import numpy as np
import cv2
import os

def delete_files(path: str):
    _data_path = path
    sessions = ['Data', 'Data 2', 'Data 3']
    # groups = ['Color_Data', 'Depth_Data', 'Eye_Pos']

    for session in sessions:
        data_path = os.path.join(_data_path, session)
        
        for data in tqdm(os.listdir(data_path)):
            if data.split('.')[-1] == 'avi':
                os.remove(os.path.join(data_path, data))
            
            # t =  data.split('.')
            # if t[-1] == 'avi':
            #     if t[0].split('_')[-1] == 'D':
            #         os.remove(os.path.join(data_path, data))

# https://blog.csdn.net/commander_ye/article/details/129327762?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-3-129327762-blog-103137636.235%5Ev38%5Epc_relevant_sort_base1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-3-129327762-blog-103137636.235%5Ev38%5Epc_relevant_sort_base1&utm_relevant_index=6

def read_3dmad_2_video(path: str):
    _data_path = path
    sessions = ['Data', 'Data 2', 'Data 3']
    # groups = ['Color_Data', 'Depth_Data', 'Eye_Pos']

    for session in sessions:
        data_path = os.path.join(_data_path, session)
        
        for data in tqdm(os.listdir(data_path)):
            print(f'file name: {data}')

            with h5py.File(os.path.join(data_path, data), 'r') as f:
                depth = f['Depth_Data'][:]
                color = f['Color_Data'][:]
                # print(color.shape)
                depth = np.transpose(depth, (0,2,3,1))
                color = np.transpose(color, (0,2,3,1))
                # pos = f.read('Eye_Pos')

                head, tail = os.path.split(os.path.join(data_path, data))
                depth_file = head+'/'+tail.split('.')[0]+'_D.avi'
                color_file = head+'/'+tail.split('.')[0]+'_C.avi'
                
                depth_video = cv2.VideoWriter(
                    depth_file, 
                    cv2.VideoWriter_fourcc(*'XVID'), 
                    30,
                    (depth.shape[2], depth.shape[1]),
                    False
                )

                color_video = cv2.VideoWriter(
                    color_file, 
                    cv2.VideoWriter_fourcc(*'XVID'), 
                    30,
                    (color.shape[2], color.shape[1]),
                    True
                )
                for i in range(0, color.shape[0]):
                    depth_frame = depth[i,:,:,:].astype(np.uint8)
                    color_frame = color[i,:,:,:]
                    color_frame = cv2.cvtColor(color_frame, cv2.COLOR_RGB2BGR)

                    depth_video.write(depth_frame)
                    color_video.write(color_frame)
                depth_video.release()
                color_video.release()

                print(f'Depth video is saved in {depth_file}.')
                print(f'Color video is saved in {color_file}.')

if __name__ == '__main__':
    _data_path = '/Users/jaemu/Desktop/data/3DMAD'

    # delete_files(_data_path)

    read_3dmad_2_video(_data_path)