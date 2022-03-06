# -*- coding: utf-8 -*-
{
    'name': "Second Hand",  # Module title
    'summary': "Manage games easily",  # Module subtitle phrase
    'description': """
Manage Library of Games
==============
Description related to game library.
    """,  # Supports reStructuredText(RST) format
    'author': "GameStock",
    'website': "http://www.gamestock.com",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base'],

    'data': [
        'security/groups.xml',
        'views/library_game.xml',
        'views/library_game_categ.xml',
        'reports/games_report.xml',
        # Si no carga demo data, este siempre carga
        #'demo/demo.xml',               
    ],

    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,   
}



