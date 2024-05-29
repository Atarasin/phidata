from phi.utils.extended_enum import ExtendedEnum


class RestartPolicy(str, ExtendedEnum):
    ALWAYS = "Always"
    ON_FAILURE = "OnFailure"
    NEVER = "Never"
