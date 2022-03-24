####### Split annotation files for few shot larning
# Usage:
# python prepare_splits.py ann_path 
# arguments:
#   [-o output location (str)]
#   [-s random seeds range (list)]
#   [-t maximum number of tryouts for sampling instnace of each class (int)]
#   [-k numbers of shots (list)]
#######
import argparse

import json
from pycocotools.coco import COCO
import os
from os.path import join
import random

def get_save_path_seeds(path, cls, shots, seed):
    prefix = "full_box_{}shot_{}".format(shots, cls)
    save_dir = join(path, "seed" + str(seed))
    os.makedirs(save_dir, exist_ok=True)
    save_path = join(save_dir, prefix + ".json")
    return save_path

class Dict:
    def __init__(self,**args):
        self.__dict__=args
        
def generate_seeds(args):
    data=COCO(args.ann_path)

    args.ID2CLASS={c["id"]:c["name"] for c in data.dataset["categories"][1:]}
    args.CLASS2ID ={v: k for k, v in args.ID2CLASS.items()}
    print(args.ID2CLASS)
    new_all_cats = data.dataset["categories"].copy()
    id2img = data.imgs.copy()
    anno = {cid: data.loadAnns(
        data.getAnnIds(catIds=cid,iscrowd=0)
        ) for cid in args.ID2CLASS.keys()}


    for i in range(args.seeds[0], args.seeds[1]):
        random.seed(i)
        for c in args.ID2CLASS.keys():
            img_ids = {}
            for a in anno[c]:
                if a["image_id"] in img_ids:
                    img_ids[a["image_id"]].append(a)
                else:
                    img_ids[a["image_id"]] = [a]

            sample_shots = []
            sample_imgs = []
            for K in args.shots:
                for _ in range(args.max_tries):
                    imgs = random.sample(list(img_ids.keys()), K)
                    for img in imgs:
                        skip = False
                        for s in sample_shots:
                            if img == s["image_id"]:
                                skip = True
                                break
                        if skip:
                            continue
                        if len(img_ids[img]) + len(sample_shots) > K:
                            continue
                            
                        sample_shots.extend(img_ids[img])
                        sample_imgs.append(id2img[img])
                        if len(sample_shots) == K:
                            break
                    if len(sample_shots) == K:
                        break
                new_data = {
                    "info": data.dataset["info"],
                    "licenses": data.dataset["licenses"],
                    "images": sample_imgs,
                    "annotations": sample_shots,
                }
                
                save_path = get_save_path_seeds(
                    args.output_root, args.ID2CLASS[c], K, i
                )
                print(save_path)
                print(f"images x{len(sample_imgs)},annotations x{len(sample_shots)}")
                new_data["categories"] = new_all_cats
                with open(save_path, "w") as f:
                    json.dump(new_data, f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('ann_path', help='annotation file path',default="ocean_coco/annotations/all_annotations.coco.json")
    parser.add_argument("-o", "--output_root", help='output file root',default="ocean_coco/splits")
    parser.add_argument("-s", "--seeds", help='random seed',default=[1,5])
    parser.add_argument("-t","--max_tries",help='maximum number of tryouts',default=200)
    parser.add_argument("-k","--shots",help='number of shots(list)',default=[1,5,10,30])
    args = parser.parse_args()
    
    args=Dict(**args.__dict__)
    print(args.__dict__)
    generate_seeds(args)
