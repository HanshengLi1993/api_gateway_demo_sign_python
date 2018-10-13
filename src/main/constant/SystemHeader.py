class SystemHeader:
    """系统HTTP头常量"""

    def __init__(self):
        # 签名Header
        self.__x_ca_signature = "X-Ca-Signature"
        # 所有参与签名的Header
        self.__x_ca_signature_headers = "X-Ca-Signature-Headers"
        # 请求时间戳
        self.__x_ca_timestamp = "X-Ca-Timestamp"
        # 请求放重放Nonce,15分钟内保持唯一,建议使用UUID
        self.__x_ca_nonce = "X-Ca-Nonce"
        # APP KEY
        self.__x_ca_key = "X-Ca-Key"

    @property
    def X_CA_SIGNATURE(self):
        return self.__x_ca_signature

    @property
    def X_CA_SIGNATURE_HEADERS(self):
        return self.__x_ca_signature_headers

    @property
    def X_CA_TIMESTAMP(self):
        return self.__x_ca_timestamp

    @property
    def X_CA_NONCE(self):
        return self.__x_ca_nonce

    @property
    def X_CA_KEY(self):
        return self.__x_ca_key
