from django.shortcuts import render
from .forms import ApiForm
from .call_api import call_api


def index(request):
    if request.method == 'POST':
        form = ApiForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            method = form.cleaned_data['method']
            result = call_api(url, method)
            return render(request, 'call_api.html', {'form': form, 'result': result, 'url': url, 'method': method})
    else:
        form = ApiForm()
        return render(request, 'call_api.html', {'form': form})