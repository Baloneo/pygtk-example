import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super(AppWindow, self).__init__(*args, **kwargs)
        self.set_border_width(10)
        # self.set_size_request(150, 100)
        grid = Gtk.Grid.new()
        label1 = Gtk.Label.new("Enter the following information...")
        label2 = Gtk.Label.new("Name:")
        entry = Gtk.Entry.new()
        grid.attach(label1, 0, 0, 2, 1)
        grid.attach(label2, 0, 1, 1, 1)
        grid.attach(entry, 1, 1, 1, 1)
        grid.set_row_spacing(80)
        grid.set_column_spacing(50)
        self.add(grid)


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.xxx.sss", **kwargs)
        self.window = None

    def do_activate(self):
        if self.window is None:
            self.window = AppWindow(title="grid", application=self)
        self.window.show_all()
        self.window.present()


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)
