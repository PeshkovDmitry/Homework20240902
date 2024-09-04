class Price:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value: (int, float)):
        if value > 0:
            setattr(instance, self.param_name, value)
        else:
            raise ValueError("Цена должна быть положительной")

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

