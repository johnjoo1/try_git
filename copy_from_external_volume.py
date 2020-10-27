import shutil
import demo

src = "/domino/nfs/{}/iris.csv".format(demo.edv1)
dst = "/mnt/artifacts/{}/iris.csv".format(demo.project_name)

shutil.copyfile(src, dst)

print("copied {} to {}".format(src, dst))
