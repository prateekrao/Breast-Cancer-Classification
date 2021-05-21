

def build_dataset():

# Importing required libraries





    import os
    import fnmatch
    from glob import glob
    import shutil
    import zipfile
    import random





# Using zipfile library to extract the data from the zipped dataset




    with zipfile.ZipFile("../Breast-Cancer-Detection/archive.zip", 'r') as zip_ref:
        zip_ref.extractall("../Breast-Cancer-Detection/archive")




# Store all the image filenames in a list



    patch_list = glob("../Breast-Cancer-Detection/archive/IDC_regular_ps50_idx5/**/*.png", recursive = True)




# Create two lists and store all the negative and positive patches in different lists respectively




    zero = fnmatch.filter(patch_list, "*class0.png")





    one = fnmatch.filter(patch_list, "*class1.png")





# Create directories for train, test and validation data





    os.mkdir("../Breast-Cancer-Detection/dataset/")





    os.mkdir("../Breast-Cancer-Detection/dataset/train")
    os.mkdir("../Breast-Cancer-Detection/dataset/test")
    os.mkdir("../Breast-Cancer-Detection/dataset/valid")




    os.mkdir("../Breast-Cancer-Detection/dataset/train/zero")
    os.mkdir("../Breast-Cancer-Detection/dataset/train/one")
    os.mkdir("../Breast-Cancer-Detection/dataset/test/zero")
    os.mkdir("../Breast-Cancer-Detection/dataset/test/one")
    os.mkdir("../Breast-Cancer-Detection/dataset/valid/zero")
    os.mkdir("../Breast-Cancer-Detection/dataset/valid/one")




# Split the data into 70% Train, 15% Validation and 15% Test




    split_1_zero = int(0.7*(len(zero)))
    split_2_zero = int(0.85*(len(zero)))




    split_1_one = int(0.7*(len(one)))
    split_2_one = int(0.85*(len(one)))




# Shuffle the data




    random.shuffle(zero)
    random.shuffle(one)




# Create lists with filenames for the split data




    train_zero = zero[:split_1_zero]
    test_zero = zero[split_1_zero:split_2_zero]
    valid_zero = zero[split_2_zero:]




    train_one = one[:split_1_one]
    test_one = one[split_1_one:split_2_one]
    valid_one = one[split_2_one:]




# Move the files to the respective directories




    for file in train_zero:
        shutil.move(file, "../Breast-Cancer-Detection/dataset/train/zero")
    for file in train_one:
        shutil.move(file, "../Breast-Cancer-Detection/dataset/train/one")




    print("Finished creating training directory")




    for file in test_zero:
        shutil.move(file, "../Breast-Cancer-Detection/dataset/test/zero")
    for file in test_one:
        shutil.move(file, "../Breast-Cancer-Detection/dataset/test/one")





    print("Finished creating testing directory")





    for file in valid_zero:
        shutil.move(file, "../Breast-Cancer-Detection/dataset/valid/zero")
    for file in valid_one:
        shutil.move(file, "../Breast-Cancer-Detection/dataset/valid/one")





    print("Finished creating validation directory")





    print("Finished Building Dataset")

