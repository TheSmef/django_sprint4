from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

handler403 = "pages.views.permission_denied"
handler404 = "pages.views.page_not_found"
handler500 = "pages.views.server_error"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/registration/', CreateView.as_view(
        template_name='registration/registration_form.html',
        form_class=UserCreationForm,
        success_url=reverse_lazy('login'),
    ), name='registration'),
    path('pages/', include('pages.urls', namespace='pages')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('blog.urls', namespace='blog')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
