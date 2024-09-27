{
    'name': 'HelpDesk task stage state',
    'version': '16.0.1.0.0',
    'author': 'DAJ MI 5, Odoo Community Association (OCA)',
    'category': 'Helpdesk',
    'license': 'AGPL-3',
    'summary': 'Helpdesk task stage state ',
    'images': [
    ],
    'depends': [
        'helpdesk_mgmt',
    ],
    'data': [
        'views/helpdesk_ticket_stage_views.xml',
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