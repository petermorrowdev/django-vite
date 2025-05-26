from django.contrib.staticfiles.views import serve
from django.http.response import Http404
from django.shortcuts import redirect

from django_vite.core.asset_loader import DjangoViteAssetLoader


def vite_static_redirect(request, path, insecure=False):
    try:
        response = serve(request, path, insecure)
    except Http404 as e:
        vite_dev_url = DjangoViteAssetLoader.instance().generate_vite_asset_url(path)
        if vite_dev_url is not None:
            return redirect(vite_dev_url, permanent=False)
        else:
            raise Http404 from e
    else:
        return response
