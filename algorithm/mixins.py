class CleaningMixin:
    def deep_clen(self, value):
        return value

    def clean(self, value):
        value = value.strip()
        return self.deep_clen(value)
