import shutil
import demo

src = "/mnt/datasets/my_dataset/latest/iris.csv".format(demo.project_name)
dst = "/domino/nfs/{}/iris.csv".format(demo.edv2)

shutil.copyfile(src, dst)
print("Hello Demo!")

print("copied {} to {}".format(src, dst))
