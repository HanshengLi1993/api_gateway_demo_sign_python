class HttpMethod:
    """HTTP方法常量"""

    def __init__(self):
        # GET
        self.__get = "GET"
        # POST
        self.__post = "POST"
        # PUT
        self.__put = "PUT"
        # DELETE
        self.__delete = "DElETE"


    @property
    def GET(self):
        return self.__get

    @property
    def POST(self):
        return self.__post

    @property
    def PUT(self):
        return self.__put

    @property
    def DELETE(self):
        return self.__delete
