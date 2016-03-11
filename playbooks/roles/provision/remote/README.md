Creates a non-root user (by default `stack`) on the target host,
generates ssh keys for logging in as that user, and grants that user
`sudo` privileges.  This role *modifies* the in-memory inventory to
use the new non-root user for subsequent Ansible connections, rather
than using `root`.
