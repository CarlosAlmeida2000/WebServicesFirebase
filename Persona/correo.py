from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

class Correo:
    
    def send(self, destinatario, asunto, template, context):
        try:
            settings.EMAIL_HOST_USER = 'carlosivanalmeida10@gmail.com'
            settings.EMAIL_HOST_PASSWORD = 'lossblzlnzwepzqf'
            tplCorreo = get_template(template)
            content = tplCorreo.render(context)
            email = EmailMultiAlternatives(asunto, " ", settings.EMAIL_HOST_USER, [destinatario])
            email.attach_alternative(content, "text/html")
            email.send()
            return True
        except Exception as e:
            return False