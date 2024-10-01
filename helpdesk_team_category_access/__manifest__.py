{
    'name': 'HelpDesk team category',
    'version': '16.0.1.0.0',
    'author': 'DAJ MI 5, Odoo Community Association (OCA)',
    'category': 'Helpdesk',
    'license': 'AGPL-3',
    'summary': 'Helpdesk Team category management',
    'images': [
    ],
    'depends': [
        'helpdesk_mgmt',
    ],
    'data': [
        'views/helpdesk_team_views.xml',
        'views/helpdesk_ticket_category_views.xml',
        'views/helpdesk_ticket_views.xml',
    ],
    'qweb': [

    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}