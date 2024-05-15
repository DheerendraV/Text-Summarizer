import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')
project_name = "Text_summarizer"
list_of_files = [".github/workflows/.gitkeep",
                 f"src/{project_name}/__init__.py",
                 f"src/{project_name}/components/__init__.py",
                 f"src/{project_name}/utils/__init__.py",
                  f"src/{project_name}/utils/common.py",
                  f"src/{project_name}/logging/__init__.py",
                  f"src/{project_name}/config/__init__.py",
                  f"src/{project_name}/config/configuration.py",
                  f"src/{project_name}/pipeline/__init__.py",
                  f"src/{project_name}/entity/__init__.py",
                  f"src/{project_name}/costant/__init__.py",
                  "config/config.yaml",
                  "params.yaml ",
                  "app.py",
                  "main.py",
                  "Dockerfile",
                  "requirements.txt",
                  "setup.py",
                  "research/trail.ipynb"
                  ]

for file in list_of_files:
    file = Path(file)
    filedr,filename = os.path.split(file)
    if filedr!="":
        os.makedirs(filedr,exist_ok=True)
        logging.info(f"creating the directory:{filedr} for the file {filename}")
    
    if(not os.path.exists(file)) or os.path.getsize(file)==0:
        with open(file,"w") as f:
            pass
            logging.info(f"crearting new file: {file}")

    else:
        logging.info(f"{filename} already exsists")        


