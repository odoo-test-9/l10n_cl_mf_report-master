# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2016 MARLON FALCON HDEZ (<http://www.marlonfalcon.cl>).
# contact: contacto@marlonfalcon.cl

######################################################################

{
    'name': 'MF Report Chile',
    'version': '1.0',
    'author': 'Marlon Falcon Hernandez',
    'category': 'Accounting & Finance',
    'summary': 'Reportes Chile',
    'sequence': 30,
    'website': 'https://www.marlonfalcon.cl',
    'description': """
Es un módulo de reportes
======================
Este módulo configura los siguientes reportes
 * Presupuesto
Nota: Necesita Ventas.
    """,
    'license' : 'AGPL-3',
    'depends': ['base_setup', 'product', 'analytic', 'report'],
    'data': [
        'views/report_saleorder_view.xml',
    ],
    'installable': True,
    'active': False,
    'auto_install': False,
}	