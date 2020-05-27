import smtplib
import glob
import re
import time
import os

LOG_PATH = r'C:\Users\ww\Desktop\logs\OpenHardwareMonitor'
CPU_TEMP_MAX = 70
CPU_LOAD_MAX = 90
RAM_USED_MAX = 80
HDD_TEMP_MAX = 50
HDD_USED_MAX = 85


def get_normal_value(text):
    value = re.search(r'\s[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?\s', text).group()
    value = ''.join(value.split())
    return int(float(value))


def send_mail(subject, text_mail):
    host = 'smtp.yandex.ru:465'
    to_mail = 'me@defeval.net'
    from_mail = 'me@defeval.net'

    body = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n{}'.format(from_mail, to_mail, subject, text_mail)
    server = smtplib.SMTP_SSL(host)
    server.login(to_mail, 'q16350331')
    server.sendmail(from_mail, to_mail, body)
    server.quit()


while True:
    log_file_list = glob.glob(LOG_PATH + r'\*.txt')
    for log_file in log_file_list:  # для каждого файла

        with open(log_file) as f:  # открываем
            ip = log_file.replace(LOG_PATH + '\\', '')
            ip = ip.replace('.txt', '')
            for line in f:
                if 'CPU Package' in line and 'temperature' in line:  # CPU Temperature in C
                    if get_normal_value(line) > CPU_TEMP_MAX:
                        subject = ip + ': Alert CPU_TEMP'
                        text_mail = 'Alert: CPU_TEMP:', get_normal_value(line), '> CPU_TEMP_MAX:', CPU_TEMP_MAX
                        send_mail(subject, text_mail)
                        print(ip, text_mail)

                if 'CPU Total' in line and 'load' in line:  # CPU load in %
                    if get_normal_value(line) > CPU_LOAD_MAX:
                        subject = ip + ': Alert CPU_LOAD'
                        text_mail = 'Alert: CPU_LOAD:', get_normal_value(line), '> CPU_LOAD_MAX:', CPU_LOAD_MAX
                        send_mail(subject, text_mail)
                        print(ip, text_mail)

                if 'Memory' in line and '/ram/load' in line:  # Memory load in %
                    if get_normal_value(line) > RAM_USED_MAX:
                        subject = ip + ': Alert RAM_USED'
                        text_mail = 'Alert: RAM_USED:', get_normal_value(line), '> RAM_USED_MAX:', RAM_USED_MAX
                        send_mail(subject, text_mail)
                        print(ip, text_mail)

                if 'hdd' in line and 'Temperature' in line:  # HDD Temperature in C
                    if get_normal_value(line) > HDD_TEMP_MAX:
                        subject = ip + ': Alert HDD_TEMP'
                        text_mail = 'Alert: HDD_TEMP:', get_normal_value(line), '> HDD_TEMP_MAX:', HDD_TEMP_MAX
                        send_mail(subject, text_mail)
                        print(ip, text_mail)

                if 'hdd' in line and 'Used Space' in line:  # HDD Used Space in %
                    if get_normal_value(line) > HDD_USED_MAX:
                        subject = ip + ': Alert HDD_USED'
                        text_mail = 'Alert: HDD_USED: ' + str(get_normal_value(line)) + \
                                    ' > HDD_USED_MAX:' + str(HDD_USED_MAX)
                        send_mail(subject, text_mail)
                        print(ip, text_mail)

                elif 'Parameters' in line:
                    break
        os.remove(log_file)

    time.sleep(10)

