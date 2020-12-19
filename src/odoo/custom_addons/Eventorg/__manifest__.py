{
    'name': 'EventOrganization',
    'category': 'Management',
    'summary': 'Manage the Event Organization ',
    'description': """
This module offers the basic functionalities to manage the employees and customers in an event organisation company.
    """,
    'depends': ['base','hr','calendar','analytic'],
    'data': [
     'views/org_details.xml',
     'views/team_scheduling.xml',
     'views/manage_team_views.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}