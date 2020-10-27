import shutil
import demo

shutil.copyfile("/mnt/artifacts/{}/iris.csv".format(demo.project_name), "/domino/nfs/{}/iris.csv".format(demo.edv2))
