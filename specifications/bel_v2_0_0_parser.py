#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

import sys

from tatsu.buffering import Buffer
from tatsu.parsing import Parser
from tatsu.parsing import tatsumasu
from tatsu.util import re, generic_main  # noqa


KEYWORDS = {}  # type: ignore


class BELBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        namechars='',
        **kwargs
    ):
        super(BELBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs
        )


class BELParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        left_recursion=True,
        parseinfo=True,
        keywords=None,
        namechars='',
        buffer_class=BELBuffer,
        **kwargs
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(BELParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            buffer_class=buffer_class,
            **kwargs
        )

    @tatsumasu()
    def _start_(self):  # noqa
        self._bel_statement_()
        self._check_eof()

    @tatsumasu()
    def _bel_statement_(self):  # noqa
        self._function_()
        self.name_last_node('subject')
        self._cut()
        with self._optional():
            self._relation_()
            self.name_last_node('relation')
            self._cut()
            self._obj_()
            self.name_last_node('object')
        self.ast._define(
            ['object', 'relation', 'subject'],
            []
        )

    @tatsumasu()
    def _obj_(self):  # noqa
        with self._group():
            with self._choice():
                with self._option():
                    self._function_()
                with self._option():
                    self._enclosed_statement_()
                self._error('no available options')

    @tatsumasu()
    def _enclosed_statement_(self):  # noqa
        self._function_open_()
        self._bel_statement_()
        self.name_last_node('bel_statement')
        self._function_close_()
        self.ast._define(
            ['bel_statement'],
            []
        )

    @tatsumasu()
    def _function_(self):  # noqa
        self._funcs_()
        self.name_last_node('function')
        self._function_open_()
        self._f_args_()
        self.name_last_node('function_args')
        self._function_close_()
        self.ast._define(
            ['function', 'function_args'],
            []
        )

    @tatsumasu()
    def _funcs_(self):  # noqa
        with self._choice():
            with self._option():
                self._token('cellSurfaceExpression')
            with self._option():
                self._token('compositeAbundance')
            with self._option():
                self._token('biologicalProcess')
            with self._option():
                self._token('microRNAAbundance')
            with self._option():
                self._token('complexAbundance')
            with self._option():
                self._token('proteinAbundance')
            with self._option():
                self._token('cellSecretion')
            with self._option():
                self._token('geneAbundance')
            with self._option():
                self._token('translocation')
            with self._option():
                self._token('rnaAbundance')
            with self._option():
                self._token('degradation')
            with self._option():
                self._token('abundance')
            with self._option():
                self._token('composite')
            with self._option():
                self._token('pathology')
            with self._option():
                self._token('activity')
            with self._option():
                self._token('reaction')
            with self._option():
                self._token('complex')
            with self._option():
                self._token('surf')
            with self._option():
                self._token('list')
            with self._option():
                self._token('list')
            with self._option():
                self._token('path')
            with self._option():
                self._token('tloc')
            with self._option():
                self._token('act')
            with self._option():
                self._token('sec')
            with self._option():
                self._token('deg')
            with self._option():
                self._token('rxn')
            with self._option():
                self._token('bp')
            with self._option():
                self._token('a')
            with self._option():
                self._token('g')
            with self._option():
                self._token('m')
            with self._option():
                self._token('p')
            with self._option():
                self._token('r')
            self._error('no available options')

    @tatsumasu()
    def _f_args_(self):  # noqa

        def sep0():
            self._token(',')

        def block0():
            with self._group():
                with self._choice():
                    with self._option():
                        self._function_()
                    with self._option():
                        self._modifier_function_()
                    with self._option():
                        self._namespace_arg_()
                    with self._option():
                        self._string_arg_()
                    self._error('no available options')
        self._gather(block0, sep0)

    @tatsumasu()
    def _modifier_function_(self):  # noqa
        self._m_funcs_()
        self.name_last_node('modifier')
        self._function_open_()
        self._m_args_()
        self.name_last_node('modifier_args')
        self._function_close_()
        self.ast._define(
            ['modifier', 'modifier_args'],
            []
        )

    @tatsumasu()
    def _m_funcs_(self):  # noqa
        with self._choice():
            with self._option():
                self._token('proteinModification')
            with self._option():
                self._token('molecularActivity')
            with self._option():
                self._token('reactants')
            with self._option():
                self._token('reactants')
            with self._option():
                self._token('fragment')
            with self._option():
                self._token('location')
            with self._option():
                self._token('products')
            with self._option():
                self._token('products')
            with self._option():
                self._token('fromLoc')
            with self._option():
                self._token('fromLoc')
            with self._option():
                self._token('variant')
            with self._option():
                self._token('fusion')
            with self._option():
                self._token('toLoc')
            with self._option():
                self._token('toLoc')
            with self._option():
                self._token('frag')
            with self._option():
                self._token('pmod')
            with self._option():
                self._token('fus')
            with self._option():
                self._token('loc')
            with self._option():
                self._token('var')
            with self._option():
                self._token('ma')
            self._error('no available options')

    @tatsumasu()
    def _m_args_(self):  # noqa

        def sep0():
            self._token(',')

        def block0():
            with self._group():
                with self._choice():
                    with self._option():
                        self._function_()
                    with self._option():
                        self._namespace_arg_()
                    with self._option():
                        self._string_arg_()
                    self._error('no available options')
        self._gather(block0, sep0)

    @tatsumasu()
    def _relation_(self):  # noqa
        self._relations_()

    @tatsumasu()
    def _relations_(self):  # noqa
        with self._choice():
            with self._option():
                self._token('prognosticBiomarkerFor')
            with self._option():
                self._token('prognosticBiomarkerFor')
            with self._option():
                self._token('negativeCorrelation')
            with self._option():
                self._token('positiveCorrelation')
            with self._option():
                self._token('rateLimitingStepOf')
            with self._option():
                self._token('rateLimitingStepOf')
            with self._option():
                self._token('directlyDecreases')
            with self._option():
                self._token('directlyIncreases')
            with self._option():
                self._token('causesNoChange')
            with self._option():
                self._token('hasComponents')
            with self._option():
                self._token('hasComponents')
            with self._option():
                self._token('transcribedTo')
            with self._option():
                self._token('biomarkerFor')
            with self._option():
                self._token('biomarkerFor')
            with self._option():
                self._token('hasComponent')
            with self._option():
                self._token('hasComponent')
            with self._option():
                self._token('subProcessOf')
            with self._option():
                self._token('subProcessOf')
            with self._option():
                self._token('translatedTo')
            with self._option():
                self._token('association')
            with self._option():
                self._token('orthologous')
            with self._option():
                self._token('orthologous')
            with self._option():
                self._token('hasMembers')
            with self._option():
                self._token('hasMembers')
            with self._option():
                self._token('analogous')
            with self._option():
                self._token('analogous')
            with self._option():
                self._token('decreases')
            with self._option():
                self._token('hasMember')
            with self._option():
                self._token('hasMember')
            with self._option():
                self._token('increases')
            with self._option():
                self._token('regulates')
            with self._option():
                self._token('cnc')
            with self._option():
                self._token('isA')
            with self._option():
                self._token('isA')
            with self._option():
                self._token('neg')
            with self._option():
                self._token('pos')
            with self._option():
                self._token('reg')
            with self._option():
                self._token('--')
            with self._option():
                self._token('-|')
            with self._option():
                self._token('=|')
            with self._option():
                self._token('=>')
            with self._option():
                self._token('->')
            with self._option():
                self._token(':>')
            with self._option():
                self._token('>>')
            self._error('no available options')

    @tatsumasu()
    def _namespace_arg_(self):  # noqa
        self._full_nsv_()
        self.name_last_node('ns_arg')
        self.ast._define(
            ['ns_arg'],
            []
        )

    @tatsumasu()
    def _full_nsv_(self):  # noqa
        self._ns_string_()
        self.name_last_node('ns')
        self._token(':')
        with self._group():
            with self._choice():
                with self._option():
                    self._quoted_string_()
                with self._option():
                    self._string_()
                self._error('no available options')
        self.name_last_node('ns_value')
        self.ast._define(
            ['ns', 'ns_value'],
            []
        )

    @tatsumasu()
    def _string_arg_(self):  # noqa
        self._full_string_()
        self.name_last_node('str_arg')
        self.ast._define(
            ['str_arg'],
            []
        )

    @tatsumasu()
    def _full_string_(self):  # noqa
        with self._group():
            with self._choice():
                with self._option():
                    self._quoted_string_()
                with self._option():
                    self._string_()
                self._error('no available options')

    @tatsumasu()
    def _quoted_string_(self):  # noqa
        self._pattern('\\"(?:[^"\\\\]|\\\\.)*\\"')

    @tatsumasu()
    def _string_(self):  # noqa
        self._pattern('[^\\s\\),]+')

    @tatsumasu()
    def _ns_string_(self):  # noqa
        self._pattern('[A-Z0-9]+')

    @tatsumasu()
    def _function_open_(self):  # noqa
        self._token('(')

    @tatsumasu()
    def _function_close_(self):  # noqa
        self._token(')')


