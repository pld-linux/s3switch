Summary:	Utility to switch your display between the various output devices on S3 Savage cards
Summary(pl):	Narzêdzie s³u¿±ce do prze³±czania siê pomiêdzy ró¿nymi wyj¶ciami na kartach S3 Savage
Name:		s3switch
Version:	20031205
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.probo.com/timr/s3ssrc.zip
# Source0-md5:	1328b070343ac79c5ed4c613a1113754
BuildRequires:	glibc-devel
BuildRequires:	glibc-kernel-headers
BuildRequires:	make
BuildRequires:	unzip
Requires:	glibc >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility that will allow you to switch your display between the various
output devices supported by the Savage (CRT, LCD, TV).

%description -l pl
Narzêdzie które pozwala prze³±czaæ wy¶iwetlanie ekranu pomiêdzy
ró¿nymi urz±dzeniami wyj¶ciowymi wspieranymi przez S3 Savage (CRT,
LCD, TV).

%prep
%setup -q -c

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
install s3switch $RPM_BUILD_ROOT%{_sbindir}
install s3switch.1x $RPM_BUILD_ROOT%{_mandir}/man8/s3switch.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*
