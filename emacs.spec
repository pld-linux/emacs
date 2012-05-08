# TODO:
# - package cedit lisp files files
# - package new (non gtk) desktop file?
# - package ctags/etags in subpackage?
#
# Conditional build:
%bcond_without	athena		# don't build athena version
%bcond_without	gtk		# don't build GTK+2 version
%bcond_without	motif		# don't build motif version
%bcond_without	nox		# don't build nox version
%bcond_with	bootstrap	# build bootsrtap version
#
Summary:	The Emacs text editor for the X Window System
Summary(de.UTF-8):	GNU Emacs
Summary(es.UTF-8):	GNU Emacs
Summary(fr.UTF-8):	GNU Emacs
Summary(pl.UTF-8):	GNU Emacs - edytor tekstu dla systemu X Window
Summary(pt_BR.UTF-8):	GNU Emacs
Summary(tr.UTF-8):	GNU Emacs
Name:		emacs
%define	ver	23.4
Version:	%{ver}
Release:	0.1
License:	GPL v3+
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.gnu.org/pub/gnu/emacs/%{name}-%{version}.tar.bz2
# Source0-md5:	070c68ad8e3c31fb3cb2414feaf5e6f0
Source1:	%{name}-dot%{name}
Source2:	%{name}-site-start.el
Source3:	%{name}.png
Source4:	%{name}-tuareg.el
Source5:	%{name}-nemerle.el
Source6:	%{name}-athena.desktop
Source7:	%{name}-gtk.desktop
Source8:	%{name}-motif.desktop
Source9:	%{name}-nox.desktop
Patch0:		%{name}-fontconfig.patch
Patch1:		%{name}-xgselect_init.patch
URL:		http://www.gnu.org/software/emacs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	freetype-devel
%{?with_gtk:BuildRequires:	gtk+2-devel}
BuildRequires:	libdnet-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	giflib-devel
BuildRequires:	ncurses-devel
%{?with_motif:BuildRequires:	openmotif-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
BuildRequires:	xorg-lib-libX11-devel
%{?with_athena:BuildRequires:	xorg-lib-libXaw-devel}
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
Requires:	%{name}-common = %{version}-%{release}
Requires:	ctags
Suggests:	emacsen-gnus-pkg-emacs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Emacs-X11 includes the Emacs text editor program for use with the X
Window System (it provides support for the mouse and other GUI
elements). Emacs-X11 will also run Emacs outside of X, but it has a
larger memory footprint than the 'non-X' Emacs package (emacs-nox).

Install emacs-X11 if you're going to use Emacs with the X Window
System. You should also install emacs-X11 if you're going to run Emacs
both with and without X (it will work fine both ways). You'll also
need to install the emacs-common package in order to run Emacs.

%description -l de.UTF-8
Emacs ist der erweiterbare, veränderbare, selbst-dokumentierende
Echtzeit-Editor. Emacs enthält spezielle Modi zum Bearbeiten von Code,
eine Script-Sprache (elisp) und Pakete für Mail, News und vieles mehr,
alles im Editor.

Dieses Paket enthält die zum Ausführen des emacs-Editors notwendig
sind. Das eigentliche Programm ist im Paket 'emacs-nox' bzw.
'emacs-X11' enthalten, je nachdem, ob Sie X-Window verwenden oder
nicht.

%description -l es.UTF-8
Emacs es un editor común, que se puede personalizar, y muestra los
propios documentos en tiempo real. Emacs posee un modo de código
especial para edición, un lenguaje script (elisp), y viene con varios
paquetes para mail, news, y más cosas, todo en tu editor. Este paquete
incluye las bibliotecas necesarias para ejecutar el editor emacs - el
programa actual puede ser encontrado en los paquetes emacs-nox o
emacs-X11, dependiendo de que uses o no el X Window.

%description -l pl.UTF-8
Emacs-X11 zawiera edytor tekstu Emacs do użytku z X Window System (ma
wsparcie dla myszy i innych elementów interfejsu graficznego).
Emacs-X11 może działać także bez X, ale wymaga więcej pamięci niż
wersja nie-X Emacsa (emacs-nox).

%description -l pt_BR.UTF-8
Emacs é um editor comum, personalizável, e mostra os próprios
documentos em tempo real. Emacs possui um modo de código especial para
edição, uma linguagem script (elisp), e vem com vários pacotes para
mail, news, e mais, tudo no seu editor. Este pacote inclui as
bibliotecas necessárias para rodar o editor emacs - o programa atual
pode ser achado nos pacotes emacs-nox ou emacs-X11, dependendo se você
usa ou não X Window.

%description -l tr.UTF-8
Emacs, son derece gelişmiş bir metin düzenleyicisidir. Bir çok
geliştirme ortamında kullanılmak üzere ayarlanabilir (C, Java, VHDL
gibi). E-posta okuyabilmek, haber gruplarına erişmek gibi birçok
değişik amaç için kullanılabilecek ek yazılımlarla yetenekli bir
çalışma ortamı sağlar. Bu paket emacs çalıştırmak için gereken
kütüphaneleri içerir. Asıl program kullandığınız ortama göre emacs-nox
veya emacs-X11 paketinde yer alır.

%package el
Summary:	The sources for elisp programs included with Emacs
Summary(de.UTF-8):	El Quelldateien - zum Betrieb von Emacs nicht erforderlich
Summary(es.UTF-8):	Fuentes .el -- no son necesarios para ejecutar Emacs
Summary(fr.UTF-8):	Fichiers sources .el - non nécessaires pour exécuter Emacs
Summary(pl.UTF-8):	Źródła programów w elispie dołączonych do Emacsa
Summary(pt_BR.UTF-8):	Fontes .el -- não são necessários para rodar o Emacs
Summary(tr.UTF-8):	Lisp kaynak dosyaları -- Emacs çalıştırmak için gerekmez
Group:		Applications/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}

