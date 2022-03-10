#!/usr/bin/env python3
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2021 Authors and contributors
#
# Released under the GNU Public Licence, v2 or any higher version
# SPDX-License-Identifier: GPL-2.0-or-later

"""Wrapper of argparse library.

Prepares helps and descriptions from numpy style docstrings and function 
inspection.

The classes are inspired by the dsargparse library 
(https://github.com/jkawamoto/dsargparse)
"""

import argparse

from .utils import parse_docs

class _SubparsersWrapper:
    """Wrapper of the action object made by argparse.ArgumentParser.add_subparsers.
    To create an instance, the constructor takes a reference to an instance of
    the action class.
    """
    __slots__ = ("__delegate")

    def __init__(self, delegate):
        self.__delegate = delegate

    def add_parser(self, func=None, name=None, **kwargs):
        if func:
            if not func.__doc__:
                raise ValueError(
                    "No docstrings given in {0}".format(func.__name__))

            print(func)

            if not name:
                name = func.__name__ if hasattr(func, "__name__") else func

        else:
            res = self.__delegate.add_parser(name, **kwargs)

        return res

    def __repr__(self):
        return self.__delegate.__repr__()

class ArgumentParser(argparse.ArgumentParser):

    def __init__(self, main=None, argmap=None, *args, **kwargs):
        super(ArgumentParser, self).__init__(*args, **kwargs)

    def add_subparsers(self, **kwargs):
        return _SubparsersWrapper(
            super(ArgumentParser, self).add_subparsers(**kwargs))