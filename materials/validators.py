from rest_framework  import serializers

allow_site = "https://www.youtube.com/"
# https://www.youtube.com/shorts/5e-fKWcvrZQ

def validate_allow_site(value):
    url = value.lower()
    if url and not url.startswith(allow_site):
        raise serializers.ValidationError("Использована ссылка на сторонние образовательные ресурсы")
