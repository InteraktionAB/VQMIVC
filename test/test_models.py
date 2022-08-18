import os

from app.download import download_assets


def test_models_get_downloaded():
    download_assets()
    assert os.path.exists("VQMIVC-pretrained models.zip")
