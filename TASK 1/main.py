from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty, StringProperty, BooleanProperty
import dbHandler


class ListItem(RecycleDataViewBehavior, BoxLayout):
    text = StringProperty('')
    edited_text = StringProperty('')
    isChecked = BooleanProperty()

    def __init__(self, **kwargs):
        super(ListItem, self).__init__(**kwargs)
        
        self.orientation = 'horizontal'
        # items = ListProperty([])
        
    def on_check(self,id,text):
        # print(id.active)
        # print(text)
        
        dbHandler.modify_data(text,text,id.active)
        
            
    
    def delete_item(self):
        app = MDApp.get_running_app()
        print("Delete ",{"text":f"{self.text}","isChecked":self.isChecked})
        print("Items: ",app.root.items)
        app.root.items.remove({"text":f"{self.text}","isChecked":self.isChecked})
        # app.root.items.remove()
        dbHandler.remove_data(self.text)

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
                print("otext: ",otext['text'],otext['isChecked'])
                if otext['text'] == self.org_text:
                    otext['text'] = self.ids.edit_input.text
                    # if (self.org_text) in app.root.items:
                    # app.root.items.remove(self.org_text)
                    app.root.items.remove({"text":f"{self.org_text}","isChecked":otext['isChecked']})
                    app.root.items.append({"text":f"{self.ids.edit_input.text}","isChecked":otext['isChecked']})
                    dbHandler.modify_data(self.org_text,self.ids.edit_input.text,otext['isChecked'])
                    print("After Rename: ",app.root.ids.rv.data)
                    app.root.ids.rv.data = dbHandler.get_data()
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
        
    def search(self,search_text):
        if(search_text == ""):
            self.ids.rv.data = dbHandler.get_data()
            
        self.data = self.ids.rv.data
        print("Self",self.data)
        if self.isFirst:
            self.const_data = self.data
            self.isFirst = False
        print(self.const_data)
        
        self.filtered_data = [item for item in self.data if search_text in item['text'].lower()]    
        print("Filtered List: ",self.filtered_data)
        self.ids.rv.data = self.filtered_data
        # print(self.ids.rv.data)
        # self.ids.rv.refresh_from_data()
        
        # self.ids.rv.data = self.const_data
        
        
    def OnText(self,v):
        print(v)
        self.search_text = v.lower()
        self.search(self.search_text)

    def on_button_press(self):
        new_item = {"text":f"Item {len(self.items) + 1}","isChecked":False}
        self.items.append(new_item)
        dbHandler.add_data(new_item["text"],new_item["isChecked"])
        self.ids.search.focus = True
        
    def extend_items(self, new_items):
        self.items.extend(new_items)
        
    def on_items(self, instance, value):
        text = []
        isChecked = []
        for i in value:
            text.append(i['text'])
            isChecked.append(i['isChecked'])
        print("On items:" ,text,"\n",isChecked)
        self.ids.rv.data = [{'text': item,"isChecked":isCheck} for item,isCheck in zip(text,isChecked)]
        
        
    def printv(self):
        print(self.items)

class MyApp(MDApp):
    def build(self):
        self.title = "Kivy Demo App"
        return MyBoxLayout()
    
    def on_start(self):
        global value
        
        value = dbHandler.get_data()
        print(value)
        # value = [{"text":"Hello","isChecked":True},{"text":"Bye","isChecked":False}]
        # print(value)
        self.root.extend_items(value)
        return super().on_start()
    
    def on_stop(self):
        print("Stop..")
        MyBoxLayout().printv()
        
        return super().on_stop()


if __name__ == '__main__':
    MyApp().run()