%description el
Emacs-el contains the emacs-elisp sources for many of the elisp
programs included with the main Emacs text editor package.

You need to install emacs-el only if you intend to modify any of the
Emacs packages or see some elisp examples.

%description el -l es.UTF-8
Este paquete contiene los fuentes emacs-lisp para muchos de los
programas elisp incluido en el programa principal del paquete emacs.
Tu no necesitas de este paquete a menos que quieras modificarlos o
mirar algunos ejemplos de programas elisp.

%description el -l fr.UTF-8
Ce paquetage contient les sources emacs-lisp de la plupart des
programmes elisp inclus avec le paquetage emacs principal. Vous n'avez
pas besoin de ce paquetage sauf si vous voulez modifier ces paquetages
ou voir quelques exemples elisp.

%description el -l pl.UTF-8
Emacs-el zawiera źródła w emacs-elispie wielu programów dołączonych do
głównego pakietu edytora Emacs. Ten pakiet jest potrzebny tylko do
modyfikowania elementów Emacsa lub obejrzenia przykładów w elispie.

%description el -l pt_BR.UTF-8
Este pacote contém os fontes emacs-lisp para muitos dos programas
elisp incluído com o programa principal do pacote emacs. Você não
necessita deste pacote a menos que você queira modificar estes pacotes
ou ver alguns exemplos de programas elisp.

%description el -l tr.UTF-8
Bu paket, ana emacs paketinde yer alan çoğu programın lisp kaynak
kodlarını içerir. Bu programları değiştirmeyi düşünmüyorsanız gerek
duymayacaksınız.

%package leim
Summary:	Emacs Lisp code for input methods for international characters
Summary(es.UTF-8):	Código Lisp para internacionalización en Emacs
Summary(pl.UTF-8):	Kod w Emacs Lispie do wprowadzania znaków narodowych
Summary(pt_BR.UTF-8):	Código Lisp para para internacionalização no Emacs
Group:		Applications/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}

%description leim
The emacs-leim package contains Emacs Lisp code for input methods for
various international character scripts. Basically, the Lisp code
provided by this package describes the consecutive keystrokes that a
user must press in order to input a particular character in a
non-English character set. Input methods for many different language's
character sets are included in this package.

%description leim -l es.UTF-8
Código Lisp para internacionalización en Emacs.

%description leim -l pl.UTF-8
Pakiet emacs-leim zawiera kod w Emacs Lispie do wprowadzania różnych
narodowych znaków. Kod zawarty w tym pakiecie opisuje sekwencje
klawiszy, które użytkownik musi nacisnąć, by uzyskać dany znak spoza
zestawu angielskiego. Pakiet zawiera sposoby wprowadzania znaków w
wielu różnych językach.