class BELSemantics(object):
    def start(self, ast):  # noqa
        return ast

    def bel_statement(self, ast):  # noqa
        return ast

    def obj(self, ast):  # noqa
        return ast

    def enclosed_statement(self, ast):  # noqa
        return ast

    def function(self, ast):  # noqa
        return ast

    def funcs(self, ast):  # noqa
        return ast

    def f_args(self, ast):  # noqa
        return ast

    def modifier_function(self, ast):  # noqa
        return ast

    def m_funcs(self, ast):  # noqa
        return ast

    def m_args(self, ast):  # noqa
        return ast

    def relation(self, ast):  # noqa
        return ast

    def relations(self, ast):  # noqa
        return ast

    def namespace_arg(self, ast):  # noqa
        return ast

    def full_nsv(self, ast):  # noqa
        return ast

    def string_arg(self, ast):  # noqa
        return ast

    def full_string(self, ast):  # noqa
        return ast

    def quoted_string(self, ast):  # noqa
        return ast

    def string(self, ast):  # noqa
        return ast

    def ns_string(self, ast):  # noqa
        return ast

    def function_open(self, ast):  # noqa
        return ast

    def function_close(self, ast):  # noqa
        return ast


def main(filename, start=None, **kwargs):
    if start is None:
        start = 'start'
    if not filename or filename == '-':
        text = sys.stdin.read()
    else:
        with open(filename) as f:
            text = f.read()
    parser = BELParser()
    return parser.parse(text, rule_name=start, filename=filename, **kwargs)


if __name__ == '__main__':
    import json
    from tatsu.util import asjson

    ast = generic_main(main, BELParser, name='BEL')
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(asjson(ast), indent=2))
    print()
