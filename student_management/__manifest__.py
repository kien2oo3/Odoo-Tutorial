{
    'name': "Module student management",
    'version': '1.0',
    'depends': ['base'],
    'author': "Kien Bui",
    'category': 'Category',
    'description': "This is Module student management",
    'license': 'LGPL-3',
    'data':[
        'security/ir.model.access.csv',
        'controllers/StudentController.xml',
        'controllers/ClassController.xml',
        'controllers/CourseController.xml',
        'views/student_views.xml',
        'views/class_views.xml',
        'views/course_views.xml',
        'views/res_partner_views.xml',
        'views/menu.xml',
    ]
}