#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Internationalization test.

import gettext
_ = gettext.gettext

def printSomeMessages():
    print(_("Hello world!"))
    print(_("This is a translate message."))

import os
import sys
localedir=os.path.dirname(os.path.abspath(sys.argv[0])) + '/../locales'

zh_CN = gettext.translation('base', localedir, languages=['zh_CN']);
zh_CN.install()
_ = zh_CN.gettext

if __name__ == '__main__':
    printSomeMessages()
