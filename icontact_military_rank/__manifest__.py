{
    'name': 'iContact - Military Rank',
    'version': '18.0.1.0.0',
    'category': 'iContact',
    'summary': 'Adds Military rank in Odoo 16',
    'description': 'Adding military rank',
    'author': 'ICRC, julien MASS',
    'depends': [
        'icrc_icontact'
    ],
    'data': [
        #'security/security_groups.xml',
        'security/ir.model.access.csv',
        'views/military_rank_views.xml',
        'views/res_partner_views.xml'
    ],
    # 'installable': True,
    'application': False,
    'license': 'LGPL-3',
}