%description leim -l pt_BR.UTF-8
Código Lisp para para internacionalização no Emacs.

%package leim-el
Summary:	Emacs Lisp source code for input methods for international characters
Summary(pl.UTF-8):	Kod źródłowy w Emacs Lispie do wprowadzania znaków narodowych
Group:		Applications/Editors/Emacs
Requires:	%{name}-leim = %{version}-%{release}

%description leim-el
Emacs Lisp source code for input methods for international characters.

%description leim-el -l pl.UTF-8
Kod źródłowy w Emacs Lispie do wprowadzania znaków narodowych.

%package nox
Summary:	The Emacs text editor without support for the X Window System
Summary(de.UTF-8):	emacs-nox - keine X-Libraries erforderlich
Summary(es.UTF-8):	emacs-nox - Emacs sin necesidad de bibliotecas X
Summary(fr.UTF-8):	emacs-nox - les bibliothèques X ne sont pas nécessaires
Summary(pl.UTF-8):	emacs-nox - edytor tekstu Emacs bez wsparcia dla X Window System
Summary(pt_BR.UTF-8):	emacs-nox - Emacs sem precisar de bibliotecas X
Summary(tr.UTF-8):	X gerektirmeyen emacs paketi
Group:		Applications/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}

%description nox
Emacs-nox is the Emacs text editor program without support for the X
Window System.

You need to install this package only if you plan on exclusively using
Emacs without the X Window System (emacs-X11 will work both in X and
out of X, but emacs-nox will only work outside of X). You'll also need
to install the emacs-common package in order to run Emacs.

%description nox -l de.UTF-8
Dieses Paket enthält eine Binärversion von emacs ohne X-Window-
Unterstützung. Das emacs-Binärprogramm im emacs-Hauptpaket
funktioniert zwar einwandfrei außerhalb von X-Window (z.B. auf der
Konsole), die Version in diesem Paket hat jedoch ein kleineres
Speicherabbild.

%description nox -l es.UTF-8
Este paquete contiene un binario emacs sin soporte al X Window. Aunque
el binario emacs, en el paquete principal, funcione bien fuera del X
Window (en la consola, por ejemplo) lo que se encuentra en este
paquete utiliza menos memoria.

%description nox -l fr.UTF-8
Ce paquetage contient un binaire emacs construit sans gestion X
Window. Bien que le binaire emacs du paquetage emacs principal
fonctionne bien sans X Window (sur un terminal, par exemple), celui-ci
à une image mémoire plus petite.

%description nox -l pl.UTF-8
Emacs-nox to edytor tekstu Emacs bez wsparcia dla X Window System.

%description nox -l pt_BR.UTF-8
Este pacote contém um binário emacs sem suporte ao X Window. Embora o
binário emacs no pacote principal funcione bem fora do X Window (na
console por exemplo) o que está neste pacote utiliza menos memória.

%description nox -l tr.UTF-8
Bu paket içinde yer alan emacs programı, X11 desteği içermez ve
çalışmak için daha az belleğe gereksinim duyar.

%package athena
Summary:	The Emacs text editor for X Window System (Athena toolkit version)
Summary(pl.UTF-8):	Emacs - edytor tekstu Emacs dla X Window System (wersja Athena)
Group:		Applications/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}

%description athena
The Emacs text editor for X Window System (Athena toolkit version).

%description athena -l pl.UTF-8
Emacs - edytor tekstu Emacs dla X Window System (wersja Athena).

%package gtk
Summary:	The Emacs text editor for X Window System (GTK+2 toolkit version)
Summary(pl.UTF-8):	Emacs - edytor tekstu Emacs dla X Window System (wersja GTK+2)
Group:		Applications/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}

%description gtk
The Emacs text editor for X Window System (GTK+2 toolkit version).

%description gtk -l pl.UTF-8
Emacs - edytor tekstu Emacs dla X Window System (wersja GTK+2).

%package motif
Summary:	The Emacs text editor for X Window System (Motif toolkit version)
Summary(pl.UTF-8):	Emacs - edytor tekstu Emacs dla X Window System (wersja Motif)
Group:		Applications/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}

%description motif
The Emacs text editor for X Window System (Motif toolkit version).

