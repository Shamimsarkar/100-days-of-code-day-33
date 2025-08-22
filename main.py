# # from tkinter import *
# import requests
# from datetime import datetime
#
# my_lat = 49.4737056
# my_lag = 11.112419
#
# # def get_quote():
# #     response = requests.get("https://api.kanye.rest")
# #     response.raise_for_status()
# #     data = response.json()
# #     quote = data["quote"]
# #     canvas.itemconfig(quote_text, text=quote)
# #
# # window = Tk()
# # window.title("Kanye")
# # window.config(padx=50, pady=50)
# #
# # canvas = Canvas(width=300, height=414)
# # background_image = PhotoImage(file="background.png")
# # canvas.create_image(150, 207, image=background_image)
# # quote_text = canvas.create_text(150, 207, text="", width=200, font=("Arial", 15, "bold"), fill="black")
# # canvas.grid(row=0, column=0)
# #
# # kanya_image = PhotoImage(file="kanye.png")
# # button = Button(image=kanya_image, command=get_quote)
# # button.grid(row=1, column=0)
# #
# # window.mainloop()
#
# parameter ={
#     "lat": my_lat,
#     "lng": my_lag,
#     "formatted": 0
# }
#
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
# response.raise_for_status()
#
# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
#
# print(sunrise, sunset)
#
# time_now = datetime.now()
# print(time_now.hour)

import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 49.4737056 # Your latitude
MY_LONG = 11.112419 # Your longitude

my_email = "rezamdshamim034@gmail.com"
my_password = "odli hfeg oopt ejzl"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_it_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(60)
    if is_it_dark() and is_iss_overhead():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="sinthya.wedding@gmail.com",
            msg="weak up my girl"
        )



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



