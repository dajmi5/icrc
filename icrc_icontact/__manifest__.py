{
    'name': 'ICRC IContact Fields',
    'version': '18.0.1.0.0',
    'summary': 'Adds custom fields to the Contact form in Odoo 16',
    'description': 'POC : Adding new field to contact',
    'category': 'Contacts',
    'author': 'ICRC, julien MASS',
    'depends': [
        'contacts',
        'partner_firstname',
        'partner_contact_gender',
        'icrc_military_rank',
        'web_hierarchy'
    ],
    'data': [
        'security/security_groups.xml',
        'views/res_partner_views.xml',
    ],
    #'installable': True,
    'application': False,
    'license': 'LGPL-3',
}