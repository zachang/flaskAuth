# coding=utf-8
import os


class Config(object):
    """SECRET_KEY object"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
2