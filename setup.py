from setuptools import find_packages, setup

setup(
    name="spotify_data",
    packages=find_packages(exclude=["spotify_data_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
