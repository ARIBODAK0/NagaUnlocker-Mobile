from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import os
import subprocess

class NagaUnlocker(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        self.root.add_widget(Label(text="NAGA UNLOCKER MOBILE v1.0", font_size='20sp', size_hint_y=None, height=50))
        
        # Area Log
        self.log_area = Label(text="Status: Ready", size_hint_y=None, height=200, halign="left", valign="top")
        scroll = ScrollView(size_hint=(1, None), height=200)
        scroll.add_widget(self.log_area)
        self.root.add_widget(scroll)

        # Tombol-Tombol
        btns = [
            ("BYPASS FRP (MTK - Tecno/Itel/Infinix)", "python3 mtk e frp"),
            ("FACTORY RESET (MTK - Oppo/Vivo/Xiaomi)", "python3 mtk e userdata"),
            ("BYPASS MI CLOUD (Xiaomi/Poco)", "python3 mtk e persist"),
            ("SAMSUNG FRP BYPASS (MTP Mode)", "adb shell am start -n com.sec.android.app.modemui/.PST"),
            ("QUALCOMM EDL ERASE FRP", "python3 edl e frp")
        ]

        for text, cmd in btns:
            btn = Button(text=text, size_hint_y=None, height=60)
            btn.bind(on_press=lambda instance, c=cmd: self.jalankan_perintah(c))
            self.root.add_widget(btn)

        return self.root

    def jalankan_perintah(self, command):
        self.log_area.text = f"Executing: {command}..."
        try:
            # Menjalankan perintah lewat shell android (butuh ROOT di HP Poco F1 Abang)
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            self.log_area.text = f"Result:\n{result.stdout}\n{result.stderr}"
        except Exception as e:
            self.log_area.text = f"Error: {str(e)}"

if __name__ == '__main__':
    NagaUnlocker().run()
          
