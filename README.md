Data for Mock integration testing
=================================

Content of this project is consumed by
[mock's](https://github.com/rpm-software-management/mock/tree/master/mock/integration-tests)
[integration tests](https://github.com/rpm-software-management/mock/tree/master/mock/integration-tests).

You probably want to have a look at [the docs](https://raw.githubusercontent.com/rpm-software-management/mock/master/mock/docs/release-instructions.txt).

Files & Directories
-------------------

`python-copr-999-1.src.rpm`, example source rpm package which uses two-phase
dynamic build requires.  Can be built on Fedora 31+.

`dep-on-python-copr-999-1-0.src.rpm` depends both build/run-time on the
python-copr package above.

`daemon-test-1-0.src.rpm` package starts `test-daemon` process on background
during build, and in %posttrans.  The process shuts down after 5 minutes itself,
if not killed.

`repo` is DNF/YUM repository providing testing package named
`always-installable`, and is available on "baseurl"
https://raw.githubusercontent.com/rpm-software-management/mock-test-data/master/repo/
