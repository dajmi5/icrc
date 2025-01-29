{
    'name': 'ICRC Partner administrative unit',
    'version': '18.0.1.0.0',
    'summary': 'Adds Location + 3 administratove levels above',
    'description': 'POC : Adding new field to contact',
    'category': 'iContact',
    'author': 'ICRC, julien MASS',
    'depends': [
        'contacts',
        #'web_hierarchy'
    ],
    'data': [
        "security/ir.model.access.csv",
        'views/icrc_referential.xml',
        #'views/res_partner_views.xml',

    ],
    #'installable': True,
    'application': False,
    'license': 'LGPL-3',
}