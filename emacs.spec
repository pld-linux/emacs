Summary:	The libraries needed to run the GNU Emacs text editor
Name:		emacs
Version:	20.4
Release:	5
License:	GPL
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	X11/Aplicações/Editores
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/pub/gnu/leim-%{version}.tar.gz
Source2:	emacs.wmconfig
Patch0:		emacs-20.2-xaw3d.patch
Patch1:		emacs-20.2-gctags.patch
Patch2:		emacs-20.3-tmprace.patch
Patch3:		emacs-20.3-linkscr.patch
Patch4:		emacs-20.4-nmhlocation.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#
# more info on multibyte support: http://sourcery.naggum.no/emacs/
#

%description
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news and more
without leaving the editor.

This package includes the libraries you need to run the Emacs editor,
so you need to install this package if you intend to use Emacs. You
also need to install the actual Emacs program package (emacs-nox or
emacs-X11). Install emacs-nox if you are not going to use the X Window
System; install emacs-X11 if you will be using X.

%description -l pl
Emacs jest potê¿nym, konfigurowalnym, samodokumentuj±cym sie edytorem
niezale¿nym od trybu pracy. Emacs zawiera wiele funkcji wspomagaj±cych
edycjê kodu, jêzyk skryptowy (elisp) oraz zdolno¶æ do czytania poczty
elektronicznej, grup dyskusyjnych itd. bez potzreby opuszczania
edytora.

Pakiet ten zawiera biblioteki niezbêdne do uruchomienia Emacsa, nale¿y
wiêc go zainstalowaæ je¶li pragnie siê u¿ywaæ Emacsa. Nale¿y równie¿
zainstalowaæ samego Emacsa (emacs-nox lub emacs-X11). Emacs-nox jest
dla osób, które nie zamierzaj± u¿ywaæ systemu X Window, za¶ emacs-x11
dla tych, którzy planuj± z niego korzystaæ.

%package el
Summary:	The sources for elisp programs included with Emacs.
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	X11/Aplicações/Editores
Requires:	%{name} = %{version}

%description el
Emacs-el contains the emacs-elisp sources for many of the elisp
programs included with the main Emacs text editor package.

You need to install emacs-el only if you intend to modify any of the
Emacs packages or see some elisp examples.

%package leim
Summary:	Emacs Lisp code for input methods for internationalization.
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	X11/Aplicações/Editores
Requires:	%{name} = %{version}

%description leim
The Emacs Lisp code for input methods for various international
character scripts.

%package leim-el
Summary:	Source code for leim.
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	X11/Aplicações/Editores
Requires:	%{name}-leim = %{version}

%description leim-el
The Emacs Lisp source code for input methods for various international
character scripts.

%package nox
Summary:	The Emacs text editor without support for the X Window System.
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	X11/Aplicações/Editores
Requires:	%{name} = %{version}

%description nox
Emacs-nox is the Emacs text editor program without support for the X
Window System.

You need to install this package only if you plan on exclusively using
Emacs without the X Window System (emacs-X11 will work both in X and
out of X, but emacs-nox will only work outside of X). You'll also need
to install the emacs package in order to run Emacs.

%package X11
Summary:	The Emacs text editor for the X Window System.
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	X11/Aplicações/Editores
Requires:	%{name} = %{version}

%description X11
Emacs-X11 includes the Emacs text editor program for use with the X
Window System (it provides support for the mouse and other GUI
elements). Emacs-X11 will also run Emacs outside of X, but it has a
larger memory footprint than the 'non-X' Emacs package (emacs-nox).

Install emacs-X11 if you're going to use Emacs with the X Window
System. You should also install emacs-X11 if you're going to run Emacs
both with and without X (it will work fine both ways). You'll also
need to install the emacs package in order to run Emacs.

%prep
%setup -q -b 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# clean out remnants of patching
find . -name "*.orig" -exec rm -f {} \;

%build
PUREDEF=""
XPUREDEF=""
libtoolize --force --copy
CONFOPTS="--prefix=%{_prefix} \
	--libexecdir=%{_libdir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--sharedstatedir=/var \
	--with-gcc \
	--with-pop"

#Build binary without X support
[ -d build-nox ] && rm -rf build-nox
mkdir build-nox && cd build-nox
CFLAGS="$RPM_OPT_FLAGS $PUREDEF" LDFLAGS=-s \
  ../configure ${CONFOPTS} --with-x=no %{_target_platform}
