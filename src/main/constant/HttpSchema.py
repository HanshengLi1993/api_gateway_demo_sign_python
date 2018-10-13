class HttpSchema:
    """HTTP Schema常量"""

    def __init__(self):
        # HTTP
        self.__http = "http://"
        # HTTPS
        self.__https = "https://"

    @property
    def HTTP(self):
        return self.__http

    @property
    def HTTPS(self):
        return self.__https
