# import global packages
import requests
import json
import tqdm
import sys
import pickle
import math

# import local packages
from config import *

TOKEN = "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"
USERNAME = "Bot-Ro-Bot"

def api_call(api, page_no=1):
    '''
    Returns the json object of all the closed issues extracted from the github repo.

    Parameters:
        api (string): A string variable 
        page_no (int): An integer with default value 1.

    Returns:
        Closed issues (json): Ascending order of all the closed issues in the github repository   
    '''
    parameters = {"filter":FILTER_TYPE,"state":STATE,"sort":"created","direction":"asc","per_page":100,"page":page_no}
    
    try:
        req = requests.get(api, auth=(USERNAME, TOKEN), params=parameters)
    except Exception as error:
        print("Exited program execution because: ", error)
        sys.exit()
    
    return req.json()


def turn_page(api, total_pages=100):
    '''

    '''
    data = []
    for i in tqdm(range(1, total_pages+1)):
        data.extend(api_call(api, i))
    return data

def find_endpage(api):
    '''

    '''
    req = requests.get(api, auth=(USERNAME, TOKEN))
    return req.json()[0]["number"]


def save_data(data,filename):
    '''

    '''
    with open(filename+".txt", "w") as file:
        file.write(data)

    # try:
    #     # pickle.dump(data, open(filename+".pkl", "wb"))
    #     with open(filename+".json", "w") as file:
    #         file.write(json.dumps(data, indent=4))
    
    # except Exception as error:
    #     print("Saving Data Failed due to:",error) 
    #     print("Skipping data saving process...")   


if __name__=="__main__":
    
    # get github username
    USERNAME = input("GitHub Username: ")

    # get github token
    TOKEN = input("GitHub Access Token: ")
  
    # find end of loop for pagination
    tf_endpage = find_endpage(TENSOR_API)
    pt_endpage = find_endpage(PYTORCH_API)
    
    tf_data_len = math.floor(tf_endpage / 100) + 1
    pt_data_len = math.floor(pt_endpage / 100) + 1

    tf_data = turn_page(TENSOR_API,tf_data_len)
    pt_data = turn_page(PYTORCH_API,pt_data_len)


    SAVE_FLAG = input("Do you want to save data? Press Y to save and any other key to continue.  :")
  
    # if(SAVE_FLAG.lower() is "y"):
        # save_data()

    
    pass