%description motif -l pl.UTF-8
Emacs - edytor tekstu Emacs dla X Window System (wersja Motif).

%package common
Summary:	The libraries needed to run the GNU Emacs text editor
Summary(pl.UTF-8):	Biblioteki potrzebne do uruchomienia edytora tekstu GNU Emacs
Group:		Applications/Editors/Emacs
Requires:	emacscommon

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

%description common -l pl.UTF-8
Emacs jest konfigurowalnym, samo-udokumentowanym edytorem tekstu o
dużych możliwościach. Zawiera ułatwienia do pisania kodu, język
skryptowy (elisp), daje możliwość czytania poczty, newsów i wiele
innych rzeczy bez opuszczania edytora.

Ten pakiet zawiera biblioteki potrzebne do uruchomienia Emacsa. Oprócz
tego pakietu potrzebny jest jeszcze właściwy program (emacs-nox lub
emacs). Zainstaluj emacs-nox jeżeli nie zamierzasz używasz Emacsa pod
X Window System; zainstaluj emacs jeżeli używasz X.

%package extras
Summary:	Files which conflict with XEmacs
Summary(pl.UTF-8):	Wspólne pliki XEmacsa i GNU Emacsa
Group:		Applications/Editors/Emacs
Provides:	emacscommon
Obsoletes:	emacscommon

%description extras
These files are common between GNU Emacs and XEmacs.

%description extras -l pl.UTF-8
Są to wspólne pliki GNU Emacs i XEmacs.

%package gnus
Summary:	Gnus is flexible message reader under Emacs
Summary(pl.UTF-8):	Gnus jest czytnikiem grup dyskusyjnych pod Emacsa
Group:		Applications/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}

%description gnus
Gnus is flexible message reader under Emacs.

%description gnus -l pl.UTF-8
Gnus jest czytnikiem grup dyskusyjnych pod Emacsa.

%package gnus-el
Summary:	Emacs Lisp source code for Gnus
Summary(pl.UTF-8):	Kod źródłowy Gnusa w Emacs Lispie
Group:		Applications/Editors/Emacs
Requires:	%{name}-gnus = %{version}-%{release}

%description gnus-el
Emacs Lisp source code for Gnus.

%description gnus-el -l pl.UTF-8
Kod źródłowy Gnusa w Emacs Lispie.

%prep
#
%if %{with gtk}
%define default_emacs gtk
%else
%if %{with motif}
%define default_emacs motif
%else
%if %{with athena}
%define default_emacs athena
%else
%if %{with nox}
%define default_emacs nox
%else
echo "ERROR: building Emacs with passed conditionals is impossible."
exit 1
%endif
%endif
%endif
%endif

%setup -q -n %{name}-%{ver}
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* .
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}

%define bootstrap 0

%if %{with athena}
echo "Building emacs athena binary ..."
rm -rf build-athena
mkdir build-athena && cd build-athena
../%configure \
	--with-crt-dir=%{_libdir} \
	--with-pop \
	--with-xpm \
	--with-jpeg \
	--with-tiff \
	--with-gif \
	--with-png \
	--with-x-toolkit=athena \
	%{?with_bootstrap:--without-gpm}

%{__make} -j1 bootstrap
%define	bootstrap athena
cd ..
%endif

%if %{with gtk}
echo "Building emacs GTK+2 binary ..."
rm -rf build-gtk
mkdir build-gtk && cd build-gtk
../%configure \
	--with-crt-dir=%{_libdir} \
	--with-pop \
	--with-xpm \
	--with-jpeg \
	--with-tiff \
	--with-gif \
	--with-png \
	--with-x-toolkit=gtk \
	%{?with_bootstrap:--without-gpm}

%if %{?bootstrap}
%{__make}
%else
%{__make} -j1 bootstrap
%define	bootstrap gtk
%endif
cd ..
%endif

%if %{with motif}
echo "Building emacs motif binary ..."
rm -rf build-motif
mkdir build-motif && cd build-motif
../%configure \
	--with-crt-dir=%{_libdir} \
	--with-pop \
	--with-xpm \
	--with-jpeg \
	--with-tiff \
	--with-gif \
	--with-png \
	--with-x-toolkit=motif \
	%{?with_bootstrap:--without-gpm}

