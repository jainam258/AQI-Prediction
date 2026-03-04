import gdown
import os

# Create artifacts folder if it doesn't exist
os.makedirs("artifacts", exist_ok=True)

files = {
    "artifacts/aqi_model.joblib":          "1yyufwqdMzipgNN9cN3gRA_EOSqYT-zwx",
    "artifacts/city_aqi_model.joblib":     "1KROU3B_vKwc1NCnohWeWWgEpSdb6SeGp",
    "artifacts/city_label_encoder.joblib": "1V-dpmuxZlZkLBRmiIHIBktW-Rq6T48Co",
    "artifacts/features.joblib":           "11KXASi35lBo_fXXgVAi-P2A-t7_587pN",
    "artifacts/imputer.joblib":            "1iU95VtGgPA4KLxrwnMF2vdKrCeGhvaq_",
    "artifacts/scaler.joblib":             "1v_9FfD0jlZQszWbKylm15G-8QmWVojqZ",
}

for path, file_id in files.items():
    if not os.path.exists(path):
        print(f"Downloading {path}...")
        gdown.download(f"https://drive.google.com/uc?id={file_id}", path, quiet=False)
        print(f"✅ Done: {path}")