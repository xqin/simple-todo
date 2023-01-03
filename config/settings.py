#!/usr/bin/env python
# coding: utf-8
import web

db = web.database(dbn='mysql', host='1.1.1.1', port=3306, db='todo', user='xxx', pw='yyyy')

render = web.template.render('templates/', cache=False)

web.config.debug = True

config = web.storage(
    email='qichangxing@gmail.com',
    site_name = '任务跟踪',
    site_desc = '',
    static = '/static',
)


web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
