from db.db_utils import *

estudantes = [('Ana Silva', 'Computação',2019),
 ('Pedro Mendes', 'Física',2021),
 ('Carla Souza', 'Computação',2020),
 ('João Alves', 'Matemática',2018),
 ('Maria Oliveira', 'Química',2022)]

create_table('Estudantes', """(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    Ano_de_Ingresso INTEGER
)""")

insert_many('Estudantes', estudantes, '(Nome, Curso, Ano_de_Ingresso)','?, ?, ?' )

select('Estudantes', 'Ano_de_Ingresso', '2019', 'or Ano_de_Ingresso == 2020')

update('Estudantes', 'Ano_de_Ingresso', 1500, 'ID == 2')

delete('Estudantes','ID', '5' )

select('Estudantes', 'Ano_de_Ingresso', '2019', 'AND Curso == "Computação"')

update('Estudantes', 'Ano_de_Ingresso', 2018,'Curso == "Computação"'  )