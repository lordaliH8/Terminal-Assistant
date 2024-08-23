import ast
import platform
import distro
from typing import List


# OS
def get_os():
    os_name = platform.system()
    if os_name == "Linux":
        distro_name, os_version = distro.name(), distro.version()
        return f"{os_name} ({distro_name} {os_version})"
    elif os_name == "Darwin":
        return "macOS"
    elif os_name == "Windows":
        return f"{os_name} ({platform.release()})"
    else:
        return "Unknown"


def validate_model_response(model_response: str, keys: List[str]):
    try:
        valid_response = ast.literal_eval(model_response)
        for key in keys:
            if key in valid_response.keys():
                continue
            else:
                return None
        return valid_response
    except Exception:
        return None
