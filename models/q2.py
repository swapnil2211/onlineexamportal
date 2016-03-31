# -*- coding: utf-8 -*-
db.define_table('quiz2a',
                Field('Ans',requires=IS_IN_SET(["A","B","C","D"])))
db.define_table('quiz2b',
                Field('Ans',requires=IS_IN_SET(["A","B","C","D"])))
db.define_table('quiz2c',
                Field('Ans',requires=IS_IN_SET(["A","B","C","D"])))
db.define_table('quiz2d',
                Field('Ans',requires=IS_IN_SET(["A","B","C","D"])))
db.define_table('quiz2e',
                Field('Ans',requires=IS_IN_SET(["A","B","C","D"])))