%if %{?bootstrap}
%{__make}
%else
%{__make} -j1 bootstrap
%define	bootstrap motif
%endif
cd ..
%endif

%if %{with nox}
echo "Building emacs binary without X support ..."
[ -d build-nox ] && rm -rf build-nox
mkdir build-nox && cd build-nox
../%configure \
	--with-crt-dir=%{_libdir} \
	--with-pop \
	--without-xpm \
	--without-jpeg \
	--without-tiff \
	--without-gif \
	--without-png \
	--with-x=no \
	%{?with_bootstrap:--without-gpm}

%if %{?bootstrap}
%{__make}
%else
%{__make} -j1 bootstrap
%define	bootstrap nox
%endif
cd ..
%endif

mv lisp/term/README README.term

%{__sed} s!@SITE_START_DIR@!%{_datadir}/emacs/site-lisp/site-start.d! \
	< %{SOURCE2} > site-start.el

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_infodir},%{_datadir}/emacs/site-lisp/site-start.d} \
	$RPM_BUILD_ROOT{%{_desktopdir},/etc/skel,%{_pixmapsdir}} \

%if %{with athena}%{with gtk}%{with motif}%{with nox}
%makeinstall -C build-%{bootstrap}
%else
echo 'ERROR: neither athena nor gtk nor motif nor nox emacs was built.' 1>&2
exit 1
%endif

for e in athena gtk motif nox ; do
	[ -d build-$e ] && install build-${e}/src/emacs $RPM_BUILD_ROOT%{_bindir}/emacs-$e
done
rm -f $RPM_BUILD_ROOT%{_bindir}/emacs
# make "default emacs" from gtk, athena, motif and non-X version
for e in gtk athena motif nox ; do
	if [ -f $RPM_BUILD_ROOT%{_bindir}/emacs-$e ] ; then
		(cd $RPM_BUILD_ROOT%{_bindir}
		 cp -pf emacs-$e emacs
		 cp -pf emacs-$e emacs-%{ver}
		)
		break;
	fi
done

install site-start.el $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
install %{SOURCE1} $RPM_BUILD_ROOT/etc/skel/.emacs
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE4} $RPM_BUILD_ROOT/%{_datadir}/emacs/%{ver}/site-lisp/tuareg.el
install %{SOURCE5} $RPM_BUILD_ROOT/%{_datadir}/emacs/%{ver}/site-lisp/nemerle.el
install %{SOURCE6} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE7} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE8} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE9} $RPM_BUILD_ROOT%{_desktopdir}

[ -d build-nox ] && install build-nox/etc/DOC-* $RPM_BUILD_ROOT%{_datadir}/emacs/%{ver}/etc

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
# ERC is in separate spec
rm -fr $RPM_BUILD_ROOT%{_datadir}/emacs/%{ver}/lisp/erc

%clean
rm -rf $RPM_BUILD_ROOT

%post	common -p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	common -p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

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
%attr(755,root,root) %{_bindir}/emacs-%{ver}
%{_desktopdir}/emacs-%{default_emacs}.desktop
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/16x16/apps/emacs*.png
%{_iconsdir}/hicolor/24x24/apps/emacs*.png
%{_iconsdir}/hicolor/32x32/apps/emacs*.png
%{_iconsdir}/hicolor/48x48/apps/emacs*.png
%{_iconsdir}/hicolor/128x128/apps/emacs*.png
%{_iconsdir}/hicolor/scalable/apps/emacs*.svg
%{_iconsdir}/hicolor/scalable/mimetypes/emacs*.svg

