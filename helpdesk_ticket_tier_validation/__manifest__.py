{
    'name': 'HelpDesk task tier validation',
    'version': '16.0.1.0.0',
    'author': 'DAJ MI 5, Odoo Community Association (OCA)',
    'category': 'Helpdesk',
    'license': 'AGPL-3',
    'summary': 'Helpdesk task tier validation ',
    'images': [
    ],
    'depends': [
        'helpdesk_task_stage_state',
        'base_tier_validation'
    ],
    'data': [
        'views/helpdesk_ticket_views.xml'
    ],
    'qweb': [

    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}