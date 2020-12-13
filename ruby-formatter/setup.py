import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ruby-analyzer",
    version="0.0.1",
    author="Alina",
    author_email="alin.grin2000@gmail.com",
    description="Console interactive utility for static analysis and modification of program codes for Ruby language.",
    url="https://github.com/Alina-Hryn/meta2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

