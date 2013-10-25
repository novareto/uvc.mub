# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


from uvc.mub import MUBPrincipal, IMUBPrincipal


def test_base():
    assert 1 == 1


def test_principal():
    assert IMUBPrincipal.implementedBy(MUBPrincipal) is True


def test_adaption():
    from zope.security.interfaces import IPrincipal
    from zope.interface import implementer
    @implementer(IPrincipal)
    class Principal(object):
        def __init__(self, name):
            self.name=name
    import pdb; pdb.set_trace()
    chris = Principal('chris')
    mub_principal = IMUBPrincipal(chris)

