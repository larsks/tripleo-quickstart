Configures the undercloud and runs `openstack undercloud deploy`.
When this role completes you have a fully functioning undercloud
environment.

You can log into the undercloud using the generated ssh configuration
(`ssh -F ~/.quickstart/ssh.config.ansible undercloud`) and then load
in the undercloud credentials (`. stackrc`) to interact with the
undercloud services.
