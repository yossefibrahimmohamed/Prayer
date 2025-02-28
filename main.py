import subprocess
import sys
import customtkinter as ctk
from PIL import Image
import pygame
import time
import os
from pygame import mixer
from functools import partial

class ExitApp:
    @staticmethod
    def exit():
        root.destroy()  # Destroy root to ensure full exit
        sys.exit()  # Force exit the entire application

class click_sound:
    @staticmethod
    def play_click_sound():
        pygame.mixer.init()
        click_sound = pygame.mixer.Sound(
            'D:\\My Projects\\Pycharm\\Prayer_By_Yossef_ibrahim\\Data\\sound\\sound_track1.wav')
        click_sound.play()

# Load background image
root = ctk.CTk()
root.geometry("700x700")
root.title("Prayer By Yossef Ibrahim")


# Class to Exit_App
background_img_path = "D:\\My Projects\\Pycharm\\Prayer_By_Yossef_ibrahim\\Data\\img\\bg.png"
background_img = Image.open(background_img_path)
img = ctk.CTkImage(light_image=background_img, dark_image=background_img, size=(700, 700))

background_label = ctk.CTkLabel(root, image=img)
background_label.place(relx=0.5, rely=0.5, anchor='center')

# Function to play click sound


# Function to generate prayer times
def generate_time_list():
    time_list = []
    for hour in range(1, 13):  # 1:00 AM - 11:45 AM
        for minute in range(0, 60, 15):
            time_list.append(f"{hour:02d}:{minute:02d} AM")
    for hour in range(12, 24):  # 12:00 PM - 11:45 PM
        display_hour = hour if hour <= 12 else hour - 12
        for minute in range(0, 60, 15):
            time_list.append(f"{display_hour:02d}:{minute:02d} PM")
    return time_list

# Function to open Prayer window
def open_prayer_window():

    click_sound.play_click_sound()
    root.withdraw()  # Hide the main page

    # Create a new Prayer window
    prayer_window = ctk.CTkToplevel(root)
    prayer_window.geometry("700x700")
    prayer_window.title("Prayer Times")
    prayer_window.protocol("WM_DELETE_WINDOW", ExitApp.exit)
    # Load Prayer window background
    prayer_img_path = "D:\\My Projects\\Pycharm\\Prayer_By_Yossef_ibrahim\\Data\\img\\Prayer Time.png"
    prayer_img = Image.open(prayer_img_path)
    img2 = ctk.CTkImage(light_image=prayer_img, dark_image=prayer_img, size=(700, 700))

    ctk.CTkLabel(prayer_window, image=img2).place(relx=0.5, rely=0.5, anchor='center')

    # Function to update live time
    def update_time():
        current_time = time.strftime('%I:%M %p')
        time_label.configure(text=current_time)
        prayer_window.after(1000, update_time)  # Update every second

    # Function to go back to the main window (No Temporary Screen)
    def get_back():
        click_sound.play_click_sound()
        prayer_window.destroy()  # Close the Prayer window
        root.deiconify()  # Show the main page instantly (No delay, No black screen)

    # Function for the Save Button
    def save_fun():
        click_sound.play_click_sound()
        print("Saving Prayer Times...")  # Replace with actual saving logic

    # Live time label
    time_label = ctk.CTkLabel(prayer_window, font=ctk.CTkFont('calibri', 40, 'bold'), fg_color='black', text_color='white', corner_radius=5, bg_color='white', width=50)
    time_label.place(relx=0.08, rely=0.1)
    update_time()

    # Prayer time dropdowns
    times = ["الفجر توقيت", "الظهر توقيت", "العصر توقيت", "المغرب توقيت", "العشاء توقيت"]
    positions = [0.175, 0.275, 0.375, 0.475, 0.575]

    for i in range(5):
        combo = ctk.CTkComboBox(prayer_window, values=generate_time_list(), width=150, height=20, border_width=2, corner_radius=10)
        combo.set(times[i])
        combo.place(relx=0.4, rely=positions[i])

    # Back Button (No Temporary Screen)
    back_button = ctk.CTkButton(
        prayer_window, text="العوده", font=ctk.CTkFont("bold", 20),
        height=40, width=120, corner_radius=10, fg_color="transparent",
        text_color="white", hover_color="gray", border_color="white",
        border_width=2, command=get_back
    )
    back_button.place(relx=0.2, rely=0.9, anchor='se')

    # Save Button (حفظ)
    save_button = ctk.CTkButton(
        prayer_window, text="حفظ", font=ctk.CTkFont("bold", 20),
        height=40, width=120, corner_radius=10, fg_color="transparent",
        text_color="white", hover_color="gray", border_color="white",
        border_width=2, cursor='hand2', command=save_fun
    )
    save_button.place(relx=0.58, rely=0.75, anchor='se')


