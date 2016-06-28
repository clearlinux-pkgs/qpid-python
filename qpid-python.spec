#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qpid-python
Version  : 0.32
Release  : 14
URL      : http://apache.arvixe.com/qpid/0.32/qpid-python-0.32.tar.gz
Source0  : http://apache.arvixe.com/qpid/0.32/qpid-python-0.32.tar.gz
Summary  : Python client implementation for Apache Qpid
Group    : Development/Tools
License  : Apache-2.0
Requires: qpid-python-bin
Requires: qpid-python-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools
Patch1: 0001-Remove-tabs.patch

%description
This distribution contains the Python client libraries for Apache Qpid.
Apache Qpid is a high-speed, language independent, platform
independent enterprise messaging system. It currently provides two
messaging brokers (one implemented in C++, one implemented in Java),
and messaging client libraries for Java JMS, C++, C# .NET, Python,
Ruby, and WCF. The messaging protocol for Apache Qpid is AMQP
(Advanced Message Queuing Protocol). You can read more about Qpid
here:

%package bin
Summary: bin components for the qpid-python package.
Group: Binaries

%description bin
bin components for the qpid-python package.


%package python
Summary: python components for the qpid-python package.
Group: Default

%description python
python components for the qpid-python package.


%prep
%setup -q -n qpid-python-0.32
%patch1 -p1

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
./qpid-python-test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/qpid-python-test

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
