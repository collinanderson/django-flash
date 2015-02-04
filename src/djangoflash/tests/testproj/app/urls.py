from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^default/$', views.render_template),
    url(r'^set_flash_var/$', views.set_flash_var, name='app.views.set_flash_var'),
    url(r'^set_another_flash_var/$', views.set_another_flash_var),
    url(r'^set_now_var/$', views.set_now_var),
    url(r'^keep_var/$', views.keep_var),
    url(r'^keep_var_decorator/$', views.keep_var_decorator),
    url(r'^discard_var/$', views.discard_var),
    url(r'^replace_flash/$', views.replace_flash),
    url(r'^remove_flash/$', views.remove_flash),
]
