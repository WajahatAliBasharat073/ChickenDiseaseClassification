# This line imports the setuptools module, which provides a set of tools to simplify the packaging of Python libraries.
import setuptools
# This line opens the "README.md" file in read mode using UTF-8 encoding.
with open("README.md", "r", encoding="utf-8") as f:
    #  This line reads the content of the "README.md" file and stores it in the long_description variable.
    long_description = f.read()

# This line starts the setup() function of the setuptools module, which is used to specify the package's metadata and its build options.
setuptools.setup(
    # This line sets the name of the package.
    name="ChickenDiseaseClassification",
    # This line sets the version of the package.
    version="0.0.0",
    # This line sets the author of the package.
    author="WajahatAliBasharat073",
    #This line sets the author's email address.
    author_email="wajahatalibasharat073@gmail.com",
    # This line sets a brief description of the package.
    description="A small python package for chicken disease classification",
    # This line sets the long description of the package, which is read from the "README.md" file.
    long_description=long_description,
    # This line sets the content type of the long description.
    long_description_content_type="text/markdown",
    # This line sets the URL of the package's home page.
    url="https://github.com/WajahatAliBasharat073/ChickenDiseaseClassification",
    # This line starts a dictionary that maps names to URLs for other related projects.
    project_urls={
        #  This line maps the name "Bug Tracker" to the URL of the package's bug tracker.
        "Bug Tracker": "https://github.com/WajahatAliBasharat073/ChickenDiseaseClassification/issues",
    },
    # This line sets the directory where the package's code is located. In this case, it is the "src" directory.
    package_dir={"": "src"},
    # This line finds all packages in the "src" directory and specifies them as the packages included in the package.
    packages=setuptools.find_packages(where="src"),
    # classifiers=[: This line starts a list of classifiers that specify the characteristics of the package.
    classifiers=[
        # This line specifies that the package requires Python 3.
        "Programming Language :: Python :: 3",
        # This line specifies that the package is compatible with all operating systems.
        "Operating System :: OS Independent",
    ],
    # python_requires=">=3.6",: This line specifies that the package requires Python 3.6 or later.
    python_requires=">=3.6",
)
# After running this script, a "dist" directory will be created in the package's root directory. This directory will contain the package's distribution files
