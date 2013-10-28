# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

from .interfaces import IMUBPrincipal
from zope.interface import implementer

try:
    # we are using zope security
    from zope.security.interfaces import IPrincipal
    from zope.component import adapter
except:
    from crom import adapter
    from cromlech.security import IPrincipal


@implementer(IMUBPrincipal)
@adapter(IPrincipal)
class MUBPrincipal(object):

    def __init__(self, principal):
        self.principal = principal

    def getAdresse(self):
        return {}
