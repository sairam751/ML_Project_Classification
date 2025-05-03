# 1.Setting up Conda Environment Locally

To set up a Conda environment in the current directory:

## 1.1 Create Environment
```bash
conda create --prefix ./venv python=3.10
conda activate ./venv
pip install -r requirements.txt
conda deactivate
```
