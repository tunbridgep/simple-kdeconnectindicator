from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import signal
import subprocess

APPINDICATOR_ID = 'myappindicator'

def build_menu():
    menu = gtk.Menu()

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    item_sms = gtk.MenuItem('Send SMS')
    item_sms.connect('activate', send_sms)
    item_url = gtk.MenuItem('Send URL')
    item_url.connect('activate', send_url)
    item_app = gtk.MenuItem('Open App')
    item_app.connect('activate', open_app)
    item_settings = gtk.MenuItem('Settings')
    item_settings.connect('activate', settings)

    menu.append(item_app)
    menu.append(gtk.SeparatorMenuItem())
    menu.append(item_sms)
    menu.append(item_url)
    menu.append(gtk.SeparatorMenuItem())
    menu.append(item_settings)
    menu.append(item_quit)
    menu.show_all()
    return menu
 
def quit(source):
    gtk.main_quit()

def send_sms(source):
    subprocess.run('kdeconnect-sms')

def send_url(source):
    subprocess.run('kdeconnect-handler')

def settings(source):
    subprocess.run('kdeconnect-settings')

def open_app(source):
    subprocess.run('kdeconnect-app')

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, 'whatever', appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gtk.main()

if __name__ == "__main__":
    main()
