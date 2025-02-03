{
    'name': 'iContact Multi relation',
    'version': '18.0.1.0.0',
    'summary': 'Adds Multi relation in form',
    'description': 'Adds Multi relation in form',
    'author': 'ICRC, Julien MASS',
    'depends': [
        'icrc_icontact',
        'partner_multi_relation'
    ],
    'data': [
        'views/res_partner_view.xml',
        'data/relation_type.xml'
    ],
    # 'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'category': 'iContact',
}