from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Netcastr_django.views.home', name='home'),
    # url(r'^Netcastr_django/', include('Netcastr_django.foo.urls')),

	# Login / logout.
    url(r'^login/$', 'django.contrib.auth.views.login'),
    #(r'^logout/$', logout_page),

    url(r'^netcastr/', include('netcastr.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)