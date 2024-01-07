# wifipassview

![Python version](https://img.shields.io/badge/python-3.11%2B-blue.svg) ![License](https://img.shields.io/badge/license-MIT-97ca00)

wifipassview is a tool to view the saved Wi-Fi profiles on the system. It's stupidly simple, and as of now, is only 2
functions.

- `get_profiles_list()`: Returns a list of all saved Wi-Fi profiles.
- `get_password()`: Returns the password for a profile, if found.

*For more information, see the docstrings for the functions.*

## Installation

```
pip install git+https://github.com/st0rmw1ndz/wifipassview
```

## Example

```py
import wifipassview as wpv

profiles = wpv.get_profiles_list()
for profile in profiles:
    print(f"{profile}: {wpv.get_password(profile)}")
```

## Planned Features

- Showing more information on a profile (key type, network adapter)