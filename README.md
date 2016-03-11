# tripleo-quickstart

One of the barriers to entry for trying out TripleO and its derivatives
has been the relative difficulty in getting an environment up quickly.

This set of ansible roles is meant to help.

You will need a host machine with at least 16G of RAM, preferably 32G,
with CentOS 7 installed. You must be able to `ssh` into your target
machine as root without a password from the system running ansible.

A quick way to test that your host (referred to as \$VIRTHOST)
is ready to rock is:

    ssh root@$VIRTHOST uname -a

The defaults are meant to "just work", so it is as easy as downloading
and running the quickstart.sh script.

The quickstart.sh script will install this repository along with
ansible in a virtual environment and run the quickstart playbook.
Note, the quickstart playbook will delete the `stack` user on the
virthost and recreate it.:

    VIRTHOST='my_test_machine.example.com'

    wget https://raw.githubusercontent.com/redhat-openstack/tripleo-quickstart/master/quickstart.sh
    bash quickstart.sh $VIRTHOST

This script will output instructions at the end to access the deployed
undercloud. If a release name is not given, `mitaka` is used.

## Pre-fetching images

It is possible to pre-download the undercloud.qcow2 image, and use it
for multiple runs. From the machine that will be the virthost, create
a directory for the undercloud image and wget it. The image location
should be world readable since a `stack` user is used for most steps.:

    mkdir -p /usr/share/quickstart_images/mitaka/
    cd /usr/share/quickstart_images/mitaka/
    wget http://artifacts.ci.centos.org/rdo/images/mitaka/delorean/stable/undercloud.qcow2.md5 \
    https://ci.centos.org/artifacts/rdo/images/mitaka/delorean/stable/undercloud.qcow2

    # Check that the md5sum's match (The playbook will also
    # check, but better to know now whether the image download
    # was ok.)
    md5sum -c undercloud.qcow2.md5

Then use the quickstart.sh script with the -u option:

   VIRTHOST='my_test_machine.example.com'
   UNDERCLOUD_QCOW2_LOCATION=file:///usr/share/quickstart_images/mitaka/undercloud.qcow2

    wget https://raw.githubusercontent.com/redhat-openstack/tripleo-quickstart/master/quickstart.sh

    bash quickstart.sh -u $UNDERCLOUD_QCOW2_LOCATION $VIRTHOST

To install `tripleo-quickstart` yourself instead of via the
quickstart.sh script:

    pip install git+https://github.com/redhat-openstack/tripleo-quickstart.git@master#egg=tripleo-quickstart

Playbooks will be located in either
`/usr/local/share/tripleo-quickstart` or in
`$VIRTUAL_ENV/usr/local/share/tripleo-quickstart` if you have installed
in a virtual environment.

## Documentation

There is some documentation in the [docs](docs/) directory.
Documentation patches are very welcome!

## Support

If you encounter any problems with `tripleo-quickstart` or if you have
feature suggestions, please feel free to open a bug report in [our issue
tracker](https://github.com/redhat-openstack/tripleo-quickstart/issues/).

You can usually find the developers hanging out on the `#rdo` channel
on [freenode][].

## Contributing

See [docs/contributing.md](docs/contributing.md) for instructions on how to contribute code
to tripleo-quickstart.

## Copyright

Copyright 2016 Red Hat, Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at <http://www.apache.org/licenses/LICENSE-2.0>.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[freenode]: https://freenode.net/
