import hmac
import base64
import hashlib
from ..constant.Constants import *
from ..constant.HttpHeader import *
from ..constant.SystemHeader import *


class SignUtil:
    """签名工具"""

    def __init__(self):
        self.__Constants = Constants()
        self.__HttpHeader = HttpHeader()
        self.__SystemHeader = SystemHeader()

    def sign(self, secret, method, path, headers, querys, bodys, signHeaderPrefixList):
        """
        计算签名
        :param secret:APP密钥
        :param method:HttpMethod
        :param path:
        :param headers:
        :param querys:
        :param bodys:
        :param signHeaderPrefixList:自定义参与签名Header前缀
        :return:签名后的字符串
        """
        try:
            keyBytes = secret.encode(self.__Constants.ENCODING)
            bytesToSign = self.__buildStringToSign(method, path, headers, querys, bodys, signHeaderPrefixList).encode(self.__Constants.ENCODING)
            hmacSha256 = str(base64.b64encode(
                hmac.new(keyBytes, bytesToSign, digestmod=hashlib.sha256).digest()).decode(Constants.ENCODING), encoding=self.__Constants.ENCODING)

            return hmacSha256
        except Exception:
            pass

    def __buildStringToSign(self, method, path, headers, querys, bodys, signHeaderPrefixList):
        """
        构建待签名字符串
        :param method:
        :param path:
        :param headers:
        :param querys:
        :param bodys:
        :param signHeaderPrefixList:
        :return:
        """
        sb = ""
        sb += method.upper() + self.__Constants.LF
        if not headers:
            if self.__HttpHeader.HTTP_HEADER_ACCEPT in headers.keys():
                sb += headers[self.__HttpHeader.HTTP_HEADER_ACCEPT]
            sb += self.__Constants.LF
            if self.__HttpHeader.HTTP_HEADER_CONTENT_MD5 in headers.keys():
                sb += headers[self.__HttpHeader.HTTP_HEADER_CONTENT_MD5]
            sb += self.__Constants.LF
            if self.__HttpHeader.HTTP_HEADER_CONTENT_TYPE in headers.keys():
                sb += headers[self.__HttpHeader.HTTP_HEADER_CONTENT_TYPE]
            sb += self.__Constants.LF
            if self.__HttpHeader.HTTP_HEADER_DATE in headers.keys():
                sb += headers[self.__HttpHeader.HTTP_HEADER_DATE]
        sb += self.__Constants.LF
        sb += self.__buildHeaders(headers, signHeaderPrefixList)
        sb += self.__buildResource(path, querys, bodys)
        return sb

    def __buildResource(self, path, querys, bodys):
        """
        构建待签名Path+Query+BODY
        :param path:
        :param querys:
        :param bodys:
        :return:待签名
        """
        sb = ""

        if not self.__isBlank(path):
            sb += path
        sortMap = {}
        if querys is not None:
            for query, value in querys.items():
                if not self.__isBlank(query):
                    sortMap[query] = value

        if bodys is not None:
            for body, value in bodys.items():
                if not self.__isBlank(body):
                    sortMap[body] = value

        sbParam = ""
        for item, value in sortMap.items():
            if not self.__isBlank(item):
                if len(sbParam) > 0:
                    sbParam += self.__Constants.SPE3
                sbParam += value
                if not self.__isBlank(value):
                    sbParam += self.__Constants.SPE4 + value
        if len(sbParam) > 0:
            sb += self.__Constants.SPE5 + sbParam

        return sb

    def __buildHeaders(self, headers, signHeaderPrefixList):
        """
        构建待签名Http头
        :param headers:请求中所有的Http头
        :param signHeaderPrefixList:自定义参与签名Header前缀
        :return:待签名Http头
        """
        sb = ""
        if signHeaderPrefixList is not None:
            signHeaderPrefixList.remove(self.__SystemHeader.X_CA_SIGNATURE)
            signHeaderPrefixList.remove(self.__HttpHeader.HTTP_HEADER_ACCEPT)
            signHeaderPrefixList.remove(self.__HttpHeader.HTTP_HEADER_CONTENT_MD5)
            signHeaderPrefixList.remove(self.__HttpHeader.HTTP_HEADER_CONTENT_TYPE)
            signHeaderPrefixList.remove(self.__HttpHeader.HTTP_HEADER_DATE)
            signHeaderPrefixList.sort()
            if not headers:
                sortMap = headers
                signHeadersStringBuilder = ""
                for header, value in sortMap.items():
                    if self.__isHeaderToSign(header, signHeaderPrefixList):
                        sb += header + self.__Constants.SPE2
                        if not self.__isBlank(value):
                            sb += value
                        sb += self.__Constants.LF
                        if 0 < len(signHeadersStringBuilder):
                            signHeadersStringBuilder += self.__Constants.SPE1
                        signHeadersStringBuilder += value
                headers[self.__SystemHeader.X_CA_SIGNATURE_HEADERS] = signHeadersStringBuilder
        return sb

    def __isHeaderToSign(self, headerName, signHeaderPrefixList):
        """
        Http头是否参与签名
        :param headerName:
        :param signHeaderPrefixList:
        :return:
        """
        if self.__isBlank(headerName):
            return False
        if headerName.startswith(self.__Constants.CA_HEADER_TO_SIGN_PREFIX_SYSTEM):
            return False
        if signHeaderPrefixList is not None:
            for signHeaderPrefix in signHeaderPrefixList:
                if headerName.lower() == signHeaderPrefix.lower():
                    return True
        return False

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