make
cd ..

#Build binary with X support
[ -d build-withx ] && rm -rf build-withx
mkdir build-withx && cd build-withx
CFLAGS="$RPM_OPT_FLAGS $XPUREDEF" LDFLAGS=-s \
  ../configure ${CONFOPTS} --with-x-toolkit %{_target_platform}
make 
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

ARCHDIR=%{_target_platform}
make install -C build-withx \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	libexecdir=$RPM_BUILD_ROOT%{_libdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	sharedstatedir=$RPM_BUILD_ROOT/var

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*
install -m755 build-nox/src/emacs $RPM_BUILD_ROOT%{_bindir}/emacs-nox

# For some reason, when emacs is stripped on the Alpha, it dumps core
# Lucky for us it started doing this on the Intel as well. Yeah.
#strip $RPM_BUILD_ROOT%{_bindir}/* ||:
for I in cvtmail digest-doc emacsserver fakemail hexl movemail profile \
	sorted-doc timer wakeup yow; do
	strip $RPM_BUILD_ROOT%{_libdir}/emacs/$RPM_PACKAGE_VERSION/$ARCHDIR/$I||:
done

install -d $RPM_BUILD_ROOT%{_libdir}/emacs/site-lisp

mv $RPM_BUILD_ROOT%{_mandir}/man1/ctags.1 $RPM_BUILD_ROOT%{_mandir}/man1/gctags.1
mv $RPM_BUILD_ROOT%{_bindir}/ctags $RPM_BUILD_ROOT%{_bindir}/gctags

# wmconfig file
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/wmconfig/emacs

gzip -9nf etc/NEWS BUGS README etc/FAQ \
	$RPM_BUILD_ROOT%{_mandir}/man*/*

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf build-nox
rm -rf build-withx

%post
[ -x /usr/sbin/fix-info-dir ] && /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ -x /usr/sbin/fix-info-dir ] && /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc {etc/NEWS,BUGS,README,etc/FAQ}.gz
%dir %{_libdir}/emacs
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%dir %{_datadir}/emacs/%{version}
%dir %{_datadir}/emacs/%{version}/etc
%dir %{_datadir}/emacs/%{version}/lisp
%dir %{_datadir}/emacs/%{version}/site-lisp
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
#%dir /var/lock/emacs
%attr(755,root,root) %{_bindir}/b2m
%attr(755,root,root) %{_bindir}/emacsclient
%attr(755,root,root) %{_bindir}/etags
%attr(755,root,root) %{_bindir}/gctags
%attr(755,root,root) %{_bindir}/rcs-checkin
%attr(2755,root,mail) %{_libdir}/emacs/%{version}/%{_target_cpu}-*/movemail
%attr(755,root,root) %{_libdir}/emacs/%{version}/%{_target_cpu}-*/cvtmail
%attr(755,root,root) %{_libdir}/emacs/%{version}/%{_target_cpu}-*/digest-doc
%attr(755,root,root) %{_libdir}/emacs/%{version}/%{_target_cpu}-*/emacsserver
%attr(755,root,root) %{_libdir}/emacs/%{version}/%{_target_cpu}-*/fakemail
%attr(755,root,root) %{_libdir}/emacs/%{version}/%{_target_cpu}-*/hexl
%attr(755,root,root) %{_libdir}/emacs/%{version}/%{_target_cpu}-*/profile
%attr(755,root,root) %{_libdir}/emacs/%{version}/%{_target_cpu}-*/rcs2log
%attr(755,root,root) %{_libdir}/emacs/%{version}/%{_target_cpu}-*/sorted-doc
%attr(755,root,root) %{_libdir}/emacs/%{version}/%{_target_cpu}-*/vcdiff
%attr(755,root,root) %{_libdir}/emacs/%{version}/%{_target_cpu}-*/yow
%{_libdir}/emacs/%{version}/%{_target_cpu}-*/fns-20.4.1.el
%{_datadir}/emacs/%{version}/etc/*
%{_datadir}/emacs/site-lisp/*
%{_datadir}/emacs/%{version}/site-lisp/*
%{_datadir}/emacs/%{version}/lisp/COPYING
%{_datadir}/emacs/%{version}/lisp/README
%{_datadir}/emacs/%{version}/lisp/forms-d2.dat
%{_datadir}/emacs/%{version}/lisp/forms-d2.el
%{_datadir}/emacs/%{version}/lisp/forms-pass.el
%{_datadir}/emacs/%{version}/lisp/loaddefs.el
%{_datadir}/emacs/%{version}/lisp/loadup.el
%{_datadir}/emacs/%{version}/lisp/patcomp.el
%{_datadir}/emacs/%{version}/lisp/paths.el
%{_datadir}/emacs/%{version}/lisp/version.el
%{_datadir}/emacs/%{version}/lisp/subdirs.el
%{_datadir}/emacs/%{version}/lisp/*.elc
%{_datadir}/emacs/%{version}/lisp/calendar/*.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/*.elc
%{_datadir}/emacs/%{version}/lisp/emulation/*.elc
%{_datadir}/emacs/%{version}/lisp/gnus/*.elc
%{_datadir}/emacs/%{version}/lisp/international/latin-1.el
%{_datadir}/emacs/%{version}/lisp/international/latin-2.el
%{_datadir}/emacs/%{version}/lisp/international/latin-3.el
%{_datadir}/emacs/%{version}/lisp/international/latin-4.el
%{_datadir}/emacs/%{version}/lisp/international/latin-5.el
%{_datadir}/emacs/%{version}/lisp/international/*.elc
%{_datadir}/emacs/%{version}/lisp/language/*.elc
%{_datadir}/emacs/%{version}/lisp/mail/blessmail.el
%{_datadir}/emacs/%{version}/lisp/mail/sc.el
%{_datadir}/emacs/%{version}/lisp/mail/*.elc
%{_datadir}/emacs/%{version}/lisp/play/*.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/*.elc
%{_datadir}/emacs/%{version}/lisp/term/README
%{_datadir}/emacs/%{version}/lisp/term/AT386.el
%{_datadir}/emacs/%{version}/lisp/term/bobcat.el
%{_datadir}/emacs/%{version}/lisp/term/internal.el
%{_datadir}/emacs/%{version}/lisp/term/iris-ansi.el
%{_datadir}/emacs/%{version}/lisp/term/keyswap.el
%{_datadir}/emacs/%{version}/lisp/term/linux.el
%{_datadir}/emacs/%{version}/lisp/term/lk201.el
%{_datadir}/emacs/%{version}/lisp/term/vt*.el
%{_datadir}/emacs/%{version}/lisp/term/*.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/*.elc
%{_mandir}/man*/*
%{_infodir}/*

%files el
%defattr(644,root,root,755)
%{_datadir}/emacs/%{version}/lisp/*.el
%{_datadir}/emacs/%{version}/lisp/calendar/*.el
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/*.el
%{_datadir}/emacs/%{version}/lisp/emulation/*.el
%{_datadir}/emacs/%{version}/lisp/gnus/*.el
%{_datadir}/emacs/%{version}/lisp/international/[a-k]*.el
%{_datadir}/emacs/%{version}/lisp/international/[m-z]*.el
%{_datadir}/emacs/%{version}/lisp/language/*.el
%{_datadir}/emacs/%{version}/lisp/mail/[e-r]*.el
%{_datadir}/emacs/%{version}/lisp/mail/sendmail.el
%{_datadir}/emacs/%{version}/lisp/mail/smtpmail.el
%{_datadir}/emacs/%{version}/lisp/mail/supercite.el
%{_datadir}/emacs/%{version}/lisp/mail/[u-v]*.el
%{_datadir}/emacs/%{version}/lisp/play/*.el
%{_datadir}/emacs/%{version}/lisp/progmodes/*.el
%{_datadir}/emacs/%{version}/lisp/term/apollo.el
%{_datadir}/emacs/%{version}/lisp/term/bg-mouse.el
%{_datadir}/emacs/%{version}/lisp/term/[n-t]*.el
%{_datadir}/emacs/%{version}/lisp/term/[w-x]*.el
%{_datadir}/emacs/%{version}/lisp/textmodes/*.el

%files leim
%defattr(644,root,root,755)
%dir %{_datadir}/emacs/%{version}/leim
%dir %{_datadir}/emacs/%{version}/leim/quail
%dir %{_datadir}/emacs/%{version}/leim/skk
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

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/emacs
%attr(755,root,root) %{_bindir}/emacs-%{version}
%config(missingok) /etc/X11/wmconfig/emacs
