class Name:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value: str):
        if value.istitle():
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Имя должно начинаться с заглавной буквы')

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)