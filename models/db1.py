# -*- coding: utf-8 -*-
db.define_table('Profile',Field('Name','string',requires=IS_NOT_EMPTY()),
               Field('Name','text',requires=IS_NOT_EMPTY()),
               Field('Address','text',requires=IS_NOT_EMPTY()),
              Field('birthdate','date',requires=IS_NOT_EMPTY()),
              Field('email',unique=True,requires=[IS_NOT_EMPTY(),IS_EMAIL()]),
              Field('Sex',requires=IS_IN_SET(["Male","Female"])))
db.Profile.email.requires=IS_NOT_IN_DB(db,'Profile.email')
