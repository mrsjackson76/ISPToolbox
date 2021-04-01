from django.shortcuts import render


def Error500View(request, **kwargs):
    context = {
        'error_title': 'An error occured',
        'error_msg': 'Sorry, your request could not be processed.'
    }
    return render(request, 'workspace/error.html', context, status=500)


def Error404View(request, exception, **kwargs):
    context = {
        'error_title': 'Page not found',
        'error_msg': 'Sorry, the page you\'re looking for doesn\'t exist or may have moved.'
    }
    return render(request, 'workspace/error.html', context, status=404)


def Error403View(request, exception, **kwargs):
    context = {
        'error_title': 'Forbidden',
        'error_msg': 'Sorry, you\'re not authorized to perform that request'
    }
    return render(request, 'workspace/error.html', context, status=403)
