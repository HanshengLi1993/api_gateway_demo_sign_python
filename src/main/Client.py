from .enums.Method import *
from .util.HttpUtil import *
from .Request import *


class Client:
    """
    Client
    """

    def execute(self, request):
        """
        发送请求
        :param request:request对象
        :return:Response
        """
        try:
            __method = request.getMethod()
            if __method == Method['GET'].value:
                return HttpUtil().httpGet(request.getHost(),
                                          request.getPath(),
                                          request.getTimeout(),
                                          request.getHeaders(),
                                          request.getQuerys(),
                                          None,
                                          request.getSignHeaderPrefixList(),
                                          request.getAppKey(),
                                          request.getAppSecret())
            elif __method == Method['POST'].value:
                return HttpUtil().httpPost(request.getHost(),
                                           request.getPath(),
                                           request.getTimeout(),
                                           request.getHeaders(),
                                           request.getQuerys(),
                                           request.getBodys(),
                                           request.getSignHeaderPrefixList(),
                                           request.getAppKey(),
                                           request.getAppSecret())
            elif __method == Method['PUT'].value:
                return HttpUtil().httpPut(request.getHost(),
                                          request.getPath(),
                                          request.getTimeout(),
                                          request.getHeaders(),
                                          request.getQuerys(),
                                          request.getBytesBody(),
                                          request.getSignHeaderPrefixList(),
                                          request.getAppKey(),
                                          request.getAppSecret())
            elif __method == Method['DELETE'].value:
                return HttpUtil().httpDelete(request.getHost(),
                                             request.getPath(),
                                             request.getTimeout(),
                                             request.getHeaders(),
                                             request.getQuerys(),
                                             None,
                                             request.getSignHeaderPrefixList(),
                                             request.getAppKey(),
                                             request.getAppSecret())
            else:
                raise Exception("unsupported method:%s", __method)
        except:
            pass
