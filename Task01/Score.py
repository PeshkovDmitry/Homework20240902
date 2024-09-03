class Score:

    def __init__(self, min_val: int, max_val: int, error_message: str):
        self.min_val = min_val
        self.max_val = max_val
        self.error_message = error_message

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value: int):
        if value in range(self.min_val, self.max_val + 1):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(self.error_message)

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

