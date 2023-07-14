import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\HP\\PycharmProjects\\PhpTravels_Project\\Configuration\\config.ini")


class Readconfig():

    @staticmethod
    def Url():
        url = config.get('common info', 'Url')
        return url

    @staticmethod
    def Email():
        email = config.get('common info', 'Email')
        return email

    @staticmethod
    def Password():
        password = config.get('common info', 'Password')
        return password
