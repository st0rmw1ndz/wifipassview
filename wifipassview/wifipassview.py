__all__ = ["get_profiles_list", "get_password"]

import subprocess
from typing import List


def get_profiles_list() -> List[str]:
    """Gets the list of Wi-Fi profiles."""

    try:
        output = (
            subprocess.check_output(["netsh", "wlan", "show", "profiles"])
            .decode("utf-8")
            .split("\n")
        )
    except subprocess.CalledProcessError:
        return []

    try:
        return [
            i.split(":")[1][1:-1] for i in output if "All User Profile" in i
        ]
    except IndexError:
        return []


def get_password(profile: str) -> str:
    """Gets the password of a given Wi-Fi profile."""

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
