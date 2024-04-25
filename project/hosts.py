from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'authentication', 'authentication.urls', name='authentication'),
    host(r'city', 'city.urls', name='city'),
    host(r'hotel', 'hotel.urls', name='hotel'),
)