def Quran_button_fun():

    def back_button_fun():
        mixer.music.stop()  # Stop any playing audio
        click_sound.play_click_sound()
        window_quran.withdraw()  # Hide the Quran window
        root.deiconify()  # Show the main root window again

    root.withdraw()
    click_sound.play_click_sound()
    window_quran = ctk.CTkToplevel()
    window_quran.geometry("700x700")
    window_quran.title("القرآن الكريم")
    window_quran.protocol("WM_DELETE_WINDOW", ExitApp.exit)

    img_path = "D:/My Projects/Pycharm/Prayer_By_Yossef_ibrahim/Data/img/bg_quran2.png"
    img = Image.open(img_path)
    display = ctk.CTkImage(light_image=img, dark_image=img, size=(700, 700))
    ctk.CTkLabel(window_quran, image=display).place(relx=0.5, rely=0.5, anchor='center')

    surah_numbers = {
        "الفاتحة": "001", "البقرة": "002", "آل عمران": "003", "النساء": "004", "المائدة": "005",
        "الأنعام": "006", "الأعراف": "007", "الأنفال": "008", "التوبة": "009", "يونس": "010",
        "هود": "011", "يوسف": "012", "الرعد": "013", "إبراهيم": "014", "الحجر": "015",
        "النحل": "016", "الإسراء": "017", "الكهف": "018", "مريم": "019", "طه": "020",
        "الأنبياء": "021", "الحج": "022", "المؤمنون": "023", "النور": "024", "الفرقان": "025",
        "الشعراء": "026", "النمل": "027", "القصص": "028", "العنكبوت": "029", "الروم": "030",
        "لقمان": "031", "السجدة": "032", "الأحزاب": "033", "سبأ": "034", "فاطر": "035",
        "يس": "036", "الصافات": "037", "ص": "038", "الزمر": "039", "غافر": "040",
        "فصلت": "041", "الشورى": "042", "الزخرف": "043", "الدخان": "044", "الجاثية": "045",
        "الأحقاف": "046", "محمد": "047", "الفتح": "048", "الحجرات": "049", "ق": "050",
        "الذاريات": "051", "الطور": "052", "النجم": "053", "القمر": "054", "الرحمن": "055",
        "الواقعة": "056", "الحديد": "057", "المجادلة": "058", "الحشر": "059", "الممتحنة": "060",
        "الصف": "061", "الجمعة": "062", "المنافقون": "063", "التغابن": "064", "الطلاق": "065",
        "التحريم": "066", "الملك": "067", "القلم": "068", "الحاقة": "069", "المعارج": "070",
        "نوح": "071", "الجن": "072", "المزمل": "073", "المدثر": "074", "القيامة": "075",
        "الإنسان": "076", "المرسلات": "077", "النبأ": "078", "النازعات": "079", "عبس": "080",
        "التكوير": "081", "الانفطار": "082", "المطففين": "083", "الانشقاق": "084", "البروج": "085",
        "الطارق": "086", "الأعلى": "087", "الغاشية": "088", "الفجر": "089", "البلد": "090",
        "الشمس": "091", "الليل": "092", "الضحى": "093", "الشرح": "094", "التين": "095",
        "العلق": "096", "القدر": "097", "البينة": "098", "الزلزلة": "099", "العاديات": "100",
        "القارعة": "101", "التكاثر": "102", "العصر": "103", "الهمزة": "104", "الفيل": "105",
        "قريش": "106", "الماعون": "107", "الكوثر": "108", "الكافرون": "109", "النصر": "110",
        "المسد": "111", "الإخلاص": "112", "الفلق": "113", "الناس": "114"
    }  # Example

    current_playing = None
    is_paused = False

    chosen_label = ctk.CTkLabel(window_quran, text="لا يوجد تشغيل حالي", font=("Arial", 18), fg_color="black",
                                text_color="white")
    chosen_label.place(relx=0.5, rely=0.2, anchor='center')

    def play_quran_audio(surah_name, button):
        nonlocal current_playing, is_paused
        if surah_name in surah_numbers:
            audio_path = f"D:/My Projects/Pycharm/Prayer_By_Yossef_ibrahim/Data/audio/{surah_numbers[surah_name]}.dat"
            if os.path.exists(audio_path):
                mixer.init()
                mixer.music.stop()
                mixer.music.load(audio_path)
                mixer.music.play()
                is_paused = False
                chosen_label.configure(text=f"تشغيل: {surah_name}")
                if current_playing:
                    current_playing.configure(fg_color="gray")
                button.configure(fg_color="green")
                current_playing = button
            else:
                print(f"❌ الملف غير موجود: {audio_path}")
        else:
            print(f"❌ السورة غير موجودة")

    frame = ctk.CTkScrollableFrame(window_quran, width=300, height=500)
    frame.place(relx=0.5, rely=0.6, anchor='center')
    for surah in surah_numbers:
        btn = ctk.CTkButton(frame, text=surah, font=ctk.CTkFont(size=16))
        btn.configure(command=partial(play_quran_audio, surah, btn))  # Correct capturing
        btn.pack(pady=5, padx=10, fill='x')

    button_back = ctk.CTkButton(window_quran, text="الرجوع", font=ctk.CTkFont("bold", 20), height=40, width=120,
                                corner_radius=10, fg_color="transparent", text_color="white", hover_color="gray",
                                border_color="white", border_width=2, cursor="hand2", command=back_button_fun)
    button_back.place(relx=0.2, rely=0.93, anchor='se')

Quran_button = ctk.CTkButton(
    root, text="القرآن الكريم", font=ctk.CTkFont("bold", 20),
    height=70, width=120, corner_radius=10, fg_color="transparent",
    text_color="white", hover_color="gray", border_color="white",
    border_width=2, cursor='hand2', command=Quran_button_fun
)
Quran_button.place(relx=0.3, rely=0.5, anchor='center')

# Prayer Times Button
Prayer_button = ctk.CTkButton(
    root, text="توقيت الاذان", font=ctk.CTkFont("bold", 20),
    height=70, width=120, corner_radius=10, fg_color="transparent",
    text_color="white", hover_color="gray", border_color="white",
    border_width=2, cursor='hand2', command=open_prayer_window
)

Prayer_button.place(relx=0.7, rely=0.5, anchor='center')
root.protocol("WM_DELETE_WINDOW", ExitApp.exit)
# Start the main loop
root.mainloop()
