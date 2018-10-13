class HttpHeader:
    """HTTP头常量"""

    def __init__(self):
        # 请求Header Accept
        self.__http_header_accept = "Accept"
        # 请求Body内容MD5 Header
        self.__http_header_content_md5 = "Content-MD5"
        # 请求Header Content-Type
        self.__http_header_content_type = "Content-Type"
        # 请求Header UserAgent
        self.__http_header_user_agent = "User-Agent"
        # 请求Header Date
        self.__http_header_date = "Date"

    @property
    def HTTP_HEADER_ACCEPT(self):
        return self.__http_header_accept

    @property
    def HTTP_HEADER_CONTENT_MD5(self):
        return self.__http_header_content_md5

    @property
    def HTTP_HEADER_CONTENT_TYPE(self):
        return self.__http_header_content_type

    @property
    def HTTP_HEADER_USER_AGENT(self):
        return self.__http_header_user_agent

    @property
    def HTTP_HEADER_DATE(self):
        return self.__http_header_date
