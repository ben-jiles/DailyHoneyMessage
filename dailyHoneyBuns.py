from fbchat import Client
from fbchat.models import *
import datetime
import time
import random
from twilio.rest import Client as MyTwilioClient

# FaceBook Chat info

fb_client = Client('use your facebook email address', 'facebook password')
thread_id = 'id for thread. open chat in facebook and look for /t/<chat id>'
thread_type = ThreadType.USER  # can use ThreadType.GROUP for a group chat

# Twilio account info

account_sid = 'twilio account SID'
auth_token = 'twilio authentication token'
twilio_client = MyTwilioClient(account_sid, auth_token)
my_twilio_number = 'your twilio phone number'
my_cell_number = 'your cell phone number'


def day_and_time():
    today_var = datetime.datetime.now().strftime('%A')
    if today_var == 'Monday' or 'Tuesday' or 'Thursday' or 'Friday':
        right_now_time = datetime.datetime.now().strftime('%H:%M')
        if right_now_time == '07:15':
            daily_message()
        else:
            time.sleep(60)
            day_and_time()


def daily_message():
    fb_client.send(Message(msg_generator()), thread_id=thread_id, thread_type=thread_type)


def msg_generator():
    msg_index = random.randint(0, 5)
    if msg_index == 1:
        return 'Good morning honey buns!!)))'
    elif msg_index == 2:
        return 'Hey Honey! Good morning! Hope work is good :)'
    elif msg_index == 3:
        return 'Good morning my love)) I miss you!!!'
    elif msg_index == 4:
        return 'honey buns love you! and good morning)'
    elif msg_index == 5:
        return 'Good morning beautiful :))))'
    else:
        twilio_client.messages.create(to=my_cell_number, from_=my_twilio_number, body='Your daily message to your honey buns did not send due to an error Please text her soon.')
        time.sleep(60)
        day_and_time()


day_and_time()
