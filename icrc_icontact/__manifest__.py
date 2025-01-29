{
    'name': 'ICRC iContact app',
    'version': '18.0.1.0.0',
    'sequence': 1,
    'summary': 'iContact management ',
    'description': 'iContact management additional fields',
    'category': 'iContact',
    'author': 'ICRC, julien MASS',
    'depends': [
        'contacts',
        'partner_firstname',
        'partner_contact_gender',
        'web_hierarchy',
    ],
    'data': [
        'security/security_groups.xml',
        'views/res_config_settings.xml',
        'views/res_partner_views.xml',
        # 'views/icrc_referential.xml',  moved to module
    ],
    #'installable': True,
    'application': True,
    'license': 'LGPL-3',
}