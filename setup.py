
import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


__version__ = '0.0.0'

REPO_NAME = "End-To-End-Chicken-Disease-Classification-Project-using-CNN"
AUTHOR_USER_NAME = "MaazSayyed05"
SRC_REPO = "chicken_disease_classification"
AUTHOR_EMAIL = "maazsayyed05@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "End-To-End-Chicken-Disease-Classification-Project-using-CNN",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/MaazSayyed05/End-To-End-Chicken-Disease-Classification-Project-using-CNN",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"": "src"},
    packages=setuptools.find_packages(where='src')
)



