class Age:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value: int):
        if value in range(0, 120 + 1):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError("Имя должно быть целым числом в диапазоне от 0 до 120")

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

