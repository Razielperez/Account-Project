# AccountProject

This project is a website that allows communication between clients and their accountant, by uploading invoices to the site while allowing editing and deletion.
When on a certain date each month all the files are merged into one file, which is sent to the accountant's email with a WhatsApp message about the arrival of a new file.
And by each month consolidating all customer invoices, creates efficiencies for both parties.

# Technologies:
- python(3.9)
- django 
- SQLite
- jenkins

# Why this project?
I chose to develop this project in order to acquire skills in the languages of Python and Django.

Get to know the world of the web.

Learn uses API ,and sending messages and emails.

Improve my capabilities when used with DB and proper system optimization.

# Running steps:
Installing all extensions:
```python
python -m pip install -r requirements.txt
python -m py_compile manage.py
```
Establishment and connection to a database:
```python
python manage.py makemigrations
python manage.py migrate
```
Start of the project:
```python
python manage.py runserver
```

