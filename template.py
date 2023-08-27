import  os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name='mlproject'

list_of_file=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/Data_ingestion.py",
    f"src/{project_name}/components/Data_trasnformation.py",
    f"src/{project_name}/components/Model_trainer.py",
    f"src/{project_name}/components/Model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/execption.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirement.txt",
    'setup.py'
]  

for filepath in list_of_file:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")