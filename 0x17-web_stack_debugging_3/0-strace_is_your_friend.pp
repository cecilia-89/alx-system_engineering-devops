#automates apache2 server

package {'puppet':
ensure  => installed
}

file {'index.html':
ensure => file
path   => '/var/www/html/index.html',
}