Summary:	The Emacs text editor for the X Window System.
Name:		emacs
Version:	20.7
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	Aplicações/Editores/Emacs
Source0:	ftp://ftp.gnu.org/gnu/emacs/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/gnu/emacs/leim-%{version}.tar.gz
Source3:	%{name}.desktop
Source4:	%{name}-dotemacs
Source5:	%{name}-site-start.el
Patch0:		%{name}-xaw3d.patch
Patch1:		%{name}-manboption.patch
Patch2:		%{name}-tmprace.patch
Patch3:		%{name}-linkscr.patch
Patch4:		%{name}-nmhlocation.patch
Patch5:		%{name}-loadup.patch
Patch6:		%{name}-kbdbuffer.patch
Patch7:		%{name}-ia64.patch
Patch8:		%{name}-ia64-2.patch
Patch9:		%{name}-ia64-3.patch
Patch10:	%{name}-lisp-startup-localealias.patch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		/usr/sbin/fix-info-dir
Requires:	emacs-common

%description
Emacs-X11 includes the Emacs text editor program for use with the X
Window System (it provides support for the mouse and other GUI
elements). Emacs-X11 will also run Emacs outside of X, but it has a
larger memory footprint than the 'non-X' Emacs package (emacs-nox).

Install emacs-X11 if you're going to use Emacs with the X Window
System. You should also install emacs-X11 if you're going to run Emacs
both with and without X (it will work fine both ways). You'll also
need to install the emacs package in order to run Emacs.

%package el
Summary:	The sources for elisp programs included with Emacs.
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	Aplicações/Editores/Emacs
Requires:	emacs-common

%description el
Emacs-el contains the emacs-elisp sources for many of the elisp
programs included with the main Emacs text editor package.

You need to install emacs-el only if you intend to modify any of the
Emacs packages or see some elisp examples.

%package leim
Summary:	Emacs Lisp code for input methods for international characters.
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	Aplicações/Editores/Emacs
Requires:	emacs-common

%description leim
The emacs-leim package contains Emacs Lisp code for input methods for
various international character scripts. Basically, the Lisp code
provided by this package describes the consecutive keystrokes that a
user must press in order to input a particular character in a
non-English character set. Input methods for many different language's
character sets are included in this package.

%package leim-el
Summary:	Emacs Lisp source code for input methods for international characters.
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	Aplicações/Editores/Emacs
Requires:	emacs-leim

%description leim-el
Emacs Lisp source code for input methods for international characters.

%package nox
Summary:	The Emacs text editor without support for the X Window System.
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	Aplicações/Editores/Emacs
Requires:	emacs-common

%description nox
Emacs-nox is the Emacs text editor program without support for the X
Window System.

You need to install this package only if you plan on exclusively using
Emacs without the X Window System (emacs-X11 will work both in X and
out of X, but emacs-nox will only work outside of X). You'll also need
to install the emacs package in order to run Emacs.

%package common
Summary:	The libraries needed to run the GNU Emacs text editor.
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	Aplicações/Editores/Emacs

%description common
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news and more
without leaving the editor.

This package includes the libraries you need to run the Emacs editor,
so you need to install this package if you intend to use Emacs. You
also need to install the actual Emacs program package (emacs-nox or
emacs). Install emacs-nox if you are not going to use the X Window
System; install emacs if you will be using X.

%prep
%setup -q -b 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p0

%build
libtoolize --force --copy
autoconf

# Build binary with X support
[ -d build-withx ] && rm -rf build-withx
mkdir build-withx && cd build-withx
CFLAGS="$RPM_OPT_FLAGS -DNCURSES_OSPEED_T" LDFLAGS=-s \
../configure \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--prefix=%{_prefix} \
	--libexecdir=%{_libdir} \
	--sharedstatedir=/var \
	--with-gcc \
	--with-pop \
	--with-x-toolkit \
	%{_target_platform}

%{__make} 
cd ..

#Build binary without X support
[ -d build-nox ] && rm -rf build-nox
mkdir build-nox && cd build-nox
CFLAGS="$RPM_OPT_FLAGS -DNCURSES_OSPEED_T" LDFLAGS=-s \
../configure \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--prefix=%{_prefix} \
	--libexecdir=%{_libdir} \
	--sharedstatedir=/var \
	--with-gcc \
	--with-pop \
	--with-x=no \
	%{_target_platform}

%{__make}
cd ..

# recompile patched .el files
build-withx/src/emacs \
	-batch \
	--no-init-file \
	--no-site-file \
	-f batch-byte-compile \
	lisp/mail/mh-utils.el

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_libdir}/emacs/site-lisp} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Development/Editors,/etc/skel}

%{__make} install -C build-withx \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	libexecdir=$RPM_BUILD_ROOT%{_libdir} \
	sharedstatedir=$RPM_BUILD_ROOT/var \
	mandir=$RPM_BUILD_ROOT/%{_mandir} \
	infodir=$RPM_BUILD_ROOT/%{_infodir}

