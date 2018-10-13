import time
import uuid
import ssl
import socket
import urllib.parse
import urllib.request
from .SignUtil import *
from ..constant.HttpMethod import *
from ..constant.ContentType import *
from ..Response import *
from .MessageDigesUtil import *


class HttpUtil:
    """Http工具类"""

    def __init__(self):
        self.__HttpMethod = HttpMethod()
        self.__HttpHeader = HttpHeader()
        self.__ContentType = ContentType()
        self.__Constants = Constants()

    def httpGet(self, host, path, connectTimeout, headers, querys, body, signHeaderPrefixList, appKey, appSecret):
        """
        HTTP GET
        :param host:
        :param path:
        :param connectTimeout:
        :param headers:
        :param querys:
        :param signHeaderPrefixList:
        :param appKey:
        :param appSecret:
        :return:
        """
        try:
            headers = self.__initialBasicHeader(self.__HttpMethod.GET, path, headers, querys, None, signHeaderPrefixList, appKey, appSecret)
            socket.setdefaulttimeout(self.__getTimeout(connectTimeout))
            return self.__convert(host, path, self.__HttpMethod.GET, querys, body, headers)
        except Exception:
            pass

    def httpPost(self, host, path, connectTimeout, headers, querys, bodys, signHeaderPrefixList, appKey, appSecret):
        """
        HTTP POST
        :param host:
        :param path:
        :param connectTimeout:
        :param headers:
        :param querys:
        :param signHeaderPrefixList:
        :param appKey:
        :param appSecret:
        :return:
        """
        try:
            if headers is None:
                headers = {}

            headers[self.__HttpHeader.HTTP_HEADER_CONTENT_TYPE] = self.__ContentType.CONTENT_TYPE_FORM

            headers = self.__initialBasicHeader(self.__HttpMethod.POST, path, headers, querys, bodys, signHeaderPrefixList, appKey, appSecret)
            socket.setdefaulttimeout(self.__getTimeout(connectTimeout))
            return self.__convert(host, path, self.__HttpMethod.POST, querys, bodys, headers)
        except Exception:
            pass

    def httpPut(self, host, path, connectTimeout, headers, querys, bodys, signHeaderPrefixList, appKey, appSecret):
        """
        HTTP PUT
        :param host:
        :param path:
        :param connectTimeout:
        :param headers:
        :param querys:
        :param signHeaderPrefixList:
        :param appKey:
        :param appSecret:
        :return:
        """
        try:
            headers = self.__initialBasicHeader(self.__HttpMethod.PUT, path, headers, querys, None, signHeaderPrefixList, appKey, appSecret)
            socket.setdefaulttimeout(self.__getTimeout(connectTimeout))
            return self.__convert(host, path, self.__HttpMethod.PUT, querys, bodys, headers)
        except Exception:
            pass

    def httpDelete(self, host, path, connectTimeout, headers, querys, body, signHeaderPrefixList, appKey, appSecret):
        """
        HTTP DELETE
        :param host:
        :param path:
        :param connectTimeout:
        :param headers:
        :param querys:
        :param signHeaderPrefixList:
        :param appKey:
        :param appSecret:
        :return:
        """
        try:
            headers = self.__initialBasicHeader(self.__HttpMethod.DELETE, path, headers, querys, None, signHeaderPrefixList, appKey, appSecret)
            socket.setdefaulttimeout(self.__getTimeout(connectTimeout))
            return self.__convert(host, path, self.__HttpMethod.DELETE, querys, body, headers)
        except Exception:
            pass

    def __initialBasicHeader(self, method, path, headers, querys, bodys, signHeaderPrefixList, appKey, appSecret):
        """
        初始化基础Header
        :return:
        """
        try:
            if not isinstance(headers, dict):
                headers = {}

            headers["X_CA_TIMESTAMP"] = str(int(time.time() * 1000))
            headers["X_CA_NONCE"] = str(uuid.uuid1())
            headers["X_CA_KEY"] = appKey
            headers["X_CA_SIGNATURE"] = SignUtil().sign(appSecret, method, path, headers, querys, bodys, signHeaderPrefixList)

            return headers
        except Exception:
            pass

    def __getTimeout(self, timeout):
        """
        读取超时时间
        :param timeout:
        :return:
        """
        if timeout == 0:
            return Constants().DEFAULT_TIMEOUT
        return timeout

    def __convert(self, host, path, method, querys, body, headers):
        """
        :param path:
        :param querys:
        :return:
        """
        try:
            res = Response()
            if method == self.__HttpMethod.GET or method == self.__HttpMethod.DELETE:
                url = self.__initUrl(host, path, querys)
                request = urllib.request.Request(url=url, headers=headers, method=method)
            elif method == self.__HttpMethod.POST or method == self.__HttpMethod.PUT:
                url = self.__initUrl(host, path, querys)
                data = urllib.parse.urlencode(body, encoding=Constants.ENCODING)
                request = urllib.request.Request(url=url, data=data, headers=headers, method=method)
            else:
                # 异常处理
                raise Exception("unsupported method:%s", method)
            if host.startsWith("https://"):
                context = ssl._create_unverified_context()
                response = urllib.request.urlopen(url=request, context=context)
            else:
                response = urllib.request.urlopen(url=request)
            if response is not None:
                res.setStatusCode(response.status_code)
                for header, value in response.headers.items():
                    res.setHeader(header, MessageDigestUtil().iso88591ToUtf8(headers[header]))

                res.setContentType(res.getHeader("Content-Type"))
                res.setRequestId(res.getHeader("X-Ca-Request-Id"))
                res.setErrorMessage(res.getHeader("X-Ca-Error-Message"))
                res.setBody(MessageDigestUtil().toString(response.content))
            else:
                # 服务器无回应
                res.setStatusCode(500)
                res.setErrorMessage("No Response")
            return res
        except:
            pass

    def __initUrl(self, host, path, querys):
        sbUrl = host
        if not self.__isBlank(path):
            sbUrl += path
        if querys is not None:
            sbQuery = ""
            for query, value in querys.items():
                if len(sbQuery) > 0:
                    sbQuery += self.__Constants.SPE3
                if self.__isBlank(query) and not self.__isBlank(value):
                    sbQuery += value
                if not self.__isBlank(query):
                    sbQuery += query
                if not self.__isBlank(value):
                    sbQuery += self.__Constants.SPE4
                    sbQuery += value

            if len(sbQuery) > 0:
                sbUrl += self.__Constants.SPE5 + sbQuery

        return sbUrl

    def __isBlank(self, string):
        """
        是否为 null
        是否为 ""
        是否为空字符串(引号中间有空格)  如： "     "
        :param string:
        :return:
        """
        if string is None or len(string.strip()) == 0:
            return True
        else:
            return False
