import re
text = "Контакты: ivanov@example.com, petrov@work.net, sid@mail.ru."
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
emails = re.findall(email_pattern, text)
print(emails)