install build-nox/src/emacs $RPM_BUILD_ROOT%{_bindir}/emacs-nox

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Development/Editors
install %{SOURCE4} $RPM_BUILD_ROOT/etc/skel/.emacs
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.el

install build-nox/etc/DOC-* $RPM_BUILD_ROOT%{_datadir}/emacs/%{version}/etc

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/emacs/*-linux/* || :

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
gzip -9nf $RPM_BUILD_ROOT%{_infodir}/* $RPM_BUILD_ROOT%{_mandir}/man1/* \
	etc/NEWS BUGS README etc/FAQ

%clean
rm -rf $RPM_BUILD_ROOT
  
%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%triggerin nox -- emacs-X11
if [ -L %{_bindir}/emacs ]; then
	rm -f %{_bindir}/emacs
fi

%triggerpostun nox -- emacs-X11
[ $2 = 0 ] || exit 0
if [ ! -L %{_bindir}/emacs ]; then
	ln -sf emacs-nox %{_bindir}/emacs
fi

%post nox
if [ ! -x %{_bindir}/emacs -a ! -L %{_bindir}/emacs ]; then
	ln -sf emacs-nox %{_bindir}/emacs
fi

%postun nox
[ $1 = 0 ] || exit 0
if [ -L %{_bindir}/emacs ]; then
	rm -f %{_bindir}/emacs
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/emacs
%attr(755,root,root) %{_bindir}/emacs-%{version}
%{_applnkdir}/Development/Editors/emacs.desktop

%files common
%defattr(644,root,root,755)
%config(noreplace) /etc/skel/.emacs
%doc {etc/NEWS,BUGS,README,etc/FAQ}.gz
%attr(755,root,root) %{_bindir}/b2m
%attr(755,root,root) %{_bindir}/emacsclient
%attr(755,root,root) %{_bindir}/rcs-checkin
%{_mandir}/man1/emacs*
%{_infodir}/*

%dir %{_libdir}/emacs
%dir %{_libdir}/emacs/site-lisp
%dir %{_libdir}/emacs/%{version}
%dir %{_libdir}/emacs/%{version}/*

%attr(2755,root,mail) %{_libdir}/emacs/%{version}/*-linux/movemail
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/cvtmail
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/digest-doc
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/emacsserver
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/fakemail
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/hexl
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/profile
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/rcs2log
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/sorted-doc
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/vcdiff
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/yow
%{_libdir}/emacs/%{version}/*/fns-20.7.1.el

%dir %{_datadir}/emacs/%{version}
%dir %{_datadir}/emacs/%{version}/site-lisp
%dir %{_datadir}/emacs/%{version}/lisp
%dir %{_datadir}/emacs/%{version}/lisp/calendar
%dir %{_datadir}/emacs/%{version}/lisp/emacs-lisp
%dir %{_datadir}/emacs/%{version}/lisp/emulation
%dir %{_datadir}/emacs/%{version}/lisp/gnus
%dir %{_datadir}/emacs/%{version}/lisp/international
%dir %{_datadir}/emacs/%{version}/lisp/language
%dir %{_datadir}/emacs/%{version}/lisp/mail
%dir %{_datadir}/emacs/%{version}/lisp/play
%dir %{_datadir}/emacs/%{version}/lisp/progmodes
%dir %{_datadir}/emacs/%{version}/lisp/term
%dir %{_datadir}/emacs/%{version}/lisp/textmodes

