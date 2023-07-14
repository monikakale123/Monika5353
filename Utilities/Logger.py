import logging
import inspect

class LogGenerate:

    @staticmethod
    def Logg():
        name = inspect.stack()[1][3]
        log = logging.getLogger(name)
        logfile = logging.FileHandler("C:\\Users\\HP\PycharmProjects\\PhpTravels_Project\\Logs\\Automation_logs.log")
        format1 = logging.Formatter("%(levelno)s : %(levelname)s : %(lineno)s : %(funcName)s : %(message)s : %(asctime)s")
        logfile.setFormatter(format1)
        log.addHandler(logfile)
        log.setLevel(logging.INFO)
        return log



























# import logging
# import inspect
#
#
# class LogGenerate:
#
#     @staticmethod
#     def logg():
#         name = inspect.stack()[1][3]
#         log = logging.getLogger(name)
#         logfile = logging.FileHandler("C:\\Users\\HP\\PycharmProjects\\PhpTravels_Project\\Logs\\Automation_logs.log")
#         format1 = logging.Formatter('%(asctime)s : %(levelname)s : %(levelno)s : %(lineno)s : %(funcName)s : %('
#                                     'message)s')
#         logfile.setFormatter(format1)
#         log.addHandler(logfile)
#         log.setLevel(logging.INFO)
#         return log







