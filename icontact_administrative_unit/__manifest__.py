{
    'name': 'ICRC IContact Administratoce Units',
    'version': '18.0.1.0.0',
    'summary': 'Adds Administratove unots related to contacts',
    'description': 'POC : Adding new field to contact',
    'category': 'iContact',
    'author': 'ICRC, julien MASS',
    'depends': [
        'icrc_icontact',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/admin_unit_views.xml',

    ],
    #'installable': True,
    'application': False,
    'license': 'LGPL-3',
}