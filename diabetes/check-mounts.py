import sys
import os

# check-mounts.py root_path mount_path read_file write_file
# Takes four optional, but positional arguments.
# root_path: Override for root path to check
# mount_path: Mount path to check (will be concatenated with root path)
# read_file: File to attempt to read from the full mount path
# write_file: File to attempt to write to the full mount path

# Defults
DEFAULT_ROOT_PATH="/domino/nfs"
DEFAULT_MOUNT_PATH = None
DEFAULT_READ_FILE = None
DEFAULT_WRITE_FILE = None
DEFAULT_WRITE_FILE_CONTENTS = "Hello World"

# Settings for log file written to running file system
DIR_LOG = "/mnt"
LOG_FILE = "check-mounts.log"

class Logger:
    def __init__(self, dir_log, log_file):
        self.dir_log = dir_log
        self.log_file = log_file
        self.f = open(os.path.join(self.dir_log, self.log_file), "w+")

    def log(self, obj_to_log):
        str_to_log = str(obj_to_log)
        print(str_to_log)
        self.f.write(str_to_log+"\n")

    def new_break(self):
        print("\n")
        self.f.write("\n")

    def close_file(self):
        self.f.close()

class Config:
    def __init__(self, list_args, logger): 
        self.dict_config = {}
        self.dict_config["root_path"] = DEFAULT_ROOT_PATH
        self.dict_config["mount_path"] = DEFAULT_MOUNT_PATH
        self.dict_config["read_file"] = DEFAULT_READ_FILE
        self.dict_config["write_file"] = DEFAULT_WRITE_FILE
        self.logger = logger

        max_index = len(list_args)-1
        for arg_index in range(max_index, 0, -1):
            cur_arg = list_args[arg_index]

            if (arg_index == 1):
                self.dict_config["root_path"] = cur_arg
            elif (arg_index == 2):
                self.dict_config["mount_path"] = cur_arg
            elif (arg_index == 3):
                self.dict_config["read_file"] = cur_arg
            elif (arg_index == 4):
                self.dict_config["write_file"] = cur_arg
            else:
                pass
    
    def log_args(self):
        self.logger.log("Root Path: " + str(self.get("root_path")))
        self.logger.log("Mount Path: " + str(self.get("mount_path")))
        self.logger.log("Read File: " + str(self.get("read_file")))
        self.logger.log("Write File: " + str(self.get("write_file")))

    def get(self, str_key):
        return(self.dict_config[str_key])

    def get_full_path(self):
        return(os.path.join(self.get("root_path"), self.get("mount_path")))

    def can_check_key(self, str_key):
        if (self.get(str_key) is None):
            return(False)
        else:
            return(True)

    def read_file(self):
        full_path_to_file = os.path.join(self.get_full_path(), self.get("read_file"))

        try:
            with open(full_path_to_file, "r") as f:
                self.logger.log(f.readlines())            
                f.close()
        except:
            self.logger.log("Cannot read file: " + str(full_path_to_file))                

    def write_file(self):
        full_path_to_file = os.path.join(self.get_full_path(), self.get("write_file"))
        try:
            with open(full_path_to_file, "w+") as f:
                f.write(DEFAULT_WRITE_FILE_CONTENTS)
                f.close()
        except:
            self.logger.log("Cannot write file: " + str(full_path_to_file))                

logger = Logger(DIR_LOG, LOG_FILE)

config = Config(sys.argv, logger)
config.log_args()

# List items in the root path
logger.new_break()
logger.log("List items in root path: " + str(config.get("root_path")))
logger.log(os.listdir(config.get("root_path")))

if (config.can_check_key("mount_path")):
    logger.new_break()
    full_path = config.get_full_path()
    logger.log("List items in mount path: " + str(full_path))
    logger.log(os.listdir(full_path))

if (config.can_check_key("read_file")):
    logger.new_break()
    logger.log("Reading file (at mount path): " + str(config.get("read_file")))
    config.read_file()

if (config.can_check_key("write_file")):
    logger.new_break()
    logger.log("Writing to new file (at mount path): " + str(config.get("write_file")))
    config.write_file()