import tkinter as tk
from tkinter import messagebox, PhotoImage
import requests
from PIL import Image, ImageTk
import time

# get api token from .env file
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")  # WeatherAPI.com API kalitini kiriting
BASE_URL = "http://api.weatherapi.com/v1/current.json"

if not API_KEY:
    messagebox.showerror("Xatolik", "Iltimos, .env faylida WEATHER_API_KEY ni kiriting!")
    exit(0)

# Ranglar va fonlar ob-havo holatiga qarab o'zgaradi
def get_background_color(condition):
    condition = condition.lower()
    if "clear" in condition or "sunny" in condition:
        return "#FFD700", "#FFA500"  # Quyoshli kun
    elif "rain" in condition or "drizzle" in condition:
        return "#3B5998", "#1C1C1C"  # Yomg'ir
    elif "snow" in condition:
        return "#E0E0E0", "#B0C4DE"  # Qor
    elif "cloud" in condition or "overcast" in condition:
        return "#A9A9A9", "#696969"  # Bulutli
    else:
        return "#282c34", "#1C1C1C"  # Default

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Xatolik", "Iltimos, shahar nomini kiriting!")
        return
    
    params = {"key": API_KEY, "q": city, "aqi": "no"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['current']['condition']['text']
        temp = data['current']['temp_c']
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_kph']
        icon_url = "http:" + data['current']['condition']['icon']
        
        update_weather_info(weather_desc, temp, humidity, wind_speed, icon_url)
    else:
        messagebox.showerror("Xatolik", "Shahar topilmadi yoki API xatosi yuz berdi!")

def update_weather_info(weather_desc, temp, humidity, wind_speed, icon_url):
    bg_color, frame_color = get_background_color(weather_desc)
    root.configure(bg=bg_color)
    frame.configure(bg=frame_color)
    header_label.config(bg=frame_color, fg="white")
    result_label.config(bg=frame_color, fg="white")
    
    result_label.config(text=f"Havo: {weather_desc}\nHarorat: {temp}°C\nNamlik: {humidity}%\nShamol tezligi: {wind_speed} km/soat")
    
    icon_image = Image.open(requests.get(icon_url, stream=True).raw)
    icon_image = icon_image.resize((100, 100), Image.ANTIALIAS)
    icon_tk = ImageTk.PhotoImage(icon_image)
    icon_label.config(image=icon_tk, bg=frame_color)
    icon_label.image = icon_tk
    
    animate_button()

def animate_button():
    for i in range(3):
        get_weather_btn.config(bg="#ffcc00")
        root.update()
        time.sleep(0.2)
        get_weather_btn.config(bg="#61afef")
        root.update()
        time.sleep(0.2)

# GUI yaratish
root = tk.Tk()
root.title("Ob-havo Ma'lumotlari")
root.geometry("500x500")
root.configure(bg="#282c34")

# Asosiy ramka
frame = tk.Frame(root, bg="#1C1C1C", bd=2, relief=tk.RIDGE)
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Sarlavha
header_label = tk.Label(frame, text="Ob-havo Ma'lumotlari", font=("Arial", 18, "bold"), bg="#1C1C1C", fg="white")
header_label.pack(pady=10)

# Shahar nomini kiritish
city_entry = tk.Entry(frame, font=("Arial", 14), width=20, justify='center')
city_entry.pack(pady=5)

# Ma'lumot olish tugmasi
get_weather_btn = tk.Button(frame, text="Ob-havo ma'lumotini olish", font=("Arial", 12), command=get_weather, bg="#61afef", fg="white", relief=tk.RAISED)
get_weather_btn.pack(pady=10)

# Ob-havo ikonkasi
icon_label = tk.Label(frame, bg="#1C1C1C")
icon_label.pack()

# Natija chiqarish
result_label = tk.Label(frame, text="", font=("Arial", 14), bg="#1C1C1C", fg="white")
result_label.pack(pady=10)

root.mainloop()
