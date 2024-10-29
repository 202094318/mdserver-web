# coding:utf-8

# ---------------------------------------------------------------------------------
# MW-Linux面板
# ---------------------------------------------------------------------------------
# copyright (c) 2018-∞(https://github.com/midoks/mdserver-web) All rights reserved.
# ---------------------------------------------------------------------------------
# Author: midoks <midoks@163.com>
# ---------------------------------------------------------------------------------

from flask import request

from admin import model
from admin.model import db, Users

import core.mw as mw

def init_option():
    model.setOption('title', '后羿面板')
    model.setOption('recycle_bin', 'open')
    model.setOption('template', 'default')

    # 开启后台任务
    # model.setOption('run_bg_task', 'close')

    # 首页展示初始化
    model.setOption('display_index', '[]')

    # 监控默认配置
    model.setOption('monitor_status', 'open', type='monitor')
    model.setOption('monitor_day', '30', type='monitor')
    model.setOption('monitor_only_netio', 'open', type='monitor')

    # 初始化安全路径
    model.setOption('admin_path', mw.getRandomString(8))
    model.setOption('server_ip', '127.0.0.1')

    return True