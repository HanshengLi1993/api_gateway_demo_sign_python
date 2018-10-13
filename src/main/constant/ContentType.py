class ContentType:
    """常用HTTP Content-Type常量"""

    def __init__(self):
        self.__content_type_form = "application/x-www-form-urlencoded; charset=UTF-8"
        self.__content_type_stream = "application/octet-stream; charset=UTF-8"
        self.__content_type_json = "application/json; charset=UTF-8"
        self.__content_type_xml = "application/xml; charset=UTF-8"
        self.__content_type_text = "application/text; charset=UTF-8"

    @property
    def CONTENT_TYPE_FORM(self):
        return self.__content_type_form

    @property
    def CONTENT_TYPE_STREAM(self):
        return self.__content_type_stream

    @property
    def CONTENT_TYPE_JSON(self):
        return self.__content_type_json

    @property
    def CONTENT_TYPE_XML(self):
        return self.__content_type_xml

    @property
    def CONTENT_TYPE_TEXT(self):
        return self.__content_type_text
