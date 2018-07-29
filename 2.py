# -*- coding: utf-8 -*-
import sys
import os
import datetime
from collections import Counter


LOGFILE = 'a.log'


class CountSql(object):
    def __init__(self, log_file):
        self.log_file_path = log_file
        # self.time_flag = datetime.datetime.fromtimestamp(0)
        self.time_flag = None
        self.one_minute = datetime.timedelta(minutes=1)
        self.log_in_a_minute = list()

    def check_input(self):
        if not os.path.isfile(self.log_file_path):
            print "未找到日志文件"
            sys.exit(1)

    def handle_file(self):
        self.check_input()
        with open(self.log_file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                content = line.split('"')
                log_time = datetime.datetime.strptime(content[0].strip(), '%Y-%m-%d %H:%M:%S')
                sql_str = content[1].strip()
                if self.time_flag is None:
                    self.time_flag = log_time
                self.minute_iter(log_time, sql_str)

            self.select_top_one()

    def minute_iter(self, log_time, sql_str):
        if log_time - self.time_flag < self.one_minute:
            # yield sql_str
            self.log_in_a_minute.append(sql_str)
        else:
            self.select_top_one()
            self.time_flag = log_time
            self.log_in_a_minute = [sql_str]

    def select_top_one(self):
        c = Counter(self.log_in_a_minute)
        print c.most_common(1)[0][0]
        # TODO: 如果一分钟内每个sql只有一个如何输出？


if __name__ == '__main__':
    counter = CountSql(LOGFILE)
    counter.handle_file()
