Example of a (modern?) Django project deployed heroku style
using dokku.

You can try it with the dokku installation in the vagrant machine as
configured in the original dokku's repository at

    https://github.com/progrium/dokku

To launch vagrant and configure the access with a public key you can
execute the following

    $ vagrant up
    $ cat vagrant.pub | ssh vagrant "sudo sshcommand acl-add dokku <name>"

The vagrant (insecure) public key file (``vagrant.pub``) can be found here

    https://github.com/mitchellh/vagrant/blob/master/keys/vagrant.pub

It's possible to configure ssh to use "vagrant" as alias appending the
output of ``vagrant ssh-config`` to your ``.ssh/config`` file.

Now you can push from this repository simply adding a remote pointing
to the machine

    $ git remote add <whatever> dokku@vagrant:<name>
    $ git push <whatever> master
    Counting objects: 4, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 817 bytes | 0 bytes/s, done.
    Total 3 (delta 1), reused 0 (delta 0)
    -----> Cleaning up ...
    -----> Building <name> ...
           Python app detected
    -----> No runtime.txt provided; assuming python-2.7.4.
    -----> Using Python runtime (python-2.7.4)
    -----> Installing dependencies using Pip (1.3.1)
           Cleaning up...
    -----> Collecting static files
           69 static files copied.

    -----> Discovering process types
           Procfile declares types -> web
    -----> Releasing <name> ...
    -----> Deploying <name> ...
    =====> Application deployed:
           http://<name>.dokku.me

    To dokku@vagrant:<name>
     + 1eb114d...5f1edf0 master -> master


Now the application should be published under a subdomain like

    http://<name>.dokku.me

remember that the subdomain is hardcoded into the Vagrantfile and that
the virtual machine has forwarded the port 80 to the port 8080.

It is also possible to execute dokku command directly using ssh, for example

    $ ssh -t dokku@vagrant logs <name>
    2013-12-05 15:58:23 [11] [INFO] Starting gunicorn 18.0
    2013-12-05 15:58:23 [11] [INFO] Listening at: http://0.0.0.0:5000 (11)
    2013-12-05 15:58:23 [11] [INFO] Using worker: sync
    2013-12-05 15:58:23 [16] [INFO] Booting worker with pid: 16
    Connection to 127.0.0.1 closed.

Dokku use only the ``web`` voice into the ``Procfile``, if you want an approach
like ``heroku`` you can use ``dokku-shoreman``.

Furthemore ``celery`` complains about running it as root, so to make it works you
have to configure the ``C_FORCE_ROOT`` environment variable:

    $ ssh -t dokku@vagrant config:set elipse C_FORCE_ROOT=1

LOCAL DEVELOPMENT
-----------------

Since we want to use the same approach of the heroku applications, we
use ``honcho`` as ```Foreman`` replacement, so is enough to launch the
following command

    $ honcho start

from the root directory of the project.
