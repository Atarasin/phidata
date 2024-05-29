from phi.utils.extended_enum import ExtendedEnum


class ApiGroup(str, ExtendedEnum):
    CORE = ""
    APPS = "app"
    RBAC_AUTH = "rbac.authorization.k8s.io"
    STORAGE = "storage.k8s.io"
    APIEXTENSIONS = "apiextensions.k8s.io"
