from datetime import datetime


def days_left(date_text):

    exam_date = datetime.strptime(
        date_text, "%d-%m-%Y"
    )

    today = datetime.today()

    difference = exam_date - today

    return difference.days
