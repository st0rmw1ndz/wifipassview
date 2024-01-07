__all__ = ["get_profiles_list", "get_password"]

import subprocess
from typing import List


def get_profiles_list() -> List[str]:
    """Gets the list of Wi-Fi profiles saved on the system.

    :return: Wi-Fi profiles list, if any.
    """
    try:
        output = (
            subprocess.check_output(["netsh", "wlan", "show", "profiles"])
            .decode("utf-8")
            .split("\n")
        )
    except subprocess.CalledProcessError:
        return []

    return [i.split(":")[1][1:-1] for i in output if "All User Profile" in i]


def get_password(profile: str) -> str:
    """Gets the password of a given Wi-Fi profile.

    :param profile: Wi-Fi profile name.
    :return: Password of the Wi-Fi profile, if found.
    """
    try:
        output = (
            subprocess.check_output(
                ["netsh", "wlan", "show", "profile", profile, "key=clear"]
            )
            .decode("utf-8")
            .split("\n")
        )
    except subprocess.CalledProcessError:
        return ""

    try:
        return [i.split(":")[1][1:-1] for i in output if "Key Content" in i][0]
    except IndexError:
        return ""
