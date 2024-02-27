import os
import json
from tqdm import tqdm
import argparse
import shutil
 
parser = argparse.ArgumentParser()
#这里根据自己的json文件位置，换成自己的就行
parser.add_argument('--origin_path', default='data/dfs_semi/imgs',type=str, help="input:image origin path")
parser.add_argument('--json_path', default='data/dfs_semi/annotations/trainval.json',type=str, help="input: coco format(json)")
parser.add_argument('--save_path', default='data/dfs_semi/trainval/', type=str, help="specify where to save the output dir of labels")
arg = parser.parse_args()
 
if __name__ == '__main__':
    json_file = arg.json_path # COCO Object Instance 类型的标注
    save_path = arg.save_path  # 保存的路径
    origin_path=arg.origin_path
 
    data = json.load(open(json_file, 'r'))
    imgs = data["images"]
    # file_names = imgs["file_name"]
    # data2 = json.load(open(json_file2, 'r'))
    if not os.path.exists(save_path):#如果没有该文件夹存在 创建
        os.makedirs(save_path)

    for j in range(len(imgs)):
        if not os.path.exists(os.path.join(save_path, imgs[j]['file_name'])):
           shutil.copy(os.path.join(origin_path, imgs[j]['file_name']), os.path.join(save_path,  imgs[j]['file_name']))
           print(str(j) +':'+ imgs[j]['file_name'])
    
        # img_id=annos[j]['image_id']
        # f_name=images2[img_id-1]['file_name']
        # if not os.path.exists(os.path.join(save_path, str(img_id)+'jpg')):
        #    shutil.copy(os.path.join(origin_path, f_name), os.path.join(save_path, str(img_id)+'.jpg'))
        #    print(j)
    
    # annos = data1["annotations"]
    # images2 = data2["images"]
    # for j in range(len(annos)):#循环并加上进度条
    #     img_id=annos[j]['image_id']
    #     f_name=images2[img_id-1]['file_name']
    #     if not os.path.exists(os.path.join(save_path, str(img_id)+'jpg')):
    #        shutil.copy(os.path.join(origin_path, f_name), os.path.join(save_path, str(img_id)+'.jpg'))
    #        print(j)