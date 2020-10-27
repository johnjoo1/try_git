import shutil
import os
import demo



shutil.copyfile("/domino/nfs/{}/iris.csv".format(demo.edv1), "/mnt/artifacts/{}/iris.csv".format(demo.project_name))
