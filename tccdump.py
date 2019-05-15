from nuxeo.client import Nuxeo
import csv

def writefile(docId):
   doc=nuxeo.documents.get(uid=docId)
   output_filename = docId + '.pdf'
   output_file = open(output_filename, "wb")
   output_file.write(doc.fetch_blob())
   output_file.close()


nuxeo=Nuxeo(
host='http://eagle.wisepoint.info:8082/nuxeo/', 
auth=('UserName', 'Password')
)

with open('test.csv') as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',')
   for row in csv_reader:
      print(row[0])
      writefile(row[0])


