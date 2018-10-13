class Response:
    def __init__(self):
        self.__statusCode = 0
        self.__contentType = ""
        self.__requestId = ""
        self.__errorMessage = ""
        self.__headers = {}
        self.__body = ""

    def getStatusCode(self):
        return self.__statusCode

    def setStatusCode(self, statusCode):
        self.__statusCode = statusCode

    def getContentType(self):
        return self.__contentType

    def setContentType(self, contentType):
        self.__contentType = contentType

    def getRequestId(self):
        return self.__requestId

    def setRequestId(self, requestId):
        self.__requestId = requestId

    def getErrorMessage(self):
        return self.__errorMessage

    def setErrorMessage(self, errorMessage):
        self.__errorMessage = errorMessage

    def getHeader(self, key=None):
        if key is None:
            return self.__headers
        else:
            if self.__headers is not None and key in self.__headers.keys():
                return self.__headers[key]
            else:
                return None

    def setHeader(self, headers=None, key="", value=""):
        if headers is None:
            if key is not None:
                self.__headers[key] = value
        else:
            self.__headers = headers

    def getBody(self):
        return self.__body

    def setBody(self, body):
        self.__body = body
