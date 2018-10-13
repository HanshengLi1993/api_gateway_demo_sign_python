import json
from ..main.constant.HttpHeader import *
from ..main.Request import *
from ..main.enums.Method import *
from ..main.constant.HttpSchema import *
from ..main.constant.Constants import *
from ..main.Client import *


class Demo:
    """
    调用示例
    请替换APP_KEY,APP_SECRET,HOST,CUSTOM_HEADERS_TO_SIGN_PREFIX为真实配置
    """

    def __init__(self):
        # APP KEY
        self.__APP_KEY = "app_key"
        # APP密钥
        self.__APP_SECRET = "APP_SECRET"
        # API域名
        self.__HOST = "api.aaaa.com"
        # 自定义参与签名Header前缀（可选,默认只有"X-Ca-"开头的参与到Header签名）
        self.__CUSTOM_HEADERS_TO_SIGN_PREFIX = []

        self.__HttpHeader = HttpHeader()
        self.__HttpSchema = HttpSchema()
        self.__Constants = Constants()
        self.__ContentType = ContentType()

    def get(self):
        """
        HTTP GET
        :return:
        """
        try:
            # 请求path
            path = "/get"
            # （必填）根据期望的Response内容类型设置
            headers = {self.__HttpHeader.HTTP_HEADER_ACCEPT: "application/json",
                       "a-header1": "header1Value",
                       "b-header2": "header2Value"}
            self.__CUSTOM_HEADERS_TO_SIGN_PREFIX = []
            self.__CUSTOM_HEADERS_TO_SIGN_PREFIX.append("a-header1")
            self.__CUSTOM_HEADERS_TO_SIGN_PREFIX.append("a-header2")
            request = Request(Method['GET'].value, self.__HttpSchema.HTTP + self.__HOST, path, self.__APP_KEY, self.__APP_SECRET, self.__Constants.DEFAULT_TIMEOUT)
            request.setHeaders(headers)
            request.setSignHeaderPrefixList(self.__CUSTOM_HEADERS_TO_SIGN_PREFIX)

            # 请求的query
            querys = {"a-query1": "query1Value",
                      "b-query2": "query2Value",
                      }
            request.setQuerys(querys)

            # 调用服务端
            response = Client().execute(request)
            print(json.dumps(response))
        except:
            pass

    def post(self):
        """
        HTTP POST
        :return:
        """
        try:
            # 请求path
            path = "/post"
            # Body内容
            body = "demo string body content"

            # （必填）根据期望的Response内容类型设置
            headers = {self.__HttpHeader.HTTP_HEADER_ACCEPT: "application/json"}
            # （可选）Body MD5, 服务端会校验Body内容是否被篡改, 建议Body非Form表单时添加此Header
            headers[self.__HttpHeader.HTTP_HEADER_CONTENT_MD5] = MessageDigestUtil().base64AndMD5(body)
            # （POST/PUT请求必选）请求Body内容格式
            headers[self.__HttpHeader.HTTP_HEADER_CONTENT_TYPE] = self.__ContentType.CONTENT_TYPE_TEXT

            headers["a-header1"] = "header1Value"
            headers["b-header2"] = "header2Value"
            self.__CUSTOM_HEADERS_TO_SIGN_PREFIX = []
            self.__CUSTOM_HEADERS_TO_SIGN_PREFIX.append("a-header1")
            self.__CUSTOM_HEADERS_TO_SIGN_PREFIX.append("a-header2")
            request = Request(Method['POST'].value, self.__HttpSchema.HTTP + self.__HOST, path, self.__APP_KEY, self.__APP_SECRET, self.__Constants.DEFAULT_TIMEOUT)
            request.setHeaders(headers)
            request.setSignHeaderPrefixList(self.__CUSTOM_HEADERS_TO_SIGN_PREFIX)

            # 请求的query
            querys = {"a-query1": "query1Value",
                      "b-query2": "query2Value",
                      }
            request.setQuerys(querys)
            request.setStringBody(body)

            # 调用服务端
            response = Client().execute(request)
            print(json.dumps(response))
        except:
            pass

    def put(self):
        """
        HTTP PUT
        :return:
        """
        try:
            # 请求path
            path = "/put"
            # Body内容
            body = "demo string body content"

            # （必填）根据期望的Response内容类型设置
            headers = {self.__HttpHeader.HTTP_HEADER_ACCEPT: "application/json"}
            # （可选）Body MD5, 服务端会校验Body内容是否被篡改, 建议Body非Form表单时添加此Header
            headers[self.__HttpHeader.HTTP_HEADER_CONTENT_MD5] = MessageDigestUtil().base64AndMD5(body)
            # （POST/PUT请求必选）请求Body内容格式
            headers[self.__HttpHeader.HTTP_HEADER_CONTENT_TYPE] = self.__ContentType.CONTENT_TYPE_TEXT

            headers["a-header1"] = "header1Value"
            headers["b-header2"] = "header2Value"
            self.__CUSTOM_HEADERS_TO_SIGN_PREFIX = []
            self.__CUSTOM_HEADERS_TO_SIGN_PREFIX.append("a-header1")
            self.__CUSTOM_HEADERS_TO_SIGN_PREFIX.append("a-header2")
            request = Request(Method['PUT'].value, self.__HttpSchema.HTTP + self.__HOST, path, self.__APP_KEY, self.__APP_SECRET, self.__Constants.DEFAULT_TIMEOUT)
            request.setHeaders(headers)
            request.setSignHeaderPrefixList(self.__CUSTOM_HEADERS_TO_SIGN_PREFIX)

            # 请求的query
            querys = {"a-query1": "query1Value",
                      "b-query2": "query2Value",
                      }
            request.setQuerys(querys)
            request.setStringBody(body)

            # 调用服务端
            response = Client().execute(request)
            print(json.dumps(response))
        except:
            pass

    def delete(self):
        """
        HTTP DELETE
        :return:
        """
        try:
            # 请求path
            path = "/delete"

            # （必填）根据期望的Response内容类型设置
            headers = {self.__HttpHeader.HTTP_HEADER_ACCEPT: "application/json"}

            request = Request(Method['DELETE'].value, self.__HttpSchema.HTTP + self.__HOST, path, self.__APP_KEY, self.__APP_SECRET, self.__Constants.DEFAULT_TIMEOUT)
            request.setHeaders(headers)
            request.setSignHeaderPrefixList(self.__CUSTOM_HEADERS_TO_SIGN_PREFIX)

            # 调用服务端
            response = Client().execute(request)
            print(json.dumps(response))
        except:
            pass
