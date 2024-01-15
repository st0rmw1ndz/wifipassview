# wifipassview

![Python version](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-97ca00)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Utility to view a list of Wi-Fi profiles and their passwords

## Installation

```
pip install git+https://github.com/st0rmw1ndz/wifipassview
```

## Example

```python
import wifipassview as wpv

profiles = wpv.get_profiles_list()
for profile in profiles:
    print(f"{profile}: {wpv.get_password(profile)}")
```