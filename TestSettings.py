import sublime, sublime_plugin
import os

PluginName = 'TestSettings'

class Prefs:
    @staticmethod
    def load():
        settings = sublime.load_settings(PluginName + '.sublime-settings')
        Prefs.var = settings.get('var', "None")
        print 'TestSettings var : ' + Prefs.var

if int(sublime.version()) < 3000:
    Prefs.load()


# sublime.run_command("test")
# view.settings().get('TestSettings').get('var', "None")
class TestCommand(sublime_plugin.ApplicationCommand):
    def run(self, **kwargs):
        print 'TestSettings var : ' + Prefs.var
