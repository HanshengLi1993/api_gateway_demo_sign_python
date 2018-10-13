class Constants:
    """通用常量"""

    def __init__(self):
        # 签名算法HmacSha256
        self.__hmac_sha256 = "HmacSHA256"
        # 编码UTF - 8
        self.__encoding = "UTF-8"
        # UserAgent
        self.__uer_agent = "demo/aliyun/python"
        # 换行符
        self.__lf = "\n"
        # 串联符
        self.__spe1 = ","
        # 示意符
        self.__spe2 = ":"
        # 连接符
        self.__spe3 = "&"
        # 赋值符
        self.__spe4 = "="
        # 问号符
        self.__spe5 = "?"
        # 默认请求超时时间, 单位毫秒
        self.__default_timeout = 1000
        # 参与签名的系统Header前缀, 只有指定前缀的Header才会参与到签名中
        self.__ca_header_to_sign_prefix_system = "X-Ca-"

    @property
    def HMAC_SHA256(self):
        return self.__hmac_sha256

    @property
    def ENCODING(self):
        return self.__encoding

    @property
    def USER_AGENT(self):
        return self.__uer_agent

    @property
    def LF(self):
        return self.LF

    @property
    def SPE1(self):
        return self.__spe1

    @property
    def SPE2(self):
        return self.__spe2

    def SPE3(self):
        return self.__spe3

    @property
    def SPE4(self):
        return self.__spe4

    @property
    def SPE4(self):
        return self.__spe5

    @property
    def SPE5(self):
        return self.__spe5

    @property
    def DEFAULT_TIMEOUT(self):
        return self.__default_timeout

    @property
    def CA_HEADER_TO_SIGN_PREFIX_SYSTEM(self):
        return self.__ca_header_to_sign_prefix_system

