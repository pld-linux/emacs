Summary:	The libraries needed to run the GNU Emacs text editor.
Name:		emacs
Version:	20.3
Release:	16
Copyright:	GPL
Group:		Applications/Editors
Source0:	ftp://ftp.gnu.org/pub/gnu/emacs-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/pub/gnu/leim-%{version}.tar.gz
Source2:	emacs.wmconfig
Source3:	mh-utils.elc
Patch0:		emacs-20.3-gnu.patch
Patch1:		emacs-20.2-xaw3d.patch
Patch2:		emacs-20.2-gctags.patch
# patch4 (signal patch) not needed for emacs > 20.2
Patch4:		emacs-20.2-signal.patch
Patch5:		emacs-20.3-tmprace.patch
Patch6:		emacs-20.3-ufix.patch
Patch7:		emacs-armconfig.patch
Patch8:		emacs-20.3-linkscr.patch
Patch9:		emacs-20.3-nmhlocation.patch
Patch10:	emacs-20.3-dxpc.patch
Buildroot:	/tmp/%{name}-%{version}-root
#
# more info on multibyte support: http://sourcery.naggum.no/emacs/
#

%description
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news and more without
leaving the editor.

This package includes the libraries you need to run the Emacs editor, so
you need to install this package if you intend to use Emacs.  You also
need to install the actual Emacs program package (emacs-nox or emacs-X11).
Install emacs-nox if you are not going to use the X Window System; install
emacs-X11 if you will be using X.

%package el
Summary:	The sources for elisp programs included with Emacs.
Group:		Applications/Editors
Requires:	%{name} = %{version}

%description el
Emacs-el contains the emacs-elisp sources for many of the elisp
programs included with the main Emacs text editor package.

You need to install emacs-el only if you intend to modify any of the
Emacs packages or see some elisp examples.

%package leim
Summary:	Emacs Lisp code for input methods for internationalization.
Group:		Applications/Editors
Requires:	%{name} = %{version}

%description leim
The Emacs Lisp code for input methods for various international
character scripts.

%package nox
Summary:	The Emacs text editor without support for the X Window System.
Group:		Applications/Editors
Requires:	%{name} = %{version}

%description nox
Emacs-nox is the Emacs text editor program without support for
the X Window System.

You need to install this package only if you plan on exclusively using
Emacs without the X Window System (emacs-X11 will work both in X and out
of X, but emacs-nox will only work outside of X).  You'll also need to
install the emacs package in order to run Emacs.

%package X11
Summary:	The Emacs text editor for the X Window System.
Group:		Applications/Editors
Requires:	%{name} = %{version}

%description X11
Emacs-X11 includes the Emacs text editor program for use with the
X Window System (it provides support for the mouse and other GUI
elements). Emacs-X11 will also run Emacs outside of X, but it has
a larger memory footprint than the 'non-X' Emacs package
(emacs-nox).

Install emacs-X11 if you're going to use Emacs with the X Window System.
You should also install emacs-X11 if you're going to run Emacs both
with and without X (it will work fine both ways). You'll also need to
install the emacs package in order to run Emacs.

%prep
%setup -q -b 1
cp -f $RPM_SOURCE_DIR/mh-utils.elc lisp/mail
%patch0 -p1
%patch1 -p1
%patch2 -p1
# patch4 (signal patch) not needed for emacs > 20.2
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p2

# clean out remnants of patching
find . -name "*.orig" -exec rm -f {} \;

%build
PUREDEF=""
XPUREDEF=""
libtoolize --force --copy
CONFOPTS="--prefix=%{_prefix} --libexecdir=%{_libdir} --sharedstatedir=/var --with-gcc --with-pop"

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
	sharedstatedir=$RPM_BUILD_ROOT/var

