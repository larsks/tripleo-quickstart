Perform basic system configuration on the target host:

- Install `libvirt` via the `parts/libvirt` role.
- Configure kvm via the `parts/kvm` role.
- Configure the libvirt networks defined in the `networks` variable
- Whitelist the libvirt network bridges in `/etc/qemu/bridge.conf` (or
  equivalent file)
