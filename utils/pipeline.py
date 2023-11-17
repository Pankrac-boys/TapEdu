import os
import sys
import shutil
from sklearn.model_selection import train_test_split

if len(sys.argv) < 3:
    print("Too few arguments")

root_dir = argv[1]

test_split_ratio = argv[2]

train_dir = '../data/train'
test_dir = '../data/test'

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

for class_folder in os.listdir(root_dir):
    class_path = os.path.join(root_dir, class_folder)

    if not os.path.isdir(class_path):
        continue

    images = [img for img in os.listdir(class_path) if img.endswith(".jpg")]  # assuming images are in jpg format

    train_images, test_images = train_test_split(images, test_size=test_split_ratio, random_state=42)

    train_class_dir = os.path.join(train_dir, class_folder)
    test_class_dir = os.path.join(test_dir, class_folder)
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(test_class_dir, exist_ok=True)

    for img in train_images:
        src_path = os.path.join(class_path, img)
        dest_path = os.path.join(train_class_dir, img)
        shutil.copy(src_path, dest_path)

    for img in test_images:
        src_path = os.path.join(class_path, img)
        dest_path = os.path.join(test_class_dir, img)
        shutil.copy(src_path, dest_path)

print("Split complete.")
