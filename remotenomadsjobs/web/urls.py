from django.urls import path

from remotenomadsjobs.web.views import indexView, DashboardView, CompanyProfileCreatView, UserProfileCreatView, \
    CompanyProfileUpdateView, UserProfileUpdateView, ProfileUpdateView, ContactFormView

urlpatterns = (

    path('', indexView.as_view(), name='index'),
    path("dashboard/", DashboardView.as_view(), name='dashboard'),

    path("save_user/", UserProfileCreatView.as_view(), name='save_user'),
    path("save_company/", CompanyProfileCreatView.as_view(), name='save_company'),

    path("profile/", ProfileUpdateView.as_view(), name='update_profile'),
    path("company_profile/", CompanyProfileUpdateView.as_view(), name='update_company_profile'),
    path("user_profile/", UserProfileUpdateView.as_view(), name='update_user_profile'),

    path("contact/", ContactFormView.as_view(), name='contact_form'),
)