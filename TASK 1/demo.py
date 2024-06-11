from kivy.properties import ListProperty, StringProperty

class demo:
    l = ListProperty(["Hello"])

    # l.append("Hello")

    def on_items(instance,value):
        print(value)
        
    l.append("Hi")