%files common
%defattr(644,root,root,755)
%config(noreplace) /etc/skel/.emacs
%attr(755,root,root) %{_bindir}/emacsclient
%attr(755,root,root) %{_bindir}/ebrowse
%{_mandir}/man1/ebrowse*
%{_mandir}/man1/emacs*
%{_infodir}/*

%dir %{_libdir}/emacs
%dir %{_libdir}/emacs/%{ver}
%dir %{_libdir}/emacs/%{ver}/*

%attr(2755,root,mail) %{_libdir}/emacs/%{ver}/*-linux/movemail
%attr(755,root,mail) %{_libdir}/emacs/%{ver}/*-linux/digest-doc
%attr(755,root,mail) %{_libdir}/emacs/%{ver}/*-linux/fakemail
%attr(755,root,mail) %{_libdir}/emacs/%{ver}/*-linux/hexl
%attr(755,root,mail) %{_libdir}/emacs/%{ver}/*-linux/profile
%attr(755,root,mail) %{_libdir}/emacs/%{ver}/*-linux/rcs2log
%attr(755,root,mail) %{_libdir}/emacs/%{ver}/*-linux/sorted-doc
%attr(755,root,mail) %{_libdir}/emacs/%{ver}/*-linux/vcdiff
%attr(755,root,mail) %{_libdir}/emacs/%{ver}/*-linux/update-game-score

%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/%{ver}
%dir %{_datadir}/emacs/%{ver}/site-lisp
%dir %{_datadir}/emacs/%{ver}/lisp
%dir %{_datadir}/emacs/%{ver}/leim
%dir %{_datadir}/emacs/%{ver}/lisp/calc
%dir %{_datadir}/emacs/%{ver}/lisp/calendar
%dir %{_datadir}/emacs/%{ver}/lisp/cedet
%dir %{_datadir}/emacs/%{ver}/lisp/cedet/ede
%dir %{_datadir}/emacs/%{ver}/lisp/cedet/semantic
%dir %{_datadir}/emacs/%{ver}/lisp/cedet/srecode
%dir %{_datadir}/emacs/%{ver}/lisp/emacs-lisp
%dir %{_datadir}/emacs/%{ver}/lisp/emulation
%dir %{_datadir}/emacs/%{ver}/lisp/eshell
%dir %{_datadir}/emacs/%{ver}/lisp/international
%dir %{_datadir}/emacs/%{ver}/lisp/language
%dir %{_datadir}/emacs/%{ver}/lisp/mail
%dir %{_datadir}/emacs/%{ver}/lisp/mh-e
%dir %{_datadir}/emacs/%{ver}/lisp/net
%dir %{_datadir}/emacs/%{ver}/lisp/nxml
%dir %{_datadir}/emacs/%{ver}/lisp/obsolete
%dir %{_datadir}/emacs/%{ver}/lisp/org
%dir %{_datadir}/emacs/%{ver}/lisp/play
%dir %{_datadir}/emacs/%{ver}/lisp/progmodes
%dir %{_datadir}/emacs/%{ver}/lisp/term
%dir %{_datadir}/emacs/%{ver}/lisp/textmodes
%dir %{_datadir}/emacs/%{ver}/lisp/url

%{_datadir}/emacs/site-lisp
%{_datadir}/emacs/%{ver}/etc
%{_datadir}/emacs/%{ver}/lisp/*.el
%{_datadir}/emacs/%{ver}/lisp/*.elc
%{_datadir}/emacs/%{ver}/lisp/README
%{_datadir}/emacs/%{ver}/lisp/calc/*.el
%{_datadir}/emacs/%{ver}/lisp/calc/*.elc
%{_datadir}/emacs/%{ver}/lisp/calc/README*
%{_datadir}/emacs/%{ver}/lisp/calendar/*.el
%{_datadir}/emacs/%{ver}/lisp/calendar/*.elc
%{_datadir}/emacs/%{ver}/lisp/emacs-lisp/*.el
%{_datadir}/emacs/%{ver}/lisp/emacs-lisp/*.elc
%{_datadir}/emacs/%{ver}/lisp/emulation/*.elc
%{_datadir}/emacs/%{ver}/lisp/eshell/*.elc
%{_datadir}/emacs/%{ver}/lisp/eshell/esh-groups.el
%{_datadir}/emacs/%{ver}/lisp/international/*.el
%{_datadir}/emacs/%{ver}/lisp/international/*.elc
%{_datadir}/emacs/%{ver}/lisp/international/README
%{_datadir}/emacs/%{ver}/lisp/language/*.el
%{_datadir}/emacs/%{ver}/lisp/language/*.elc
#%{_datadir}/emacs/%{ver}/lisp/cedet/*.el
%{_datadir}/emacs/%{ver}/lisp/cedet/*.elc
%{_datadir}/emacs/%{ver}/lisp/cedet/ede/*.el
%{_datadir}/emacs/%{ver}/lisp/cedet/ede/*.elc
%{_datadir}/emacs/%{ver}/lisp/cedet/semantic/*.el
%{_datadir}/emacs/%{ver}/lisp/cedet/semantic/*.elc
%{_datadir}/emacs/%{ver}/lisp/cedet/srecode/*.el
%{_datadir}/emacs/%{ver}/lisp/cedet/srecode/*.elc
%{_datadir}/emacs/%{ver}/lisp/mail/blessmail.el
%{_datadir}/emacs/%{ver}/lisp/mail/*.elc
%{_datadir}/emacs/%{ver}/lisp/mh-e/*.el
%{_datadir}/emacs/%{ver}/lisp/mh-e/*.elc
%{_datadir}/emacs/%{ver}/lisp/net/*.elc
%{_datadir}/emacs/%{ver}/lisp/nxml/*.elc
%{_datadir}/emacs/%{ver}/lisp/nxml/TODO
%{_datadir}/emacs/%{ver}/lisp/obsolete/*.elc
%{_datadir}/emacs/%{ver}/lisp/org/*.elc
%{_datadir}/emacs/%{ver}/lisp/play/bruce.el
%{_datadir}/emacs/%{ver}/lisp/play/*.elc
%{_datadir}/emacs/%{ver}/lisp/progmodes/*.elc
%{_datadir}/emacs/%{ver}/lisp/term/*.el
%{_datadir}/emacs/%{ver}/lisp/term/*.elc
%{_datadir}/emacs/%{ver}/lisp/textmodes/*.elc
%{_datadir}/emacs/%{ver}/lisp/url/*.elc

%dir /var/games/emacs
/var/games/emacs/tetris-scores
/var/games/emacs/snake-scores

%{_datadir}/emacs/%{ver}/site-lisp/subdirs.el
%{_datadir}/emacs/%{ver}/site-lisp/tuareg.el
%{_datadir}/emacs/%{ver}/site-lisp/nemerle.el

%files extras
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/b2m
%attr(755,root,root) %{_bindir}/grep-changelog
%attr(755,root,root) %{_bindir}/rcs-checkin
%{_mandir}/man1/b2m*
%{_mandir}/man1/grep-changelog*
%{_mandir}/man1/rcs-checkin*

%files el
%defattr(644,root,root,755)
%{_datadir}/emacs/%{ver}/lisp/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/calc/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/calendar/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/emacs-lisp/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/emulation/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/eshell/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/international/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/language/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/mail/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/mh-e/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/net/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/nxml/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/obsolete/*.el
%{_datadir}/emacs/%{ver}/lisp/obsolete/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/org/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/play/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/progmodes/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/term/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/textmodes/*.el.gz
%{_datadir}/emacs/%{ver}/lisp/url/*.el.gz

%files leim
%defattr(644,root,root,755)
%dir %{_datadir}/emacs/%{ver}/leim/ja-dic
%dir %{_datadir}/emacs/%{ver}/leim/quail
%{_datadir}/emacs/%{ver}/leim/leim-list.el
%{_datadir}/emacs/%{ver}/leim/quail/*.elc
%{_datadir}/emacs/%{ver}/leim/ja-dic/*.elc

%files leim-el
%defattr(644,root,root,755)
%{_datadir}/emacs/%{ver}/leim/quail/*.el.gz
%{_datadir}/emacs/%{ver}/leim/ja-dic/*.el.gz

%if %{with nox} && %{?default_emacs} != "nox"
%files nox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/emacs-nox
%{_desktopdir}/emacs-nox.desktop
%endif

%if %{with athena} && %{?default_emacs} != "athena"
%files athena
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/emacs-athena
%{_desktopdir}/emacs-athena.desktop
%endif

%if %{with gtk} && %{?default_emacs} != "gtk"
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/emacs-gtk
%{_desktopdir}/emacs-gtk.desktop
%endif

%if %{with motif} && %{?default_emacs} != "motif"
%files motif
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/emacs-motif
%{_desktopdir}/emacs-motif.desktop
%endif

%files gnus
%defattr(644,root,root,755)
%dir %{_datadir}/emacs/%{ver}/lisp/gnus
%{_datadir}/emacs/%{ver}/lisp/gnus/*.*
%exclude %{_datadir}/emacs/%{ver}/lisp/gnus/*.el.gz

%files gnus-el
%defattr(644,root,root,755)
%{_datadir}/emacs/%{ver}/lisp/gnus/*.el.gz
