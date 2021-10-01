#!/usr/bin/env python3

import cgi
import model

print("Content-type: text/html")
print()
#print("<h1>Hello world!</h1>")

form = cgi.FieldStorage()

fn = ''
mn = ''
ln = ''
bd = ''

if 'first_name' in form:
    fn = form['first_name'].value
if 'middle_name' in form:
    mn = form['middle_name'].value
if 'last_name' in form:
    ln = form['last_name'].value
if 'birth_date' in form:
    bd = form['birth_date'].value

record = model.record(fn, mn, ln, bd)
no_records, table = model.find_records(record)

print(record)
print('<br><br>')
print('Найдено записей: ', no_records)
print('<br><br>')
print(table)

"""""

message = None
full_name = None

if 'image' in form:
    fileitem = form['image']
    fn = os.path.basename(fileitem.filename)
    full_name = os.path.join(os.getcwd(), 'files', fn)
    open(full_name, 'wb').write(fileitem.file.read())
    message = fn + ' was uploaded, result: ' + str(model.processImage(full_name))
else:
    message = 'No image'

"""
