Sets up the virtual infrastructure:

- Downloads the undercloud base image
- Configures the base image
- Creates (but does not boot) the overcloud vms
- Creates the undercloud vm
- Creates an ssh key that will be used by the undercloud to control
  libvirt on your host, and installs the public key into the
  `authorized_keys` file of the `stack` user on your host.
