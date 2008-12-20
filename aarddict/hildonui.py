"""
This file is part of AardDict (http://code.google.com/p/aarddict) - 
a dictionary for Nokia Internet Tablets. 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Copyright (C) 2006-2008 Igor Tkach
"""

import osso, hildon, ui
import webbrowser, gtk

osso_c = osso.Context("aarddict", ui.version, False)

import articleformat
#hack, normal way of determining char width for some reason yields incorrect
#result
articleformat.CHAR_WIDTH = 13

class HildonDictViewer(ui.DictViewer):
            
    def create_top_level_widget(self):
        app = hildon.Program()        
        window = hildon.Window()
        try:
            #This function has been omited twice already during significant 
            #Pymaemo updates - hence try/except
            gtk.set_application_name(ui.app_name)
        except:
            print 'Failed to set application name'
        window.connect("key-press-event", self.on_key_press)
        app.add_window(window)        
        window.connect("event", self.window_event)
        return window
    
    def update_title(self):
        self.window.set_title(self.create_dict_title())
    
    def on_key_press(self, widget, event, *args):
        if event.keyval == gtk.keysyms.F6:
            # The "Full screen" hardware key has been pressed
            self.toggle_full_screen(self.actiongroup.get_action('FullScreen'))
        else:
            ui.DictViewer.on_key_press(self, widget, event, *args)
    
    def add_menu(self, content_box):        
        main_menu =  gtk.Menu()
        self.window.set_menu(main_menu)                
        for menu in self.create_menus():
            main_menu.append(menu)
        main_menu.show_all()
    
    def create_menus(self):           
        return (self.mi_open, 
                self.mn_remove_item, 
                self.mi_info, 
                self.mn_copy_item, 
                self.mi_select_phonetic_font, 
                self.mi_drag_selects, 
                self.mi_show_word_list,
                self.mi_back,
                self.mi_forward,
                self.mi_about, 
                self.mi_exit)
    
    def create_file_chooser_dlg(self):
        return hildon.FileChooserDialog(self.window, 
                                        gtk.FILE_CHOOSER_ACTION_OPEN);  
    
    def open_external_link(self, url):
        webbrowser.open(url, context = osso_c)
        
#    def supports_cursor_changes(self):
#        return False         
        
