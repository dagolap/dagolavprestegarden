exec { "apt-update":
    command => "/usr/bin/apt-get update"
}
Exec["apt-update"] -> Package <| |> # Ensures apt-get update is run before any package installation starts

Package { ensure => "present" }
package { 'dev':
    name => ['tmux', 'python-virtualenv', 'virtualenvwrapper', 'vim', 'python-dev']
}