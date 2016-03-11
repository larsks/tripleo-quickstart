# Tripleo-quickstart roles

(This documentation was assembled automatically)

## Overview

The following diagram illustrates the workflow of the
tripleo-quickstart process.  Roles colored <span style="color:
red">red</span> require root privileges on the remote host; roles
colored <span style="color: green">green</span> are run as an
unprivileged user.

![tripleo-quickstart workflow](workflow.png)

## Roles
- [common](#common)
- [environment](#environment)
- [environment/teardown](#environment/teardown)
- [environment/setup](#environment/setup)
- [libvirt](#libvirt)
- [libvirt/teardown](#libvirt/teardown)
- [libvirt/setup](#libvirt/setup)
- [provision](#provision)
- [provision/remote](#provision/remote)
- [provision/local](#provision/local)
- [rebuild-inventory](#rebuild-inventory)
- [tripleo](#tripleo)
- [tripleo/overcloud](#tripleo/overcloud)
- [tripleo/undercloud](#tripleo/undercloud)
- [images](#images)
- [parts](#parts)
- [parts/libvirt](#parts/libvirt)
- [parts/kvm](#parts/kvm)

## <a id="common">common</a>

The `common` module defines variables that are used throughout the
playbooks.  In particular, it declares the disk and memory allocations
in the `flavors` variable, virtual infrastructure layout in the
`overcloud_nodes` variable and the network configuration in the
`networks` variable.

## <a id="environment">environment</a>

Roles that require root privileges on the target host in order to
perform system configuration tasks.

### <a id="environment/teardown">environment/teardown</a>

Remove the configuration created by the `environment/setup` role:

- Remove whitelist entries from `/etc/qemu/bridge.conf`
- Destroy and undefine the libvirt networks

The `environment/teardown` role *will not* remove packages or attempt
to undo the KVM configuration, because these things may have been
configured prior to running the script and we do not want to break an
existing environment.

### <a id="environment/setup">environment/setup</a>

Perform basic system configuration on the target host:

- Install `libvirt` via the `parts/libvirt` role.
- Configure kvm via the `parts/kvm` role.
- Configure the libvirt networks defined in the `networks` variable
- Whitelist the libvirt network bridges in `/etc/qemu/bridge.conf` (or
  equivalent file)

## <a id="libvirt">libvirt</a>

The `libvirt` roles are responsible for setting up the virtual
infrastructure on the target host.

### <a id="libvirt/teardown">libvirt/teardown</a>

Removes the virtual resources created by the `libvirt/setup` role:

- Deletes virtual machines and associated storage
- Deletes the libvirt storage pool
- Removes ssh key used for undercloud access to the host libvirt

### <a id="libvirt/setup">libvirt/setup</a>

Sets up the virtual infrastructure:

- Downloads the undercloud base image
- Configures the base image
- Creates (but does not boot) the overcloud vms
- Creates the undercloud vm
- Creates an ssh key that will be used by the undercloud to control
  libvirt on your host, and installs the public key into the
  `authorized_keys` file of the `stack` user on your host.

## <a id="provision">provision</a>

The `provision` roles are responsible for preparing a target host for
the rest of the playbooks.

### <a id="provision/remote">provision/remote</a>

Creates a non-root user (by default `stack`) on the target host,
generates ssh keys for logging in as that user, and grants that user
`sudo` privileges.  This role *modifies* the in-memory inventory to
use the new non-root user for subsequent Ansible connections, rather
than using `root`.

### <a id="provision/local">provision/local</a>

Adds the target host to the in-memory Ansible inventory.

## <a id="rebuild-inventory">rebuild-inventory</a>

Generates an Ansible inventory file from the in-memory inventory using
the `templates/inventory.j2` template.

## <a id="tripleo">tripleo</a>

The `tripleo` roles are responsible for installing the undercloud and
deploying the overcloud using [tripleo][].

[tripleo]: http://docs.openstack.org/developer/tripleo-docs/

### <a id="tripleo/overcloud">tripleo/overcloud</a>

Runs `openstack overcloud deploy` and performs some post-deploy
validation.

### <a id="tripleo/undercloud">tripleo/undercloud</a>

Configures the undercloud and runs `openstack undercloud deploy`.
When this role completes you have a fully functioning undercloud
environment.

You can log into the undercloud using the generated ssh configuration
(`ssh -F ~/.quickstart/ssh.config.ansible undercloud`) and then load
in the undercloud credentials (`. stackrc`) to interact with the
undercloud services.

## <a id="images">images</a>

Contains roles used to build and publish the undercloud image.

## <a id="parts">parts</a>

These roles install and/or configure individual components, and should
not depend on any configuration or roles from outside of the `parts/`
directory.

### <a id="parts/libvirt">parts/libvirt</a>

This role installs `libvirt` and dependencies and starts the
`libvirtd` daemon.

### <a id="parts/kvm">parts/kvm</a>

This roles configures [kvm][].  It will:

- Determine the appropriate architecture-specific module to load
  (`kvm_intel` vs `kvm_amd`)
- Detect if your host supports nested virtualization.
- Configure nested virtualization if appropriate.
- Load the necessary modules.
- Make the configuration persistent via changes in `/etc/modprobe.d`
  and `/etc/module-load.d`.

[kvm]: http://www.linux-kvm.org/page/Main_Page


---
<https://github.com/redhat-openstack/tripleo-quickstart/>
