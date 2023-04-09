import os

# parameters for API Call
TOKEN = None
USERNAME = None
PYTORCH_API = "https://api.github.com/repos/pytorch/pytorch/issues"
TENSOR_API = "https://api.github.com/repos/tensorflow/tensorflow/issues"
START_DATE = "2020-01-01"
DATA_PER_PAGE = 100
STATE = "closed"
FILTER_TYPE = "all"

# navigation parameters
os.makedirs("dataset",exist_ok=True)
os.makedirs("figures",exist_ok=True)

DATA_DIR = os.path.join(os.path.curdir,"dataset")
FIG_DIR = os.path.join(os.path.curdir,"figure")

token = "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"
