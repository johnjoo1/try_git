import shutil
import demo

target = "/domino/nfs/{}/iris.csv".format(demo.edv1)

shutil.copyfile("/mnt/datasets/my_dataset/latest/iris.csv", target)

print("wrote to {}".format(target))
