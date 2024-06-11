from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty, StringProperty



class ListItem(RecycleDataViewBehavior, BoxLayout):
    text = StringProperty('')
    edited_text = StringProperty('')

    def __init__(self, **kwargs):
        super(ListItem, self).__init__(**kwargs)
        
        self.orientation = 'horizontal'
        # items = ListProperty([])
        

    def delete_item(self):
        app = MDApp.get_running_app()
        app.root.items.remove(self.text)

    org_text = ""
    def edit_item(self):
        print("Original : ",self.org_text)
        if self.ids.edit.text == "Edit":
            self.org_text = self.ids.edit_input.text
            
            self.ids.edit_input.focus = True
            self.ids.edit_input.readonly = False
            self.ids.edit.text = "Save"
        else:
            # MyBoxLayout().rename(self.org_text,self.ids.edit_input.text)
            app = MDApp.get_running_app()
            print(app.root.ids.rv.data)
            for otext in app.root.ids.rv.data:
                print("otext: ",otext)
                if otext['text'] == self.org_text:
                    otext['text'] = self.ids.edit_input.text
                    if (self.org_text) in app.root.items:
                        app.root.items.remove(self.org_text)
                        app.root.items.append(self.ids.edit_input.text)
                    print("After Rename: ",app.root.ids.rv.data)
            app.root.ids.rv.refresh_from_data()
            self.ids.edit_input.readonly = True
            self.ids.edit.text = "Edit"
            

    def hi():
        print("hello")

class MyBoxLayout(BoxLayout):
    global value
    items = ListProperty([])
    
    const_data = []
    isFirst = True
    
    def rename(self,org_text,new_text):
        print("new",new_text)
        print("org",org_text)
        
                
    
    def search(self,search_text):
        
        self.data = self.ids.rv.data
        print("Self",self.data)
        if self.isFirst:
            self.const_data = self.data
            self.isFirst = False
        print(self.const_data)
        
        self.filtered_data = [item for item in self.const_data if search_text in item['text'].lower()]    
        print("Filtered List: ",self.filtered_data)
        self.ids.rv.data = self.filtered_data
        print(self.ids.rv.data)
        self.ids.rv.refresh_from_data()
        
    def OnText(self,v):
        print(v)
        self.search_text = v.lower()
        self.search(self.search_text)
        # rv = self.ids?.rv
        # MyRecycleView().filter_items(self.search_text)
        
    def on_button_press(self):
        new_item = f"Item {len(self.items) + 1}"
        self.items.append(new_item)
        self.ids.search.focus = True
        
    def extend_items(self, new_items):
        self.items.extend(new_items)
        
    def on_items(self, instance, value):
        self.ids.rv.data = [{'text': item} for item in value]
        
        
    def printv(self):
        print(self.items)

class MyApp(MDApp):
    def build(self):
        self.title = "Kivy Demo App"
        
        
        return MyBoxLayout()
    
    def on_start(self):
        global value
        value = ["L1","L2","L3"]
        self.root.ids.rv.data = [{'text': item} for item in value]
        self.root.extend_items(value)
        return super().on_start()
    
    def on_stop(self):
        print("Stop..")
        MyBoxLayout().printv()
        
        return super().on_stop()


if __name__ == '__main__':
    MyApp().run()
