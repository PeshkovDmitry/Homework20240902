class Email:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value: str):
        if value.count("@"):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Адрес электронной почты должен содержать символ @')

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)