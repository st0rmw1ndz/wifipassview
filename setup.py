from setuptools import find_packages, setup

setup(
    name="wifipassview",
    version="1.0.1",
    py_modules=["wifipassview"],
    install_requires=["Click"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "wifipassview = wifipassview.__main__:cli",
        ],
    },
)
