# connect to a server Execute a command

file_line{'/etc/ssh/ssh_config'
  ensure  => 'present',
  content => 'PasswordAuthentication no
              IdentityFile ~/.ssh/holberton'
}
