import gdown


def download_assets(
    url: str = "https://drive.google.com/uc?id=1Flw6Z0K2QdRrTn5F-gVt6HdR9TRPiaKy",  # noqa
):
    gdown.download(url, quiet=True)
