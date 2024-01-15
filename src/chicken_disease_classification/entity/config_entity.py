
from dataclasses import dataclass
from pathlib import Path



@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: Path
    unzip_dir: Path
    kaggle_api_key: Path
    dataset_name: str
    kaggle_username: str

    


