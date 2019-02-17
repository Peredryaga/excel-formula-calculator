# coding: utf8

from __future__ import unicode_literals, print_function
from efc.utils import u
import six


class BaseEFCException(Exception):
    code = None
    msg = None

    def __str__(self):
        context = {k: u(i) for k, i in six.iteritems(self.__dict__)}
        msg_list = []
        if self.code is not None:
            msg_list.append('Code %d' % self.code)
        if self.msg:
            msg_list.append(self.msg.format(**context))
        if self.__dict__.get('formula'):
            msg_list.append('Formula: %s' % self.__dict__['formula'])
        if self.__dict__.get('ws_name'):
            msg_list.append('WS: %s' % self.__dict__['ws_name'])
        return '. '.join(msg_list)
