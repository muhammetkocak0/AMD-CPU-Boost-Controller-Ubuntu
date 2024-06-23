import gi
import os

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

class Indicator:
    def __init__(self):
        self.app = 'test_indicator'
        # Relative path to the custom icon
        rel_icon_path = "amd_icon.png"
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Directory where the script is located
        icon_path = os.path.join(base_dir, rel_icon_path)
        
        # Fallback to a default icon if the specified one doesn't exist
        if not os.path.exists(icon_path):
            icon_path = os.path.join(base_dir, 'default_icon.png')
        
        self.indicator = AppIndicator3.Indicator.new(
            self.app, icon_path,
            AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.menu = self.build_menu()
        self.indicator.set_menu(self.menu)
        self.update_menu_item()

    def build_menu(self):
        menu = Gtk.Menu()

        # Create a toggle menu item with dynamic labeling based on current boost state
        self.item_toggle = Gtk.MenuItem(label='Checking Boost...')
        self.item_toggle.connect('activate', self.toggle_turbo_boost)
        menu.append(self.item_toggle)

        # Create and append the quit menu item
        item_quit = Gtk.MenuItem(label='Quit')
        item_quit.connect('activate', self.quit)
        menu.append(item_quit)

        menu.show_all()
        return menu

    def toggle_turbo_boost(self, source):
        current_state = self.get_current_boost_state()
        new_state = '0' if current_state == '1' else '1'
        try:
            # Write the new boost state directly to the system file
            with open('/sys/devices/system/cpu/cpufreq/boost', 'w') as file:
                file.write(new_state)
            # Update the system setting using echo and sudo tee for higher permission actions
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

    def update_menu_item(self):
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
