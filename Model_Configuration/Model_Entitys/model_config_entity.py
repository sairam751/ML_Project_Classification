from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    """
    Data Ingestion Configuration class.
    """
    root_dir_artifacts: Path
    root_dir_data: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path