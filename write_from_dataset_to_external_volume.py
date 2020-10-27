import shutil
import demo

shutil.copyfile("/mnt/datasets/my_dataset/latest/iris.csv", "/domino/nfs/{}/iris.csv".format(demo.edv1)
