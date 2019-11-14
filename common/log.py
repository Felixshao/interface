import os
import logging
from logging.handlers import TimedRotatingFileHandler
from config.getPathInfo import get_path

path = get_path()
log_path = os.path.join(path, 'result')


class Logger(object):
    def __init__(self, logger_name='logs...'):  # 初始化变量
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = 'logs.log'     # 日志文件名称
        self.backuo_count = 5   # 设置日志文件最多存放数量
        # 日志输出级别
        self.console_output_level = 'DEBUG'
        self.file_output_level = 'DEBUG'
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        if not self.logger.handlers:
            console_handle = logging.StreamHandler()
            console_handle.setFormatter(self.formatter)
            console_handle.setLevel(self.console_output_level)
            self.logger.addHandler(console_handle)

            # 每天重新创建一个log文件，最多保存backuo_count份
            file_handle = TimedRotatingFileHandler(filename=os.path.join(log_path, self.log_file_name), when='D',
                                                   interval=1, backupCount=self.backuo_count, delay=True,
                                                   encoding='utf-8')
            file_handle.setFormatter(self.formatter)
            file_handle.setLevel(self.file_output_level)
            self.logger.addHandler(file_handle)
        return self.logger

logger = Logger().get_logger()



