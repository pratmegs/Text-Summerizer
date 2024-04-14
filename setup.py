import setuptools 

with open("README.md", "r", encoding = 'utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summerizier"
AUTHOR_USER_NAME = "pratmegs"
SRC_REPO = "textsummerization"
AUTH_EMAIL = "pratmegs@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTH_EMAIL,
    description="End to End project on Text Summerization",
    long_description=long_description,
    long_description_content ="text/markdown",
    url = "https://github.com/pratmegs/Text-Summerization",
    project_urls = {
        "bugs Tracker" : f"https://github.com/pratmegs/bugs"
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src"),
)