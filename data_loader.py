import pandas as pd
from pathlib import Path

def load_inventory_data(file) -> pd.DataFrame:
    """
    Load inventory data from:
    - Streamlit UploadedFile
    - Local file path (str or Path)
    """

    # Case 1: Streamlit UploadedFile
    if hasattr(file, "name"):
        filename = file.name
        file_obj = file

    # Case 2: Local file path (string or Path)
    else:
        filename = str(file)
        file_obj = file

    ext = Path(filename).suffix.lower()

    if ext == ".csv":
        return pd.read_csv(file_obj)
    elif ext in [".xls", ".xlsx"]:
        return pd.read_excel(file_obj)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")
