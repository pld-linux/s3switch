Summary:	Utility to switch display between the various output devices on S3 Savage cards
Summary(pl.UTF-8):	Narzędzie do przełączania się pomiędzy różnymi wyjściami na kartach S3 Savage
Name:		s3switch
Version:	20031205
Release:	4
License:	Distributable
Group:		Applications/System
URL:		http://www.probo.com/timr/savage40.html
Source0:	ftp://ftp.probo.com/pub/s3ssrc.zip
# Source0-md5:	1328b070343ac79c5ed4c613a1113754
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Patch0:		%{name}-glibc-kernel-headers.patch
Patch1:		%{name}-thinkpad-t23.patch
BuildRequires:	unzip
Requires(post,preun):	/sbin/chkconfig
Requires:	glibc >= 2.2
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility that will allow you to switch your display between the various
output devices supported by the Savage (CRT, LCD, TV).

%description -l pl.UTF-8
Narzędzie pozwalające przełączać wyświetlanie ekranu pomiędzy różnymi
urządzeniami wyjściowymi wspieranymi przez S3 Savage (CRT, LCD, TV).

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{sysconfig,rc.d/init.d} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install s3switch $RPM_BUILD_ROOT%{_sbindir}
install s3switch.1x $RPM_BUILD_ROOT%{_mandir}/man8/s3switch.8
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/s3switch
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/s3switch

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add s3switch

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del s3switch
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/s3switch
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/s3switch
%{_mandir}/man*/*
