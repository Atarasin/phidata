from phi.utils.extended_enum import ExtendedEnum


class Protocol(str, ExtendedEnum):
    UDP = "UDP"
    TCP = "TCP"
    SCTP = "SCTP"
