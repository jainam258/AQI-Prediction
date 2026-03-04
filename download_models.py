import gdown
import os

# Create artifacts folder if it doesn't exist
os.makedirs("artifacts", exist_ok=True)

files = {
    "artifacts/aqi_model.joblib":          "https://drive.google.com/file/d/1yyufwqdMzipgNN9cN3gRA_EOSqYT-zwx/view?usp=sharing",
    "artifacts/city_aqi_model.joblib":     "https://drive.google.com/file/d/1KROU3B_vKwc1NCnohWeWWgEpSdb6SeGp/view?usp=sharing",
    "artifacts/city_label_encoder.joblib": "https://drive.google.com/file/d/1V-dpmuxZlZkLBRmiIHIBktW-Rq6T48Co/view?usp=sharing",
    "artifacts/features.joblib":           "https://drive.google.com/file/d/11KXASi35lBo_fXXgVAi-P2A-t7_587pN/view?usp=sharing",
    "artifacts/imputer.joblib":            "https://drive.google.com/file/d/1iU95VtGgPA4KLxrwnMF2vdKrCeGhvaq_/view?usp=sharing",
    "artifacts/scaler.joblib":             "https://drive.google.com/file/d/1v_9FfD0jlZQszWbKylm15G-8QmWVojqZ/view?usp=sharing",
}

for path, file_id in files.items():
    if not os.path.exists(path):
        print(f"Downloading {path}...")
        gdown.download(f"https://drive.google.com/uc?id={file_id}", path, quiet=False)
        print(f"✅ Done: {path}")