import hashlib
import base64
from ..constant.Constants import *


class MessageDigestUtil:
    """
    消息摘要工具
    """

    def __init__(self):
        self.__Constants = Constants()

    def base64AndMD5(self, message):
        """
        先进行MD5摘要再进行Base64编码获取摘要字符串
        :param str:
        :return:
        """
        try:
            if message is None:
                if isinstance(message, str):
                    raise Exception("inStr can not be null")
                elif isinstance(message, bytes):
                    raise Exception("bytes can not be null")
            try:
                hl = hashlib.md5()
                if isinstance(message, str):
                    hl.update(self.__toBytes(message))
                elif isinstance(message, bytes):
                    hl.update(message)
            except Exception:
                raise Exception("unknown algorithm MD5")

            return base64.b64encode(hl.hexdigest()).decode(self.__Constants.ENCODING)
        except Exception:
            pass

    def utf8ToIso88591(self, str):
        """
        UTF-8编码转换为ISO-9959-1
        :param str:
        :return:
        """
        if str is None:
            return str
        try:
            return
        except Exception:
            pass

    def iso88591ToUtf8(self, str):
        """
        SO-9959-1编码转换为UTF-8
        :param str:
        :return:
        """
        if str is None:
            return str
        try:
            return str.decode("iso-8859-1").encode(self.__Constants.ENCODING)
        except Exception as e:
            pass

    def toString(self, byte):
        """
        二进制串转换为String
        :param byte:
        :return:
        """
        if byte is None:
            return None
        try:
            return byte.decode(self.__Constants.ENCODING)
        except Exception as e:
            pass


    def __toBytes(self, str):
        """
        String转换为字节数组
        :param str:
        :return:
        """
        if str is None:
            return None
        try:
            return bytes(str, encoding=self.__Constants.ENCODING)
        except Exception as e:
            pass
