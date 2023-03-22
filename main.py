from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


from kivy.core.window import Window

Window.size = (300,200)
Window.clearcolor = (255/255, 165/255, 0/266)
Window.title = 'Калькулятор'

class MyApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='Конвертер валют')
        self.dollar = Label(text='Доллары:')
        self.tenge = Label(text='Тенге:')
        self.belRub = Label(text='Белорусский рубль:')
        self.input_data = TextInput(hint_text='Введите значение: (руб.)', multiline=False)
        self.input_data.bind(text=self.on_text)

    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.dollar.text = 'Доллары: ' + str(float(data) / 76.84)
            self.tenge.text = 'Тенге: ' + str(float(data) / 0.1662)
            self.belRub.text = 'Бел.руб: ' + str(float(data) / 26.8)
        else:
            self.input_data.text = ''

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.dollar)
        box.add_widget(self.tenge)
        box.add_widget(self.belRub)
        return box


if __name__ == "__main__":
    MyApp().run()

