class Main:
    __value = 5

    def get_value():
        return Main.__value

    def set_value(new_value):
        Main.__value = new_value


Main.set_value(4)
print(Main.get_value())
