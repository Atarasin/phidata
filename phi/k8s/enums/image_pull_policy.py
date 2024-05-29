from phi.utils.extended_enum import ExtendedEnum


class ImagePullPolicy(str, ExtendedEnum):
    ALWAYS = "Always"
    IF_NOT_PRESENT = "IfNotPresent"
    NEVER = "Never"
