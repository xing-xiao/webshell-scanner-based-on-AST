#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: lo0o.xing@gmail.com

import logging
# create logger
logger_name = "example"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)
# create file handler
log_path = "default.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.DEBUG)
# create formatter
fmt = "[%(asctime)-15s] [%(levelname)s] [%(filename)s] [line:%(lineno)d] [pid:%(process)d] %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)
# add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)