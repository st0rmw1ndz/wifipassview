# wifipassview

Utility to view Wi-Fi profiles and their passwords.

## Example

```python
import wifipassview as wpv

profiles = wpv.get_profiles_list()
for profile in profiles:
    print(f"{profile}: {wpv.get_password(profile)}")
```

## Installation

```
pip install git+https://github.com/st0rmw1ndz/wifipassview.git
```