#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: lo0o.xing@gmail.com

import sys

from utility.logger import logger
from phply.phplex import full_lexer, lexer as phplexer
from phply.phpparse import make_parser


def phplex(data):
    lexer = full_lexer
    lexer.input(data)
    _token = lexer.token
    while True:
        tok = _token()
        if not tok:
            break
        sys.stdout.write('(%s,%r,%d,%d)\n' % (tok.type, tok.value, tok.lineno, tok.lexpos))

def phpparse(data):
    parser = make_parser(debug=False)
    s = data
    lexer = phplexer
    lexer.lineno = 1
    try:
        result = parser.parse(s, lexer=lexer.clone(), debug=False)
    except SyntaxError as e:
        if e.lineno is not None:
            logger.error(e, 'near', repr(e.text))
        else:
            logger.error(e)
        raise
    except:
        logger.error("Critical error")
        raise

    import pprint
    for item in result:
        if hasattr(item, 'generic'):
            item = item.generic()
        pprint.pprint(item)
    parser.restart()


class ParsePHP(object):
    def __init__(self, data):
        self.logger = logger
        self.data = data

    def lex(self):
        '''
        get php lex
        :return: list of tokens
        '''
        toks = []
        lexer = full_lexer
        lexer.input(self.data)
        _token = lexer.token
        while True:
            tok = _token()
            if not tok:
                break
            toks.append(tok)
            #sys.stdout.write('(%s,%r,%d,%d)\n' % (tok.type, tok.value, tok.lineno, tok.lexpos))
        return toks

    def get_all_string(self):
        '''
        extract strings of php lex
        :return: string in php
        '''
        strings = ''
        for tok in self.lex():
            if tok.type in ['STRING', 'CONSTANT_ENCAPSED_STRING']:
                strings += tok.value
        return strings


if __name__ == '__main__':
    path = '/Users/lty/Downloads/demon/shell/shell2.php'
    data = open(path, 'r', encoding='latin1').read()
    print(data)
    phplex(data)
    phpparse(data)
    strings = ParsePHP(data).get_all_string()
    print(strings)