# -*- coding: utf-8 -*-
class Config(object):
    DEBUG = False

    ISSUE_STATUS = {10: '待处理', 20: '处理中', 30: '完结(需求上线）', 31: '完结(需求方已评价）', 40: '不予处理'}  # Status
