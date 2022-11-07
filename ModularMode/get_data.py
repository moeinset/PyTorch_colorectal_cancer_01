import requests
import zipfile
from pathlib import Path

# Setup path to data folder
data_path = Path("data/")
image_path = data_path / "tumor_stroma_lympho"

# If the image folder doesn't exist, download it and prepare it... 
if image_path.is_dir():
    print(f"{image_path} directory exists.")
else:
    print(f"Did not find {image_path} directory, creating one...")
    image_path.mkdir(parents=True, exist_ok=True)
    
    # Download data
    with open(data_path / "tumor_stroma_lympho.zip", "wb") as f:
        request = requests.get("https://cdn-130.anonfiles.com/8ep9p1F8y5/04b33f1f-1667216246/tumor_stroma_lympho.zip")
        print("Downloading ...")
        f.write(request.content)

    # Unzip data
    with zipfile.ZipFile(data_path / "tumor_stroma_lympho.zip", "r") as zip_ref:
        print("Unzipping data...") 
        zip_ref.extractall(image_path)
