# Copyright 2024 ICRC <https://icrc.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'IContact Demo',
    'version': '18.0.1.0.0',
    'summary': 'Install base IContact module',
    'category': 'iContact',
    'author': 'ICRC, julien MASS',
    'depends': [
        'icrc_icontact',

    ],
    'data': [
        'data/base_setup.xml',         # load lang, currency
        'data/res_company.xml',        # enter company data
    ],
    # 'installable': True,
    'application': False,
    'license': 'LGPL-3',
}