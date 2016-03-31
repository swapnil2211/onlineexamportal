# -*- coding: utf-8 -*-
db.define_table('quiz',
                Field('Ans',requires=IS_IN_SET(["A","B","C","D"])))
db.define_table('quizb',
                Field('Ans',requires=IS_IN_SET(["A","B","C","D"])))
db.define_table('quizc',
                Field('Ans',requires=IS_IN_SET(["A","B","C","D"])))
db.define_table('quizd',
                Field('Ans',requires=IS_IN_SET(["A","B","C","D"])))
db.define_table('quize',
                Field('Ans',requires=IS_IN_SET(["A","B","C","D"])))
