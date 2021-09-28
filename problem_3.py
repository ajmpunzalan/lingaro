# Write function that returns datetime.date object from given string ('YY-MM-DD'). Do it 'pythonic way'.
from datetime import datetime

LIST_DATE_FORMATS = ['%Y-%m-%d', '%y-%m-%d']


def get_date(stringlike_date):
    """
    Return datetime.date object from given stringlike_date :param stringlike_date
    :return date object
    """
    for date_format in LIST_DATE_FORMATS:
        try:
            date = datetime.strptime(stringlike_date, date_format).date()
            return date
        except ValueError:
            pass
        except TypeError:
            pass
    raise ValueError(
        'Invalid date format. Please use - {}'.format(LIST_DATE_FORMATS))
