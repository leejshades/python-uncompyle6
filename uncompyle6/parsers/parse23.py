#  Copyright (c) 2016 Rocky Bernstein
#  Copyright (c) 2000-2002 by hartmut Goebel <hartmut@goebel.noris.de>
#  Copyright (c) 1999 John Aycock

from spark_parser import DEFAULT_DEBUG as PARSER_DEFAULT_DEBUG
from uncompyle6.parser import PythonParserSingle
from uncompyle6.parsers.parse24 import Python24Parser

class Python23Parser(Python24Parser):

    def __init__(self, debug_parser=PARSER_DEFAULT_DEBUG):
        super(Python24Parser, self).__init__(debug_parser)
        self.customized = {}

    def p_misc23(self, args):
        '''
        _while1test ::= JUMP_FORWARD JUMP_IF_FALSE POP_TOP COME_FROM

        while1stmt ::= SETUP_LOOP _while1test l_stmts JUMP_BACK
                       COME_FROM POP_TOP POP_BLOCK COME_FROM

        list_compr ::= BUILD_LIST_0 DUP_TOP LOAD_ATTR designator list_iter del_stmt
        '''

class Python23ParserSingle(Python23Parser, PythonParserSingle):
    pass

if __name__ == '__main__':
    # Check grammar
    p = Python23Parser()
    p.checkGrammar()
    p.dumpGrammar()

# local variables:
# tab-width: 4
