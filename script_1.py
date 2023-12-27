import smtplib
import ssl
from dotenv import load_dotenv
import os
sample = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""


def make_letter():
    site_name_ref = 'https://dvmn.org/referrals/6AnEpHMiwDPOo77YbomGO37JUGzUwywWTsRv6Hzm/'
    friend_name = 'Антонина'
    sender_name = 'Александр Скрипко'
    title_from = 'From: testingprogramms@mail.ru'
    title_to = 'To: testingprogramms@mail.ru'
    title_subject = 'Subject: Приглашение!'
    title_content = 'Content-Type: text/plain, charset="UTF-8";'
    text = sample.replace('%website%', site_name_ref)
    text = text.replace('%friend_name%', friend_name)
    text = text.replace('%my_name%', sender_name)
    letter = f"""{title_from}\n{title_to}\n{title_subject}\n{title_content}\n{text}"""
    letter = letter.encode("UTF-8")
    return letter


def main():
    load_dotenv()
    password = os.getenv("PASSWORD")
    login = os.getenv("LOGIN")
    port = 587
    smtp_server = 'smtp.mail.ru'
    friend_mail = 'testingprogramms@mail.ru'
    message = make_letter()
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.login(login, password)
        server.sendmail(login, friend_mail, message)
        server.quit()


if __name__ == "__main__":
    main()
