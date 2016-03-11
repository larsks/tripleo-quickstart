This roles configures [kvm][].  It will:

- Determine the appropriate architecture-specific module to load
  (`kvm_intel` vs `kvm_amd`)
- Detect if your host supports nested virtualization.
- Configure nested virtualization if appropriate.
- Load the necessary modules.
- Make the configuration persistent via changes in `/etc/modprobe.d`
  and `/etc/module-load.d`.

[kvm]: http://www.linux-kvm.org/page/Main_Page

