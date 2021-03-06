from dateutil import parser
from datetime import datetime


def create_moment(db_obj):
    # get current time, database object time, get the difference in minutes
    now_datetime = datetime.now()
    item_datetime = parser.parse(db_obj.dt)
    obj_time = item_datetime.strftime("%-I:%M")
    obj_day = item_datetime.strftime("%x")
    minutes_diff = (now_datetime - item_datetime).total_seconds() / 60.0

    if minutes_diff > 0:
        # if the time difference is less than 5 minutes
        if minutes_diff < 5.0:
            db_obj.moment = "Just now"

        # if the time difference is less than 1 hour
        elif minutes_diff < 60.0:
            minutes_diff = round(minutes_diff)
            db_obj.moment = f"{minutes_diff} minutes ago"

        # if the time difference is less than 1 day
        elif minutes_diff < 1440.0:
            minutes_diff = round(minutes_diff / 60.0)
            if minutes_diff == 1:
                hour = "hour"
            else:
                hour = "hours"
            db_obj.moment = f"{minutes_diff} {hour} ago"

        # if the time difference is less than 1 week
        elif minutes_diff < 10080.0:
            day = item_datetime.strftime("%a")
            db_obj.moment = f"{day} at {obj_time}"

        # if the time difference is less than 1 year
        elif minutes_diff < 525600.0:
            day = item_datetime.strftime("%-m/%-d")
            db_obj.moment = f"{day} at {obj_time}"

        # if the time difference is more than 1 year
        else:
            db_obj.moment = f"{obj_day} at {obj_time}"
    else:
        # if the time difference is less than 5 minutes in the future
        if minutes_diff > -5.0:
            db_obj.moment = "Now"

        # if the time difference is less than 1 hour
        elif minutes_diff > -60.0:
            minutes_diff = round(abs(minutes_diff))
            db_obj.moment = f"in {abs(minutes_diff)} minutes"

        # if the time difference is less than 1 day in the future
        elif minutes_diff > -1440.0:
            minutes_diff = round(abs(minutes_diff) / 60.0)
            if minutes_diff == 1:
                hour = "hour"
            else:
                hour = "hours"
            db_obj.moment = f"in {abs(minutes_diff)} {hour}"

        # if the time difference is less than 1 week in the future
        elif minutes_diff > -10080.0:
            day = item_datetime.strftime("%a")
            db_obj.moment = f"{day} at {obj_time}"

        # if the time difference is less than 1 year in the future
        elif minutes_diff > -525600.0:
            day = item_datetime.strftime("%-m/%-d")
            db_obj.moment = f"{day} at {obj_time}"

        # if the time difference is more than 1 year in the future
        else:
            db_obj.moment = f"{obj_day} at {obj_time}"

    return db_obj
