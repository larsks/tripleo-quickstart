Remove the configuration created by the `environment/setup` role:

- Remove whitelist entries from `/etc/qemu/bridge.conf`
- Destroy and undefine the libvirt networks

The `environment/teardown` role *will not* remove packages or attempt
to undo the KVM configuration, because these things may have been
configured prior to running the script and we do not want to break an
existing environment.
