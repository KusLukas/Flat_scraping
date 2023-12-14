# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
import csv



class FlatPipeline:

    def __init__(self):
        hostname = 'db'#local host for non compose usage
        username = 'postgres'
        password = 'SPS_pass'
        database = 'flats'
        port="5432"

        self.con = psycopg2.connect(host=hostname, user=username, password=password, dbname=database,port=port)
        self.con.autocommit = True
        self.cur = self.con.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS flats_items(
            id serial PRIMARY KEY,
            Title text,
            Image_url text
        )
        """)
        self.cur.execute("DELETE FROM flats_items")


    def process_item(self, item, spider):
        self.cur.execute(""" INSERT INTO flats_items (Title, Image_url) values (%s,%s)""", (
            item["Title"],
            str(item["Image_url"]),
        ))
        self.con.commit()
        return item


    def close_spider(self, spider):
        self.cur.execute("SELECT * FROM flats_items")

        results = self.cur.fetchall()

        # with open("output.csv", "w", newline="") as f:#to check validity of database
        #     writer = csv.writer(f)
        #     writer.writerow([col[0] for col in self.cur.description])
        #     writer.writerows(results)
        #     writer.writerows("test")

        with open('/usr/src/server/Flat_page.html', 'w', encoding="utf-8") as file:
            file.write("<html>")
            file.write("<meta charset=UTF-8 / >")
            file.write("<head>")
            file.write("<title>Flats: Names and overview images</title>")
            file.write("</head>")
            file.write("<body>")
            file.write("<h1>Flats: Names and overview images</h1>")

            file.write('<table style="border: solid black;">\n')
            for i in (range(0,int(len(results)),1)):#define structure of page, currently 4columns
                if i%4==0:
                    file.write('<tr>\n')
                file.write(f'<td>{(results[i][1])}</td>')
                file.write(f'<td><img src ='+str(results[i][2])+'></td>')
                # print(type(results))
                if i%4==3:
                    file.write('</tr>\n')

            file.write('</table>')
            file.write("</body>")
            file.write("</html>")
            file.close()

        self.cur.close()
        self.con.close()
