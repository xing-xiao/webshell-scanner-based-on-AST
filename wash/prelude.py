#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: lo0o.xing@gmail.com

import os
import pandas as pd
from utility.logger import logger
from conf import global_extens
from wash.entropy import Entropy

class Prelude(object):
    def __init__(self):
        self.cur_path = os.path.split(os.path.realpath(__file__))[0]
        self.train_path = os.path.abspath(os.path.join(self.cur_path, os.path.pardir, 'train_set'))
        self.index, is_webshell, self.fs = self.prelude()
        self.dataframe = pd.DataFrame(is_webshell, columns=['is_webshell'], index=self.index)
        self.logger = logger

    def prelude(self):
        index = []
        is_webshell = []
        fs = []
        for root, dirs, files in os.walk(self.train_path):
            for f in files:
                if f[64:] in global_extens:
                    index.append(f[:64])
                    if root.endswith('webshell'):
                        is_webshell.append(1)
                        fs.append(os.path.join(root, f))
                    elif root.endswith('normal'):
                        is_webshell.append(0)
                        fs.append(os.path.join(root, f))
                    else:
                        self.logger.warning('file %s not in right path %s' % (f, root))
        return index, is_webshell, fs

    def concat_string_entropy(self):
        entropys = Entropy().entropy_dir_strings(self.fs)
        pd1 = pd.DataFrame(entropys, columns=['string_entropy'], index=self.index)
        self.dataframe = pd.concat([self.dataframe, pd1], axis=1)




if __name__ == '__main__':
    Prelude().prelude()
    Pre = Prelude()
    #print(Pre.dataframe)
    Pre.concat_string_entropy()
    Pre.dataframe.to_csv('pd.csv')