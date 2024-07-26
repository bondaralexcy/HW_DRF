from rest_framework  import serializers

allow_site = "https://www.youtube.com/"
# Например: https://www.youtube.com/shorts/5e-fKWcvrZQ

def validate_allow_site(value):
    url = value.lower()
    if url and not url.startswith(allow_site):
        raise serializers.ValidationError("Использована ссылка на сторонние образовательные ресурсы")


# Если через класс, то надо так:
#
# class ValidateURLResource():
#
#     def __init__(self, field):
#         self.field = field
#
#     def __call__(self, value):
#         url = value.get(self.field)
#         if url and not url.startswith('https://www.youtube.com/'):
#             raise ValueError('Использована ссылка на сторонние образовательные ресурсы')
