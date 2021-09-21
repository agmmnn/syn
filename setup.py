from setuptools import setup
import synonym_cli.__main__ as m

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as file:
    requires = [line.strip() for line in file.readlines()]

VERSION = m.__version__
DESCRIPTION = "Synonyms and antonyms of words from Thesaurus are now in your terminal, with rich output."

setup(
    name="synonym-cli",
    version=VERSION,
    url="https://github.com/agmmnn/synonym",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="agmmnn",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
    packages=["synonym_cli"],
    install_requires=requires,
    include_package_data=True,
    package_data={"synonym_cli": ["synonym_cli/*"]},
    python_requires=">=3.5",
    entry_points={"console_scripts": ["syn = synonym_cli.__main__:cli"]},
)
