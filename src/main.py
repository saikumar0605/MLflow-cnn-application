import mlflow
import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
import random
#this is a default template. to use and create complete end to end ml flow project.

STAGE = "Main" ## <<< change stage name 
logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

#1:40:00 mlflow 2 video...

#now in mail.py we we use mlflow to run it and work.
def main():
    with mlflow.start_run() as run:
        
        mlflow.run(".", "get_data", use_conda=False)
        mlflow.run(".", "base_model", use_conda=False)
        # mlflow.run(".", "training", use_conda=False)



if __name__ == '__main__':

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main()
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e
