#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: lo0o.xing@gmail.com

import math
import os
from utility.parsephp import ParsePHP
from utility.logger import logger


class Entropy(object):
    def __init__(self):
        self.result = ''
        self.logger = logger

    def entropy_file_content(self, x):
        '''
        calculate information entropy of all file content
        :param x: the content of file
        :return: the value of information entropy
        '''
        if not x:
            return 0
        entropy = 0
        stripped_data = x.replace(' ', '')
        for x in range(256):
            p_x = float(stripped_data.count(chr(x))) / len(stripped_data)
            if p_x > 0:
                entropy += - p_x * math.log(p_x, 2)
        return entropy

    def entropy_dir_content(self, fs):
        '''
        calcuat information entropy of files in dir
        :param dir: file list
        :return: the dict of entropy
        '''
        entropys = []
        for f in fs:
            x = open(f, 'r', encoding='latin1').read()
            entropy = self.entropy_file_content(x)
            entropys.append(entropy)
        return entropys

    def entropy_file_strings(self, x):
        '''
        calculate information entropy of strings in file
        :param x: the content of file
        :return: the value of information entropy
        '''
        if not x:
            return 0
        entropy = 0
        stripped_data = ParsePHP(x).get_all_string().replace(' ', '')
        if len(stripped_data) == 0:
            return 0
        for x in range(256):
            p_x = float(stripped_data.count(chr(x))) / len(stripped_data)
            if p_x > 0:
                entropy += - p_x * math.log(p_x, 2)
        return entropy

    def entropy_dir_strings(self, fs):
        '''
        calculate information entropy of string in dir
        :param dir: the path of file
        :return: the dict of entropy
        '''
        entropys = []
        for f in fs:
            x = open(f, 'r', encoding='latin1').read()
            entropy = self.entropy_file_strings(x)
            entropys.append(entropy)
        return entropys


if __name__ == '__main__':

    E = Entropy()
    f1 = '/Users/lty/gitHub/webshell-scanner-based-on-AST/train_set/php_webshell/0a0944635d48b8d4a44068847e8958710c644233a5227bc193bbd34999dc2131.php'
    print(E.entropy_file_content(open(f1, 'r', encoding='latin1').read()))

    f2 = '/Users/lty/gitHub/webshell-scanner-based-on-AST/train_set/php_webshell/0a5f8c8a6f82be68b260ebcbd8d917e9209f548ea1ca5827e7d27d6653f8170a.php'
    print(E.entropy_file_content(open(f2, 'r', encoding='latin1').read()))

    f3 = '/Users/lty/gitHub/webshell-scanner-based-on-AST/train_set/php_webshell/0a29cf1716e67a7932e604c5d3df4b7f372561200c007f00131eef36f9a4a6a2.php'
    print(E.entropy_file_content(open(f3, 'r', encoding='latin1').read()))

    f5 = '/Users/lty/Downloads/demon/shell/shell3.php'
    print(E.entropy_file_content(open(f5, 'r', encoding='latin1').read()))

    print(E.entropy_file_strings(open(f1, 'r', encoding='latin1').read()))
    print(E.entropy_file_strings(open(f2, 'r', encoding='latin1').read()))
    print(E.entropy_file_strings(open(f3, 'r', encoding='latin1').read()))
    print(E.entropy_file_strings(open(f5, 'r', encoding='latin1').read()))