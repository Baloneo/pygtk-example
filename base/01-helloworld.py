import gi
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = Gtk.Label.new("Hello World!")
        x, y = label.get_alignment()
        print(x, y)
        self.add(label)
        self.set_size_request(200, 100)


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp", **kwargs)  # 如果再次运行会查找此程序 存在这个id就只是再展现
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Main Window")
        self.window.show_all()
        self.window.present()


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)