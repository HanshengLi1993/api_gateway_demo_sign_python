class Request:
    """
    Request
    """

    def __init__(self, method=None, host=None, path=None, appKey=None, appSecret=None, timeout=None):
        # （必选）请求方法
        self.__method = method
        # （必选）Host
        self.__host = host
        # （必选）Path
        self.__path = path
        # （必选)APP KEY
        self.__appKey = appKey
        # （必选）APP密钥
        self.__appSecret = appSecret
        # （必选）超时时间,单位毫秒,设置零默认使用src.main.constant.Constants.DEFAULT_TIMEOUT
        self.__timeout = timeout
        # （可选） HTTP头
        self.__headers = {}
        # （可选） Querys
        self.__querys = {}
        # （可选）表单参数
        self.__bodys = {}
        # （可选）字节数组类型Body体
        self.__bytesBody = b''
        # （可选）自定义参与签名Header前缀
        self.__signHeaderPrefixList = []

    def getMethod(self):
        return self.__method

    def setMethod(self, method):
        self.__method = method

    def getHost(self):
        return self.__host

    def setPath(self, path):
        self.__path = path

    def getPath(self):
        return self.__path

    def setHost(self, host):
        self.__host = host

    def getAppKey(self):
        return self.__appKey

    def setAppKey(self, appKey):
        self.__appKey = appKey

    def getAppSecret(self):
        return self.__appSecret

    def setAppSecret(self, appSecret):
        self.__appSecret = appSecret

    def getTimeout(self):
        return self.__timeout

    def setTimeout(self, timeout):
        self.__timeout = timeout

    def getHeaders(self):
        return self.__headers

    def setHeaders(self, headers):
        self.__headers = headers

    def getQuerys(self):
        return self.__querys

    def setQuerys(self, querys):
        self.__querys = querys

    def getBodys(self):
        return self.__bodys

    def setBodys(self, bodys):
        self.__bodys = bodys

    def getStringBody(self):
        return self.__stringBody

    def setStringBody(self, stringBody):
        self.__stringBody = stringBody

    def getBytesBody(self):
        return self.__bytesBody

    def setBytesBody(self, bytesBody):
        self.__bytesBody = bytesBody

    def getSignHeaderPrefixList(self):
        return self.__signHeaderPrefixList

    def setSignHeaderPrefixList(self, signHeaderPrefixList):
        self.__signHeaderPrefixList = signHeaderPrefixList
