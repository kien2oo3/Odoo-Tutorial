# -*- coding: utf-8 -*-
{
    'name': "module-1",

    'summary': 'Module quản lý thông tin cầu thủ',

    'description': 'Module này cho phép quản lý thông tin về cầu thủ, bao gồm các thông tin như tên, quốc gia, vị trí, chiều cao, cân nặng và hình ảnh.',

    'author': "KienIoT",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    'data': [
        'views/player_views.xml'
    ],

    # any module necessary for this one to work correctly
    'depends': ['base'],

}
