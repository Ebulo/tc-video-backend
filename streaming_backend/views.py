from django.http import HttpResponse


def verifySite(request):
    filename = "B0184553A4E9FD077261539D69B80460.txt"
    content = '''5150DCA32BE697FE3002AE67BF014E74DE8B9DD0203712A614640518C13E895B
comodoca.com
3cd9b6796ae29e9'''
    response = HttpResponse(content, content_type='text/plain')
    # response['Content-Disposition'] = 'attachment; filename={0}'.format(
    #     filename)
    return response
