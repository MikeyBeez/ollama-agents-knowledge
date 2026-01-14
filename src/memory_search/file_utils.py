# src/memory_search/file_utils.py

import json
from pathlib import Path
from typing import Dict, Any, List

def read_json_file(file_path: Path) -> Dict[str, Any]:
    with open(file_path, 'r') as f:
        return json.load(f)

def write_json_file(file_path: Path, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def get_json_files_in_directory(directory: Path) -> List[Path]:
    return list(directory.glob('*.json'))

def increment_json_field(file_path: Path, field: str) -> None:
    data = read_json_file(file_path)
    data[field] = data.get(field, 0) + 1
    write_json_file(file_path, data)
