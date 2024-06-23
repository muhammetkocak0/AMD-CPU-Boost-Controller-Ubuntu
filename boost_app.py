import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3
import os

class Indicator:
    def __init__(self):
        self.app = 'test_indicator'
        # Path to the custom icon
        icon_path = "/home/prodigytrip/Downloads/amd_icon.png"
        self.indicator = AppIndicator3.Indicator.new(
            self.app, icon_path,
            AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.menu = self.build_menu()
        self.indicator.set_menu(self.menu)
        self.update_menu_item()

    def build_menu(self):
        menu = Gtk.Menu()

        # Create a toggle menu item with a placeholder label
        self.item_toggle = Gtk.MenuItem(label='Checking Boost...')
        self.item_toggle.connect('activate', self.toggle_turbo_boost)
        menu.append(self.item_toggle)

        item_quit = Gtk.MenuItem(label='Quit')
        item_quit.connect('activate', self.quit)
        menu.append(item_quit)

        menu.show_all()
        return menu

    def toggle_turbo_boost(self, source):
        current_state = self.get_current_boost_state()
        new_state = '0' if current_state == '1' else '1'
        try:
            with open('/sys/devices/system/cpu/cpufreq/boost', 'w') as file:
                file.write(new_state)
            os.system(f'echo "{new_state}" | sudo tee /sys/devices/system/cpu/cpufreq/boost')
        except Exception as e:
            self.item_toggle.set_label(f"Failed to toggle: {str(e)}")
        self.update_menu_item()

    def get_current_boost_state(self):
        try:
            with open('/sys/devices/system/cpu/cpufreq/boost', 'r') as file:
                return file.read().strip()
        except Exception:
            return None

    def update_menu_item(self, *args):
        current_state = self.get_current_boost_state()
        if current_state == '1':
            self.item_toggle.set_label("Disable Boost")
        else:
            self.item_toggle.set_label("Enable Boost")

    def quit(self, source):
        Gtk.main_quit()

def main():
    app = Indicator()
    Gtk.main()

if __name__ == "__main__":
    main()
