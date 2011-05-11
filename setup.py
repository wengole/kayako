# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2011, Evan Leis
#
# Distributed under the terms of the GNU General Public License (GPL)
#-----------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name='kayako',
    version='4.01.204',
    author='Evan Leis',
    author_email='engineergod@yahoo.com',
    url='',
    install_requires=[
        "lxml",
    ],
    setup_requires=[],
    packages=find_packages(exclude=[]),
    include_package_data=True,
    test_suite='kayako.tests',
    package_data={},
    zip_safe=True,
    entry_points="""
    """,
    license="GNU General Public License (GPL)",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="Python API Wrapper for Kayako 4.01.204",
    long_description='''
Python API wrapper for Kayako 4.01.204
--------------------------------------
    
*NOTE: Tests require your input. To test this code against your installation of 
Kayako, modify kayako.tests.__init__.py filling in API_URL, API_KEY, and 
SECRET_KEY.*

**Usage:**

::

    from kayako import KayakoAPI, User, Ticket, Department, UnsetParameter
    api = KayakoAPI('http://kayako.foo.com/api/index.php', 's8v092-2lksd-9cso-c2', 'somesecret')
    departments = api.get_all(Department)
    for department in departments:
        # Print every ticket in every department
        tickets = api.get_all(Ticket, department.id)
        for ticket in tickets:
            print department, ticket
    >>> <Department...> <Ticket...>
    >>> <Department...> <Ticket...>
    >>> <Department...> <Ticket...>
    
**Add an object**

::

    department = api.create(Department)
    department.title = 'Food Department' # Department author was hungry
    department.module = 'tickets'
    department.type = 'private'
    assert department.id is UnsetParameter
    department.add()
    assert department.id is not UnsetParameter
    department.title = 'Foo Department' # 'Food' was supposed to be 'Foo'
    department.save()
    department.delete()

**API Factory Methods:**

``api.create(Object)``

    Create and return a new KayakoObject of the type given.
    
``api.get_all(Object, *args, **kwargs)``

    *Get all Kayako Objects of the given type.*
    *In most cases, all items are returned.*
    
    e.x.::
        api.get_all(Department)
        >>> [<Department....>, ....]

    *Special Cases:*
    
        ``api.get_all(User, marker=1, maxitems=1000)``
            Return all Users from userid ``marker`` with up to ``maxitems`` 
            results (max 1000.)
            
        ``api.get_all(Ticket, departmentid, ticketstatusid=-1, ownerstaffid=-1, userid=-1)``
            Return all Tickets filtered by the required argument 
            ``departmentid`` and by the optional keyword arguments.
            
        ``api.get_all(TicketAttachment, ticketid)``
            Return all TicketAttachments for a Ticket with the given ID.
            
        ``api.get_all(TicketPost, ticketid)``
            Return all TicketPosts for a Ticket with the given ID.

``api.get(Object, *args)``

    *Get a Kayako Object of the given type by ID.*
    
    e.x.
        ``api.get(User, 112359)``
        ``>>> <User (112359)....>``
    
    *Special Cases:*
        
        ``api.get(TicketAttachment, ticketid, attachmentid)``
            Return a ``TicketAttachment`` for a ``Ticket`` with the given Ticket
            ID and TicketAttachment ID.  Getting a specific ``TicketAttachment``
            gets a ``TicketAttachment`` with the actual attachment contents.
        
        ``api.get(TicketPost, ticketid, ticketpostid)``
            Return a ``TicketPost`` for a ticket with the given Ticket ID and
            TicketPost ID.
            
**Object persistence methods**

``kayakoobject.add()``
    *Adds the instance to Kayako.*
``kayakoobject.save()``
    *Saves an existing object the instance to Kayako.*
``kayakoobject.delete()``
    *Removes the instance from Kayako*
    
These methods can raise exceptions:

    Raises ``KayakoRequestError`` if one of the following is true:
        - The action is not available for the object
        - A required object parameter is UnsetParameter or None (add/save)
        - The API URL cannot be reached
        
    Raises ``KayakoResponseError`` if one of the following is true:
        - There is an error with the request (not HTTP 200 Ok)
        - The XML is in an unexpected format indicating a possible Kayako version mismatch (expects 4.01.204)
    
**Quick Reference**

================= ====================================================================== ========================= ======= ======= =====================
Object            Get All                                                                Get                       Add     Save    Delete
================= ====================================================================== ========================= ======= ======= =====================
Department        Yes                                                                    Yes                       Yes     Yes     Yes
Staff             Yes                                                                    Yes                       Yes     Yes     Yes
StaffGroup        Yes                                                                    Yes                       Yes     Yes     Yes
Ticket            departmentid, ticketstatusid= -1, ownerstaffid= -1, userid= -1         Yes                       Yes     Yes     Yes
TicketAttachment  ticketid                                                               ticketid, attachmentid    Yes     No      Yes
TicketNote        ticketid                                                               No                        Yes     No      No (delete ticket)
TicketPost        ticketid                                                               ticketid, postid          Yes     No      Yes
TicketPriority    Yes                                                                    Yes                       No      No      No
TicketStatus      Yes                                                                    Yes                       No      No      No
TicketType        Yes                                                                    Yes                       No      No      No
User              marker=1, maxitems=1000                                                Yes                       Yes     Yes     Yes
UserGroup         Yes                                                                    Yes                       Yes     Yes     Yes
UserOrganization  Yes                                                                    Yes                       Yes     Yes     Yes
================= ====================================================================== ========================= ======= ======= =====================

''',
)
