# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


from zope.interface import Interface



class IMUBPrincipal(Interface):
    """Generic Principal for CUSA-MUB
    """

    def getAddress():
        """Return Adress Information
        """
