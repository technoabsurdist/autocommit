from setuptools import setup, find_packages

setup(
    name="autocommit",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "ollama",
    ],
    entry_points={
        "console_scripts": [
            "autocommit=autocommit.main:main",
        ],
    },
)