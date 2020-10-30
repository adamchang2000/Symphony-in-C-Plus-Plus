import sublime
import sublime_plugin

class UpdateOnSave(sublime_plugin.EventListener):

    actions = {'insert': 0, 'left_delete': 0 , 'undo': 0, 'redo_or_repeat': 0, 'paste': 0 ,'insert_best_completion': 0}
 
    def on_text_command(self, view, command_name, args):
        if command_name in self.actions.keys():
            #print(command_name, args)
            pass
        print(command_name, args)

class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")