rm -f $RPM_BUILD_ROOT/usr/info/dir
gzip -9nf $RPM_BUILD_ROOT/usr/info/*
install -m755 build-nox/src/emacs $RPM_BUILD_ROOT/usr/bin/emacs-nox

# For some reason, when emacs is stripped on the Alpha, it dumps core
# Lucky for us it started doing this on the Intel as well. Yeah.
#strip $RPM_BUILD_ROOT/usr/bin/* ||:
for I in cvtmail digest-doc emacsserver fakemail hexl movemail profile \
	sorted-doc timer wakeup yow; do
	strip $RPM_BUILD_ROOT/usr/lib/emacs/$RPM_PACKAGE_VERSION/$ARCHDIR/$I||:
done

chown root.mail $RPM_BUILD_ROOT/usr/lib/emacs/$RPM_PACKAGE_VERSION/$ARCHDIR/movemail
chmod 2755 $RPM_BUILD_ROOT/usr/lib/emacs/$RPM_PACKAGE_VERSION/$ARCHDIR/movemail

mkdir -p $RPM_BUILD_ROOT/usr/lib/emacs/site-lisp

mv $RPM_BUILD_ROOT/usr/man/man1/ctags.1 $RPM_BUILD_ROOT/usr/man/man1/gctags.1
mv $RPM_BUILD_ROOT/usr/bin/ctags $RPM_BUILD_ROOT/usr/bin/gctags

# wmconfig file
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m 0644 $RPM_SOURCE_DIR/emacs.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/emacs

#
# create file lists
#

find $RPM_BUILD_ROOT/usr/share/emacs/%{PACKAGE_VERSION}/lisp \
  -name '*.elc' -print | sed "s^$RPM_BUILD_ROOT^^" > elc-filelist
find $RPM_BUILD_ROOT/usr/lib/emacs/%{PACKAGE_VERSION} -type f | \
    sed "s^$RPM_BUILD_ROOT^^" | grep -v movemail >> elc-filelist

find $RPM_BUILD_ROOT/usr/share/emacs/%{PACKAGE_VERSION}/leim \
  -name '*.elc' -print | sed "s^$RPM_BUILD_ROOT^^" > leim-filelist

#
# be sure to exclude some files which are need in core package
#
find $RPM_BUILD_ROOT/usr/share/emacs/%{PACKAGE_VERSION}/lisp \
  -name '*.el' -print | sed "s^$RPM_BUILD_ROOT^^" |\
  grep -v "international\/latin-[0-9]*.el" > el-filelist

find $RPM_BUILD_ROOT/usr/share/emacs/%{PACKAGE_VERSION}/leim \
  -name '*.el' -print | sed "s^$RPM_BUILD_ROOT^^" |\
  grep -v "leim\/leim-list.el" >> el-filelist

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf build-nox
rm -rf build-withx

%post
/sbin/install-info /usr/info/ccmode.gz /usr/info/dir --entry="* CC mode: (ccmode).    The GNU Emacs mode for editing C, C++, Objective-C and Java code." --section="Emacs"
/sbin/install-info /usr/info/ediff.gz /usr/info/dir --entry="* Ediff: (ediff).       A comprehensive visual interface to diff & patch." --section="Emacs"
/sbin/install-info /usr/info/dired-x.gz /usr/info/dir --entry="* Dired-X: (dired-x).   Dired Extra Features." --section="Emacs"
/sbin/install-info /usr/info/sc.gz /usr/info/dir --entry="* SC: (sc).             Supercite lets you cite parts of messages you're replying to, in flexible ways." --section="Emacs"
/sbin/install-info /usr/info/cl.gz /usr/info/dir --entry="* CL: (cl).             Partial Common Lisp support for Emacs Lisp." --section="Emacs"
/sbin/install-info /usr/info/mh-e.gz /usr/info/dir --entry="* MH-E: (mh-e).         Emacs interface to the MH mail system." --section="Emacs"
/sbin/install-info /usr/info/message.gz /usr/info/dir --entry="* Message: (message).   Mail and news composition mode that goes with Gnus." --section="Emacs"
/sbin/install-info /usr/info/gnus.gz /usr/info/dir --entry="* Gnus: (gnus).         The news reader Gnus." --section="Emacs"
/sbin/install-info /usr/info/forms.gz /usr/info/dir --entry="* Forms: (forms).       Emacs package for editing data bases by filling in forms." --section="Emacs"
/sbin/install-info /usr/info/viper.gz /usr/info/dir --entry="* VIPER: (viper).       The new VI-emulation mode in Emacs-19.29." --section="Emacs"
/sbin/install-info /usr/info/vip.gz /usr/info/dir --entry="* VIP: (vip).           A VI-emulation for Emacs." --section="Emacs"
/sbin/install-info /usr/info/emacs.gz /usr/info/dir --entry="* Emacs: (emacs).       The extensible self-documenting text editor." --section="Emacs"
/sbin/install-info /usr/info/info.gz /usr/info/dir --entry="* Info: (info).         Documentation browsing system." --section="Emacs"
/sbin/install-info /usr/info/reftex.gz /usr/info/dir --entry="* RefTeX: (reftex).         Manage labels, references, and citations with Emacs." --section="Emacs"
/sbin/install-info /usr/info/widget.gz /usr/info/dir --entry="* Widget: (widget).         Emacs widget library." --section="Emacs"
/sbin/install-info /usr/info/customize.gz /usr/info/dir --entry="* Customize: (customize).         Declaring customization items." --section="Emacs"

%preun
if [ "$1" = 0 ]; then
/sbin/install-info --delete /usr/info/ccmode.gz /usr/info/dir --entry="* CC mode: (ccmode).    The GNU Emacs mode for editing C, C++, Objective-C and Java code." --section="Emacs"
/sbin/install-info --delete /usr/info/ediff.gz /usr/info/dir --entry="* Ediff: (ediff).       A comprehensive visual interface to diff & patch." --section="Emacs"
/sbin/install-info --delete /usr/info/dired-x.gz /usr/info/dir --entry="* Dired-X: (dired-x).   Dired Extra Features." --section="Emacs"
/sbin/install-info --delete /usr/info/sc.gz /usr/info/dir --entry="* SC: (sc).             Supercite lets you cite parts of messages you're replying to, in flexible ways." --section="Emacs"
/sbin/install-info --delete /usr/info/cl.gz /usr/info/dir --entry="* CL: (cl).             Partial Common Lisp support for Emacs Lisp." --section="Emacs"
/sbin/install-info --delete /usr/info/mh-e.gz /usr/info/dir --entry="* MH-E: (mh-e).         Emacs interface to the MH mail system." --section="Emacs"
/sbin/install-info --delete /usr/info/message.gz /usr/info/dir --entry="* Message: (message).   Mail and news composition mode that goes with Gnus." --section="Emacs"
/sbin/install-info --delete /usr/info/gnus.gz /usr/info/dir --entry="* Gnus: (gnus).         The news reader Gnus." --section="Emacs"
/sbin/install-info --delete /usr/info/forms.gz /usr/info/dir --entry="* Forms: (forms).       Emacs package for editing data bases by filling in forms." --section="Emacs"
/sbin/install-info --delete /usr/info/viper.gz /usr/info/dir --entry="* VIPER: (viper).       The new VI-emulation mode in Emacs-19.29." --section="Emacs"
/sbin/install-info --delete /usr/info/vip.gz /usr/info/dir --entry="* VIP: (vip).           A VI-emulation for Emacs." --section="Emacs"
/sbin/install-info --delete /usr/info/emacs.gz /usr/info/dir --entry="* Emacs: (emacs).       The extensible self-documenting text editor." --section="Emacs"
/sbin/install-info --delete /usr/info/info.gz /usr/info/dir --entry="* Info: (info).         Documentation browsing system." --section="Emacs"
/sbin/install-info /usr/info/reftex.gz /usr/info/dir --entry="* RefTeX: (reftex).         Manage labels, references, and citations with Emacs." --section="Emacs"
/sbin/install-info --delete /usr/info/widget.gz /usr/info/dir --entry="* Widget: (widget).         Emacs widget library." --section="Emacs"
/sbin/install-info --delete /usr/info/customize.gz /usr/info/dir --entry="* Customize: (customize).         Declaring customization items." --section="Emacs"
fi

%files -f elc-filelist
%defattr(-,root,root)
%doc etc/NEWS BUGS README etc/FAQ
/usr/bin/b2m
/usr/bin/emacsclient
/usr/bin/etags
/usr/bin/gctags
/usr/bin/rcs-checkin
/usr/man/*/*
/usr/info/*
#%dir /var/lock/emacs

%dir /usr/lib/emacs
%attr(2755,root,mail) /usr/lib/emacs/%{PACKAGE_VERSION}/%{_target_cpu}-redhat-linux/movemail
%dir /usr/lib/emacs/site-lisp

%dir /usr/share/emacs/site-lisp
%dir /usr/share/emacs/%{PACKAGE_VERSION}
%dir /usr/share/emacs/%{PACKAGE_VERSION}/site-lisp
%dir /usr/share/emacs/%{PACKAGE_VERSION}/leim
%dir /usr/share/emacs/%{PACKAGE_VERSION}/lisp
%dir /usr/share/emacs/%{PACKAGE_VERSION}/lisp/term
/usr/share/emacs/%{PACKAGE_VERSION}/etc

# handled by dynamically generated file lists
#/usr/share/emacs/%{PACKAGE_VERSION}/lisp/*.elc
#/usr/share/emacs/%{PACKAGE_VERSION}/lisp/*/*.elc
#/usr/share/emacs/%{PACKAGE_VERSION}/lisp/*.elc
#/usr/share/emacs/20.2/lisp/mail/*.elc

