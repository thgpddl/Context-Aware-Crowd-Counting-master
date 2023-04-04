import json
from os.path import join
import glob


if __name__ == '__main__':
    # path to folder that contains images
    train_img_folder = r'dataset\ShanghaiTech_Crowd_Counting_Dataset\part_B_final\train_data\images'
    train_output_json = 'train_data.json'

    test_img_folder = r'dataset\ShanghaiTech_Crowd_Counting_Dataset\part_B_final\test_data\images'
    test_output_json = 'test_data.json'

    img_list = []

    for img_path in glob.glob(join(train_img_folder,'*.jpg')):
        img_list.append(img_path)

    with open(train_output_json,'w') as f:
        json.dump(img_list,f)

    for img_path in glob.glob(join(test_img_folder,'*.jpg')):
        img_list.append(img_path)

    with open(test_output_json,'w') as f:
        json.dump(img_list,f)
