import tkinter as tk
import requests
import time

def getweather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=dcc8b4f36fea7f8f955315f4a429791e"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main'] #this is done to convert the temp from kelvin to celsius
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp'] - 273.15)
    max_temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data ['wind']['speed']

    final_info = condition = "\n" + str(temp) + "°C"
    final_data = "\n" + "Max temp;" + str(max_temp) + "\n" + "min_temp;" + str(min_temp) + "\n" + "pressure;" + str(pressure) + "\n" + "humidity" + str(humidity) + "\n" + "wind speed" + str(wind)
    label1.config(text = final_info)
    label2.configure(text = final_data)



canvas = tk.Tk()
canvas.geometry('600x500')
canvas.title("weather App")

f = ("poppins", 15, "bold")
t = ("poppins" ,35, "bold")

textfield = tk.Entry(canvas,font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getweather)

label1 = tk.Label(canvas,font = t)
label1.pack()
label2 = tk.Label(canvas,font = f)
label2.pack()
canvas.mainloop()