/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/README
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/AT386.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/bobcat.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/internal.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/keyswap.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/lk201.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt102.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt125.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt201.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt220.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt240.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt300.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt320.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt400.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt420.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/COPYING
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/forms-d2.dat
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/README
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/mail/blessmail.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/forms-d2.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/forms-pass.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/loaddefs.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/loadup.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/patcomp.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/paths.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/mail/sc.el
#/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term-nasty.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/version.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/subdirs.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/international/latin-1.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/international/latin-2.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/international/latin-3.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/international/latin-4.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/international/latin-5.el

%files -f el-filelist el
%defattr(-,root,root)
# handled by dynamically generated file lists
#/usr/share/emacs/%{PACKAGE_VERSION}/lisp/*.el
#/usr/share/emacs/%{PACKAGE_VERSION}/lisp/*/*.el
#/usr/share/emacs/%{PACKAGE_VERSION}/leim/*.el
#/usr/share/emacs/%{PACKAGE_VERSION}/leim/*/*.el

%files -f leim-filelist leim
%defattr(-,root,root)
/usr/share/emacs/%{PACKAGE_VERSION}/leim/leim-list.el
# handled by dynamically generated file lists
#/usr/share/emacs/%{PACKAGE_VERSION}/leim/*.elc
#/usr/share/emacs/%{PACKAGE_VERSION}/leim/*/*.elc

%files nox
%defattr(-,root,root)
/usr/bin/emacs-nox

%files X11
%defattr(-,root,root)
/usr/bin/emacs
/usr/bin/emacs-%{version}
%config(missingok) /etc/X11/wmconfig/emacs
