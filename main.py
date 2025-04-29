import os
import pickle
from datetime import datetime

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.camera import Camera
from kivy.core.image import Image as CoreImage
from kivy.utils import platform
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore

# Platform-specific storage path
def get_app_storage_path():
    if platform == 'android':
        from android.storage import app_storage_path
        return app_storage_path()
    elif platform == 'ios':
        # iOS-specific storage path (Documents folder)
        return os.path.expanduser('~/Documents')
    else:
        return os.getcwd()

APP_PATH = get_app_storage_path()
os.makedirs(APP_PATH, exist_ok=True)
DB_FILE = os.path.join(APP_PATH, 'user_db.pkl')

user_db = {}
temporary_fingerprint_data = None

class FingerprintApp(App):
    def build(self):
        self.load_user_db()
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.layout.add_widget(Label(text="Fingerprint Authentication System", size_hint=(1, 0.1)))

        self.register_button = Button(text="Register User", size_hint=(1, 0.1))
        self.register_button.bind(on_press=self.register_user)
        self.layout.add_widget(self.register_button)

        self.verify_button = Button(text="Verify Fingerprint", size_hint=(1, 0.1))
        self.verify_button.bind(on_press=self.verify_fingerprint)
        self.layout.add_widget(self.verify_button)

        return self.layout

    def load_user_db(self):
        global user_db
        if os.path.exists(DB_FILE):
            with open(DB_FILE, 'rb') as f:
                user_db = pickle.load(f)

    def save_user_db(self):
        with open(DB_FILE, 'wb') as f:
            pickle.dump(user_db, f)

    def save_user_details(self, name, phone, reg_no, photo_path, fingerprint_data):
        if reg_no in user_db:
            self.show_popup_message("Error", "Fingerprint already registered!")
            return False

        user_db[reg_no] = {
            'name': name,
            'phone': phone,
            'photo': photo_path,
            'fingerprint': fingerprint_data,
            'verified': False,
            'registration_timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.save_user_db()
        self.send_registration_message(name, reg_no, user_db[reg_no]['registration_timestamp'])
        return True

    def send_registration_message(self, name, reg_no, timestamp):
        print(f"[REGISTERED] User {name} with reg no {reg_no} at {timestamp}")

    def capture_fingerprint(self, reg_no):
        # Simulate fingerprint data (replace with real biometric API if available)
        return f"simulated_fingerprint_data_{reg_no}"

    def send_alert_to_admin(self, name, reg_no, time, registration_timestamp=None):
        if registration_timestamp:
            msg = f"[ALERT] Repeat verification by {name} ({reg_no}) at {time}. Registered on {registration_timestamp}"
        else:
            msg = f"[ALERT] Unrecognized fingerprint. Name: {name}, Reg No: {reg_no}, Time: {time}"
        print(msg)
        self.show_popup_message("Admin Alert", msg)

    def check_fingerprint(self, fingerprint_data, reg_no):
        if reg_no not in user_db:
            self.send_alert_to_admin("Unknown", reg_no, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            return False

        if user_db[reg_no]['verified']:
            self.send_alert_to_admin(user_db[reg_no]['name'], reg_no, datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                     user_db[reg_no]['registration_timestamp'])
            return False

        if fingerprint_data == user_db[reg_no]['fingerprint']:
            user_db[reg_no]['verified'] = True
            self.save_user_db()
            return True
        else:
            self.send_alert_to_admin(user_db[reg_no]['name'], reg_no, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            return False

    def open_camera(self, name, callback):
        self.camera_layout = BoxLayout(orientation='vertical')
        self.camera = Camera(play=True)
        self.camera.resolution = (640, 480)
        self.camera_layout.add_widget(self.camera)

        self.capture_button = Button(text="Capture Photo", size_hint=(1, 0.2))
        self.capture_button.bind(on_press=lambda x: self.capture_photo(name, callback))
        self.camera_layout.add_widget(self.capture_button)

        self.camera_popup = Popup(title="Capture Photo", content=self.camera_layout, size_hint=(0.9, 0.9))
        self.camera_popup.open()

    def capture_photo(self, name, callback):
        texture = self.camera.texture
        if texture:
            photo_path = os.path.join(APP_PATH, f"{name}_photo.png")
            image = CoreImage(texture)
            image.save(photo_path)
            self.photo_path = photo_path
            callback()
        else:
            self.show_popup_message("Error", "Failed to capture photo.")
        self.camera.play = False
        self.camera_popup.dismiss()

    def register_user(self, instance):
        self.popup_register = BoxLayout(orientation='vertical', spacing=10)
        self.name_input = TextInput(hint_text="Name", size_hint=(1, None), height=40)
        self.phone_input = TextInput(hint_text="Phone", size_hint=(1, None), height=40)
        self.reg_no_input = TextInput(hint_text="Reg No", size_hint=(1, None), height=40)

        self.popup_register.add_widget(self.name_input)
        self.popup_register.add_widget(self.phone_input)
        self.popup_register.add_widget(self.reg_no_input)

        submit_button = Button(text="Continue", size_hint=(1, None), height=50)
        submit_button.bind(on_press=lambda x: self.capture_and_register())
        self.popup_register.add_widget(submit_button)

        self.popup = Popup(title="Register User", content=self.popup_register, size_hint=(0.8, 0.7))
        self.popup.open()

    def capture_and_register(self):
        name = self.name_input.text
        phone = self.phone_input.text
        reg_no = self.reg_no_input.text

        if reg_no in user_db:
            self.show_popup_message("Error", "This registration number already exists.")
            return

        self.popup.dismiss()

        def after_photo():
            fingerprint_data = self.capture_fingerprint(reg_no)
            if self.save_user_details(name, phone, reg_no, self.photo_path, fingerprint_data):
                self.show_popup_message("Success", f"{name} registered successfully.")

        self.open_camera(name, after_photo)

    def verify_fingerprint(self, instance):
        self.popup_verify = BoxLayout(orientation='vertical', spacing=10)
        self.reg_no_verify_input = TextInput(hint_text="Enter registration number", size_hint=(1, None), height=40)
        self.popup_verify.add_widget(self.reg_no_verify_input)

        verify_btn = Button(text="Verify", size_hint=(1, None), height=50)
        verify_btn.bind(on_press=self.perform_fingerprint_verification)
        self.popup_verify.add_widget(verify_btn)

        self.popup = Popup(title="Verify Fingerprint", content=self.popup_verify, size_hint=(0.8, 0.6))
        self.popup.open()

    def perform_fingerprint_verification(self, instance):
        reg_no = self.reg_no_verify_input.text
        fingerprint_data = self.capture_fingerprint(reg_no)
        if self.check_fingerprint(fingerprint_data, reg_no):
            self.show_popup_message("Access Granted", "Fingerprint verified successfully!")
        else:
            self.show_popup_message("Access Denied", "Fingerprint verification failed.")

    def show_popup_message(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10)
        layout.add_widget(Label(text=message))
        close_btn = Button(text="Close", size_hint=(1, None), height=50)
        close_btn.bind(on_press=lambda x: self.popup.dismiss())
        layout.add_widget(close_btn)
        self.popup = Popup(title=title, content=layout, size_hint=(0.7, 0.3))
        self.popup.open()

if __name__ == '__main__':
    FingerprintApp().run()
