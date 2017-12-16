#!/usr/local/bin/python3

# import psycopg2 the DB API driver complaint with PostgreSQL
import psycopg2 as p

# All questions and queries are loaded into variables
question1 = 'What are the most popular three articles of all time?'
query1 = '''
    SELECT title, count(*) AS views
    FROM articles
    INNER JOIN log
    ON concat('/article/', articles.slug) = log.path
    WHERE log.status = '200 OK'
    GROUP BY articles.title
    ORDER BY views desc limit 3;
    '''
question2 = 'Who are the most popular article authors of all time?'
query2 = '''
    SELECT authors.name, count(*)
    FROM articles
    INNER JOIN authors ON articles.author = authors.id
    INNER JOIN log
    ON log.path = concat('/article/', articles.slug)
    WHERE log.status = '200 OK'
    GROUP BY authors.name
    ORDER BY count desc;
    '''
question3 = 'On which days did more than 1% of requests lead to errors?'
query3 = '''
    SELECT * FROM (
        SELECT total.day,
        round(100*errors.count / total.count, 2) AS percenterror
        FROM
            (SELECT date(time) AS day, count(*)::numeric AS count
            FROM log GROUP BY day) AS total
            inner join
            (SELECT date(time) AS day, count(*)::numeric AS count
            FROM log
            WHERE status LIKE '%404%' GROUP BY day) AS errors
            ON total.day = errors.day)
    AS values WHERE percenterror > 1;
    '''


class Activate:
    def __init__(self):
        try:
            self.activate = p.connect('dbname=news')
            self.cursor = self.activate.cursor()
        except Exception:
            print("Database Connection Error!")

    # Simple formatter that draws a double line after each question
    def formatter(self, num=55, sep='='):
        print(sep * num)

    def perform_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def answer(self, question, query, view='views'):
        result = self.perform_query(query)
        print (question)
        self.formatter()
        for i in range(len(result)):
            print ('\t', i + 1, '.', result[i][0], '--',
                   '{:,}'.format(result[i][1]), view, '\n')

    def exit(self):
        self.deactivate = self.activate.close()
        return self.deactivate


if __name__ == '__main__':
    activated = Activate()
    activated.answer(question1, query1)
    activated.answer(question2, query2)
    activated.answer(question3, query3, '% Error')
    activated.exit()
