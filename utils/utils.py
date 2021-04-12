from datetime import datetime


def get_datetime_str():
    return datetime.now().strftime("%d-%m-%Y_%H-%M-%S")


def get_datetime_now():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