%{_datadir}/emacs/site-lisp
%{_datadir}/emacs/%{version}/etc
%{_datadir}/emacs/%{version}/lisp/*.elc
%{_datadir}/emacs/%{version}/lisp/README
%{_datadir}/emacs/%{version}/lisp/COPYING
%{_datadir}/emacs/%{version}/lisp/bindings.el
%{_datadir}/emacs/%{version}/lisp/cus-load.el
%{_datadir}/emacs/%{version}/lisp/cus-start.el
%{_datadir}/emacs/%{version}/lisp/generic-x.el
%{_datadir}/emacs/%{version}/lisp/loaddefs.el
%{_datadir}/emacs/%{version}/lisp/loadup.el
%{_datadir}/emacs/%{version}/lisp/patcomp.el
%{_datadir}/emacs/%{version}/lisp/paths.el
%{_datadir}/emacs/%{version}/lisp/subdirs.el
%{_datadir}/emacs/%{version}/lisp/version.el

%{_datadir}/emacs/%{version}/lisp/language/*.elc
%{_datadir}/emacs/%{version}/lisp/gnus/*.elc
%{_datadir}/emacs/%{version}/lisp/mail/*.elc
%{_datadir}/emacs/%{version}/lisp/mail/sc.el
%{_datadir}/emacs/%{version}/lisp/mail/blessmail.el
%{_datadir}/emacs/%{version}/lisp/play/*.elc
%{_datadir}/emacs/%{version}/lisp/play/bruce.el
%{_datadir}/emacs/%{version}/lisp/term/*.elc
%{_datadir}/emacs/%{version}/lisp/emulation/*.elc
%{_datadir}/emacs/%{version}/lisp/international/*.elc
%{_datadir}/emacs/%{version}/lisp/international/latin-*.el
%{_datadir}/emacs/%{version}/lisp/international/mule-conf.el
%{_datadir}/emacs/%{version}/lisp/calendar/*.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/*.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/*.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/*.elc

%files el
%defattr(644,root,root,755)
%{_datadir}/emacs/%{version}/lisp/forms-d2.dat

%{_datadir}/emacs/%{version}/lisp/a*.el
%{_datadir}/emacs/%{version}/lisp/ba*.el
%{_datadir}/emacs/%{version}/lisp/b[j-z]*.el
%{_datadir}/emacs/%{version}/lisp/c[a-t]*.el
%{_datadir}/emacs/%{version}/lisp/cus-[a-k]*.el
%{_datadir}/emacs/%{version}/lisp/custom.el
%{_datadir}/emacs/%{version}/lisp/generic.el
%{_datadir}/emacs/%{version}/lisp/g[f-z]*.el
%{_datadir}/emacs/%{version}/lisp/[d-f]*.el
%{_datadir}/emacs/%{version}/lisp/[h-k]*.el
%{_datadir}/emacs/%{version}/lisp/l[a-n]*.el
%{_datadir}/emacs/%{version}/lisp/loadhist.el
%{_datadir}/emacs/%{version}/lisp/locate.el
%{_datadir}/emacs/%{version}/lisp/l[p-z]*.el
%{_datadir}/emacs/%{version}/lisp/[m-o]*.el
%{_datadir}/emacs/%{version}/lisp/paren.el
%{_datadir}/emacs/%{version}/lisp/p[b-z]*.el
%{_datadir}/emacs/%{version}/lisp/[q-r]*.el
%{_datadir}/emacs/%{version}/lisp/s-*.el
%{_datadir}/emacs/%{version}/lisp/s[a-t]*.el
%{_datadir}/emacs/%{version}/lisp/subr.el
%{_datadir}/emacs/%{version}/lisp/sun*.el
%{_datadir}/emacs/%{version}/lisp/[t-u]*.el
%{_datadir}/emacs/%{version}/lisp/[w-z]*.el
%{_datadir}/emacs/%{version}/lisp/v[a-d]*.el
%{_datadir}/emacs/%{version}/lisp/v[f-z]*.el

%{_datadir}/emacs/%{version}/lisp/language/*.el
%{_datadir}/emacs/%{version}/lisp/gnus/*.el
%{_datadir}/emacs/%{version}/lisp/mail/[c-r]*.el
%{_datadir}/emacs/%{version}/lisp/mail/[t-z]*.el
%{_datadir}/emacs/%{version}/lisp/mail/sendmail.el
%{_datadir}/emacs/%{version}/lisp/mail/smtpmail.el
%{_datadir}/emacs/%{version}/lisp/mail/supercite.el
%{_datadir}/emacs/%{version}/lisp/play/blackbox.el
%{_datadir}/emacs/%{version}/lisp/play/cookie1.el
%{_datadir}/emacs/%{version}/lisp/play/[^(bruce)]*.el
%{_datadir}/emacs/%{version}/lisp/term/*.el
%{_datadir}/emacs/%{version}/lisp/emulation/*.el
%{_datadir}/emacs/%{version}/lisp/international/[a-k]*.el
%{_datadir}/emacs/%{version}/lisp/international/[o-z]*.el
%{_datadir}/emacs/%{version}/lisp/international/mule-cmds.el
%{_datadir}/emacs/%{version}/lisp/international/mule-diag.el
%{_datadir}/emacs/%{version}/lisp/international/mule-util.el
%{_datadir}/emacs/%{version}/lisp/international/mule.el
%{_datadir}/emacs/%{version}/lisp/calendar/*.el
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/*.el
%{_datadir}/emacs/%{version}/lisp/textmodes/*.el
%{_datadir}/emacs/%{version}/lisp/progmodes/*.el

%files leim
%defattr(644,root,root,755)
%dir %{_datadir}/emacs/%{version}/leim
%dir %{_datadir}/emacs/%{version}/leim/skk
%dir %{_datadir}/emacs/%{version}/leim/quail
%{_datadir}/emacs/%{version}/leim/leim-list.el
%{_datadir}/emacs/%{version}/leim/quail/*.elc
%{_datadir}/emacs/%{version}/leim/skk/*.elc

%files leim-el
%defattr(644,root,root,755)
%{_datadir}/emacs/%{version}/leim/quail/*.el
%{_datadir}/emacs/%{version}/leim/skk/*.el

%files nox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/emacs-nox
