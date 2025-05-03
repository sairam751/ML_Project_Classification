# 1 Project Details

To set up a Conda environment in the current directory:

## 1.1..Setting up Conda Environment Locally

```bash
conda create --prefix ./venv python=3.10 #To create environment
conda activate ./venv # To actiavte Environment
pip install -r requirements.txt # To install requiremnt file
conda deactivate # To deactivate environment
```

## 2. Project Structure

- structure

## 3. Configuration File

### 3.1  Replace the Project Name and Details

- In config.yaml file replace name of the file with your project name
- Replace project name in data ingestion configuration

## 4. Data Ingestion Steps

### 4.1 DVC

- DVC Setup for Data Ingestion

Initialize DVC:

```bash
dvc init
dvc add {Folder_Path}
git add {Folder_Path} .gitignore
git commit -m "Track ingested data with DVC"
dvc remote add -d myremote <remote-url>
dvc push

```

To Push Locally:

```bash
mkdir ../dvc_storage
dvc remote add -d localstore ../dvc_storage
dvc push

```

- test
