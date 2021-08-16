# set up the client SSH configuration file ussing puppet
file_line { 'change identityfile':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  match  => '^IdentityFile',
  line   => 'IdentityFile ~/.ssh/holberton'
}

file_line {'configure passwd':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
}
