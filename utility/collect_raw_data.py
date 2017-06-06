#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: lo0o.xing@gmail.com

import os
import shutil
import hashlib

from utility.logger import logger
from conf import global_extens

def file_walk(path):
    '''
    get files list in the path
    :param path: dir path
    :return: the file path list
    '''
    return [os.path.join(root, f) for (root, dirs, files) in os.walk(path) for f in files]


def collect_raw_data(src_path, src_extension, dst_extension, is_webshell=True, check_format=None):
    '''
    transform file to train_set, with sha256sum 
    :param src_path: raw data file path
    :param src_extension: string or list, raw data extension 
    :param dst_extension: string, dst file extension
    :param check_format: check file format or not, eg. php, jsp, .net, py, rube
    :return: 
    '''

    if dst_extension not in global_extens:
        raise Exception('dst extension error, must be one of %s' % str(global_extens))
    extens = src_extension if isinstance(src_extension, list) else src_extension.split(' ')
    cur_path = os.path.split(os.path.realpath(__file__))[0]
    dst_path = os.path.abspath(os.path.join(cur_path, os.path.pardir, 'train_set'))
    fs = [os.path.join(root, f) for (root, dirs, files) in os.walk(src_path) for f in files]
    fs = [f for e in extens for f in fs if f.endswith(e)]
    num = len(fs)
    for f in fs:
        sha256 = hashlib.sha256(open(f, 'rb').read()).hexdigest()
        dst_file = os.path.join(dst_path, dst_extension[1:]+'_webshell', sha256+dst_extension) \
            if is_webshell else os.path.join(dst_path, dst_extension[1:]+'_normal', sha256+dst_extension)
        if os.path.isfile(dst_file):
            num = num -1
        else:
            shutil.copy(f, dst_file)
    logger.info('add %d webshell/files' % num)


if __name__ == '__main__':
    # src_path = '/Users/lty/Downloads/demon/shell'
    # collect_raw_data(src_path, ['.php', '.php.txt'], '.php', True)
    src_path = '/Users/lty/Downloads/wordpress'
    collect_raw_data(src_path, '.php', '.php', is_webshell=False)
    src_path = '/Users/lty/Downloads/phpcms_v9_UTF8'
    collect_raw_data(src_path, '.php', '.php', is_webshell=False)
    src_path = '/Users/lty/Downloads/discuz'
    collect_raw_data(src_path, '.php', '.php', is_webshell=False)