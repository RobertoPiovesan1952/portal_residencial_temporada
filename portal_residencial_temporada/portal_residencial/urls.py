from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from portal_publico import views as publico
from core import views as core
from moradores import views as moradores

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", publico.home, name="home"),
    path("estrutura/", publico.estrutura, name="estrutura"),
    path("regras/", publico.regras, name="regras"),
    path("solicitar-vaga/", publico.solicitar_vaga, name="solicitar_vaga"),
    path("obrigado/", publico.obrigado, name="obrigado"),

    path("portal/login/", auth_views.LoginView.as_view(template_name="admin_portal/login.html"), name="login"),
    path("portal/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("portal/", core.dashboard, name="dashboard"),
    path("portal/candidatos/", moradores.candidatos_lista, name="candidatos_lista"),
    path("portal/candidatos/<int:pk>/", moradores.candidato_detalhe, name="candidato_detalhe"),
    path("portal/candidatos/<int:pk>/aprovar/", moradores.aprovar_candidato, name="aprovar_candidato"),
    path("portal/moradores/", moradores.moradores_lista, name="moradores_lista"),
    path("portal/moradores/<int:pk>/", moradores.morador_detalhe, name="morador_detalhe"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
