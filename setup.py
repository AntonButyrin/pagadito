import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Pagadito",
    version="0.1.0",
    description="python implementation of pagadito",
    author="Anton Butyrin",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["pagadito"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["pydantic", "requests", "requests"],
    python_requires=">=3.8",
    include_package_data=True,
)
