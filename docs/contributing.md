# Contributing to tripleo-quickstart

If you *fix* a problem or implement a new feature, you may submit your
changes via Gerrit. The `tripleo-quickstart` project uses a Gerrit
workflow similar to the [OpenStack Gerrit workflow][gerrit].

[gerrit]: http://docs.openstack.org/infra/manual/developers.html#development-workflow

We're currently using Gerrit hosted on [gerrithub][], so you will need
to establish an account there first.

[gerrithub]: http://review.gerrithub.io/

Once your gerrithub account is ready, install the [git-review][] tool,
then from within a clone of the tripleo-quickstart repository run:

[git-review]: http://docs.openstack.org/infra/manual/developers.html#installing-git-review

    git review -s

After you have made your changes locally, commit them to a feature
branch, and then submit them for review by running:

    git review

Your changes will be tested by our [automated CI
infrastructure][rdoci], and will also be reviewed by other developers.
If you need to make changes (and you probably will; it's not uncommon
for patches to go through several iterations before being accepted),
make the changes on your feature branch, and instead of creating a new
commit, *amend the existing commit*, making sure to retain the
`Change-Id` line that was placed there by `git-review`:

[rdoci]: https://ci.centos.org/view/rdo/

    git ci --amend

After committing your changes, resubmit the review:

    git review

