#
# Conditional build:
%bcond_without	gtk
#
%define	snap	20051223
Summary:	The Emacs text editor for the X Window System
Summary(de):	GNU Emacs
Summary(es):	GNU Emacs
Summary(fr):	GNU Emacs
Summary(pl):	GNU Emacs - edytor tekstu dla systemu X Window
Summary(pt_BR):	GNU Emacs
Summary(tr):	GNU Emacs
Name:		emacs
Version:	22.0.50
Release:	0.%{snap}.1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	eabc6711e7dc55c487c87333f76f5d98
Source1:	%{name}.desktop
Source2:	%{name}-dot%{name}
Source3:	%{name}-site-start.el
Source4:	%{name}.png
Source5:	%{name}-tuareg.el
Source6:	%{name}-nemerle.el
URL:		http://www.gnu.org/software/emacs/
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
BuildRequires:	ncurses-devel
%if %{with gtk}
BuildRequires:	gtk+2-devel
%else
BuildRequires:	Xaw3d-devel >= 1.5E-3
%endif
BuildRequires:	texinfo
Requires:	ctags
Requires:	%{name}-common = %{version}-%{release}
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

%description -l de
Emacs ist der erweiterbare, veränderbare, selbst-dokumentierende
Echtzeit-Editor. Emacs enthält spezielle Modi zum Bearbeiten von Code,
eine Script-Sprache (elisp) und Pakete für Mail, News und vieles mehr,
alles im Editor.

Dieses Paket enthält die zum Ausführen des emacs-Editors notwendig
sind. Das eigentliche Programm ist im Paket 'emacs-nox' bzw.
'emacs-X11' enthalten, je nachdem, ob Sie X-Window verwenden oder
nicht.

%description -l es
Emacs es un editor común, que se puede personalizar, y muestra los
propios documentos en tiempo real. Emacs posee un modo de código
especial para edición, un lenguaje script (elisp), y viene con varios
paquetes para mail, news, y más cosas, todo en tu editor. Este paquete
incluye las bibliotecas necesarias para ejecutar el editor emacs - el
programa actual puede ser encontrado en los paquetes emacs-nox o
emacs-X11, dependiendo de que uses o no el X Window.

%description -l pl
Emacs-X11 zawiera edytor tekstu Emacs do u¿ytku z X Window System (ma
wsparcie dla myszy i innych elementów interfejsu graficznego).
Emacs-X11 mo¿e dzia³aæ tak¿e bez X, ale wymaga wiêcej pamiêci ni¿
wersja nie-X Emacsa (emacs-nox).

%description -l pt_BR
Emacs é um editor comum, personalizável, e mostra os próprios
documentos em tempo real. Emacs possui um modo de código especial para
edição, uma linguagem script (elisp), e vem com vários pacotes para
mail, news, e mais, tudo no seu editor. Este pacote inclui as
bibliotecas necessárias para rodar o editor emacs - o programa atual
pode ser achado nos pacotes emacs-nox ou emacs-X11, dependendo se você
usa ou não X Window.

%description -l tr
Emacs, son derece geliþmiþ bir metin düzenleyicisidir. Bir çok
geliþtirme ortamýnda kullanýlmak üzere ayarlanabilir (C, Java, VHDL
gibi). E-posta okuyabilmek, haber gruplarýna eriþmek gibi birçok
deðiþik amaç için kullanýlabilecek ek yazýlýmlarla yetenekli bir
çalýþma ortamý saðlar. Bu paket emacs çalýþtýrmak için gereken
kütüphaneleri içerir. Asýl program kullandýðýnýz ortama göre emacs-nox
veya emacs-X11 paketinde yer alýr.

%package el
Summary:	The sources for elisp programs included with Emacs
Summary(de):	El Quelldateien - zum Betrieb von Emacs nicht erforderlich
Summary(es):	Fuentes .el -- no son necesarios para ejecutar Emacs
Summary(fr):	Fichiers sources .el - non nécessaires pour exécuter Emacs
Summary(pl):	¬ród³a programów w elispie do³±czonych do Emacsa
Summary(pt_BR):	Fontes .el -- não são necessários para rodar o Emacs
Summary(tr):	Lisp kaynak dosyalarý -- Emacs çalýþtýrmak için gerekmez
Group:		Applications/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}

%description el
Emacs-el contains the emacs-elisp sources for many of the elisp
programs included with the main Emacs text editor package.

You need to install emacs-el only if you intend to modify any of the
Emacs packages or see some elisp examples.

%description el -l es
Este paquete contiene los fuentes emacs-lisp para muchos de los
programas elisp incluido en el programa principal del paquete emacs.
Tu no necesitas de este paquete a menos que quieras modificarlos o
mirar algunos ejemplos de programas elisp.

%description el -l fr
Ce paquetage contient les sources emacs-lisp de la plupart des
programmes elisp inclus avec le paquetage emacs principal. Vous n'avez
pas besoin de ce paquetage sauf si vous voulez modifier ces paquetages
ou voir quelques exemples elisp.

%description el -l pl
Emacs-el zawiera ¼ród³a w emacs-elispie wielu programów do³±czonych do
g³ównego pakietu edytora Emacs. Ten pakiet jest potrzebny tylko do
modyfikowania elementów Emacsa lub obejrzenia przyk³adów w elispie.

%description el -l pt_BR
Este pacote contém os fontes emacs-lisp para muitos dos programas
elisp incluído com o programa principal do pacote emacs. Você não
necessita deste pacote a menos que você queira modificar estes pacotes
ou ver alguns exemplos de programas elisp.

%description el -l tr
Bu paket, ana emacs paketinde yer alan çoðu programýn lisp kaynak
kodlarýný içerir. Bu programlarý deðiþtirmeyi düþünmüyorsanýz gerek
duymayacaksýnýz.

%package leim
Summary:	Emacs Lisp code for input methods for international characters
Summary(es):	Código Lisp para internacionalización en Emacs
Summary(pl):	Kod w Emacs Lispie do wprowadzania znaków narodowych
Summary(pt_BR):	Código Lisp para para internacionalização no Emacs
Group:		Applications/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}

%description leim
The emacs-leim package contains Emacs Lisp code for input methods for
various international character scripts. Basically, the Lisp code
provided by this package describes the consecutive keystrokes that a
user must press in order to input a particular character in a
non-English character set. Input methods for many different language's
character sets are included in this package.

%description leim -l es
Código Lisp para internacionalización en Emacs.

%description leim -l pl
Pakiet emacs-leim zawiera kod w Emacs Lispie do wprowadzania ró¿nych
narodowych znaków. Kod zawarty w tym pakiecie opisuje sekwencje
klawiszy, które u¿ytkownik musi nacisn±æ, by uzyskaæ dany znak spoza
zestawu angielskiego. Pakiet zawiera sposoby wprowadzania znaków w
wielu ró¿nych jêzykach.

%description leim -l pt_BR
Código Lisp para para internacionalização no Emacs.

%package leim-el
Summary:	Emacs Lisp source code for input methods for international characters
Summary(pl):	Kod ¼ród³owy w Emacs Lispie do wprowadzania znaków narodowych
Group:		Applications/Editors/Emacs
Requires:	%{name}-leim = %{version}-%{release}

%description leim-el
Emacs Lisp source code for input methods for international characters.

%description leim-el -l pl
Kod ¼ród³owy w Emacs Lispie do wprowadzania znaków narodowych.

%package nox
Summary:	The Emacs text editor without support for the X Window System
Summary(de):	emacs-nox - keine X-Libraries erforderlich
Summary(es):	emacs-nox - Emacs sin necesidad de bibliotecas X
Summary(fr):	emacs-nox - les bibliothèques X ne sont pas nécessaires
Summary(pl):	emacs-nox - edytor tekstu Emacs bez wsparcia dla X Window System
Summary(pt_BR):	emacs-nox - Emacs sem precisar de bibliotecas X
Summary(tr):	X gerektirmeyen emacs paketi
Group:		Applications/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}

%description nox
Emacs-nox is the Emacs text editor program without support for the X
Window System.

You need to install this package only if you plan on exclusively using
Emacs without the X Window System (emacs-X11 will work both in X and
out of X, but emacs-nox will only work outside of X). You'll also need
to install the emacs-common package in order to run Emacs.

%description nox -l de
Dieses Paket enthält eine Binärversion von emacs ohne X-Window-
Unterstützung. Das emacs-Binärprogramm im emacs-Hauptpaket
funktioniert zwar einwandfrei außerhalb von X-Window (z.B. auf der
Konsole), die Version in diesem Paket hat jedoch ein kleineres
Speicherabbild.

%description nox -l es
Este paquete contiene un binario emacs sin soporte al X Window. Aunque
el binario emacs, en el paquete principal, funcione bien fuera del X
Window (en la consola, por ejemplo) lo que se encuentra en este
paquete utiliza menos memoria.

%description nox -l fr
Ce paquetage contient un binaire emacs construit sans gestion X
Window. Bien que le binaire emacs du paquetage emacs principal
fonctionne bien sans X Window (sur un terminal, par exemple), celui-ci
à une image mémoire plus petite.

%description nox -l pl
Emacs-nox to edytor tekstu Emacs bez wsparcia dla X Window System.

%description nox -l pt_BR
Este pacote contém um binário emacs sem suporte ao X Window. Embora o
binário emacs no pacote principal funcione bem fora do X Window (na
console por exemplo) o que está neste pacote utiliza menos memória.

%description nox -l tr
Bu paket içinde yer alan emacs programý, X11 desteði içermez ve
çalýþmak için daha az belleðe gereksinim duyar.

%package common
Summary:	The libraries needed to run the GNU Emacs text editor
Summary(pl):	Biblioteki potrzebne do uruchomienia edytora tekstu GNU Emacs
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

%description common -l pl
Emacs jest konfigurowalnym, samo-udokumentowanym edytorem tekstu o
du¿ych mo¿liwo¶ciach. Zawiera u³atwienia do pisania kodu, jêzyk
skryptowy (elisp), daje mo¿liwo¶æ czytania poczty, newsów i wiele
innych rzeczy bez opuszczania edytora.

Ten pakiet zawiera biblioteki potrzebne do uruchomienia Emacsa. Oprócz
tego pakietu potrzebny jest jeszcze w³a¶ciwy program (emacs-nox lub
emacs). Zainstaluj emacs-nox je¿eli nie zamierzasz u¿ywasz Emacsa pod
X Window System; zainstaluj emacs je¿eli u¿ywasz X.

%package extras
Summary:	Files which conflict with XEmacs
Summary(pl):	Wspólne pliki XEmacsa i GNU Emacsa
Group:		Applications/Editors/Emacs
Provides:	emacscommon
Obsoletes:	emacscommon

%description extras
These files are common between GNU Emacs and XEmacs.

%description extras -l pl
S± to wspólne pliki GNU Emacs i XEmacs.

%package gnus
Summary:	Gnus is flexible message reader under Emacs
Summary(pl):	Gnus jest czytnikiem grup dyskusyjnych pod Emacsa
Group:		Application/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}

%description gnus
Gnus is flexible message reader under Emacs.

%description gnus -l pl
Gnus jest czytnikiem grup dyskusyjnych pod Emacsa.

%package gnus-el
Summary:	Emacs Lisp source code for Gnus
Summary(pl):	Kod ¼ród³owy Gnusa w Emacs Lispie
Group:		Application/Editors/Emacs
Requires:	%{name}-gnus = %{version}-%{release}

%description gnus-el
Emacs Lisp source code for Gnus.

%description gnus-el -l pl
Kod ¼ród³owy Gnusa w Emacs Lispie.

%prep 
%setup -q


# /usr/sbin is not in standard path
for file in Makefile.in lispref/Makefile.in; do
	sed "s/install\-info/\/usr\/sbin\/install\-info/" < $file > $file.new
	mv $file.new $file
done

%build
cp -f /usr/share/automake/config.* .

# Build binary with X support
[ -d build-withx ] && rm -rf build-withx
mkdir build-withx && cd build-withx
../configure \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--localstatedir=%{_localstatedir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--libexecdir=%{_libdir} \
	--sharedstatedir=%{_var} \
	--with-gcc \
	--with-pop \
	--with-xpm \
	--with-jpeg \
	--with-tiff \
	--with-gif \
	--with-png \
%if %{without gtk}
        --with-x-toolkit \
%else
	--with-gtk \
%endif
	%{_target_platform}

%{__make} bootstrap
cd ..

#Build binary without X support
[ -d build-nox ] && rm -rf build-nox
mkdir build-nox && cd build-nox
../configure \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--localstatedir=%{_localstatedir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--libexecdir=%{_libdir} \
	--sharedstatedir=%{_var} \
	--with-gcc \
	--with-pop \
	--without-xpm \
	--without-jpeg \
	--without-tiff \
	--without-gif \
	--without-png \
	--with-x=no \
	%{_target_platform}

%{__make} bootstrap
cd ..

mv lisp/term/README README.term

sed s!@SITE_START_DIR@!%{_datadir}/emacs/site-lisp/site-start.d! \
	< %{SOURCE3} > site-start.el

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_infodir},%{_datadir}/emacs/site-lisp/site-start.d} \
	$RPM_BUILD_ROOT{%{_desktopdir},/etc/skel,%{_pixmapsdir}} \

%{makeinstall} -C build-withx
install build-nox/src/emacs	$RPM_BUILD_ROOT%{_bindir}/emacs-nox
install site-start.el $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/skel/.emacs
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE5} $RPM_BUILD_ROOT/%{_datadir}/emacs/%{version}/site-lisp/tuareg.el
install %{SOURCE6} $RPM_BUILD_ROOT/%{_datadir}/emacs/%{version}/site-lisp/nemerle.el

install build-nox/etc/DOC-* $RPM_BUILD_ROOT%{_datadir}/emacs/%{version}/etc

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

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
%dir %{_datadir}/emacs/%{version}/lisp/toolbar
%{_desktopdir}/emacs.desktop
%{_pixmapsdir}/*

%files common
%defattr(644,root,root,755)
%config(noreplace) /etc/skel/.emacs
%attr(755,root,root) %{_bindir}/emacsclient
%attr(755,root,root) %{_bindir}/ebrowse
%{_mandir}/man1/emacs*
%{_infodir}/*

%dir %{_libdir}/emacs
%dir %{_libdir}/emacs/%{version}
%dir %{_libdir}/emacs/%{version}/*

%attr(2755,root,mail) %{_libdir}/emacs/%{version}/*-linux/movemail
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/cvtmail
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/digest-doc
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/fakemail
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/hexl
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/profile
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/rcs2log
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/sorted-doc
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/vcdiff
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/yow
%attr(755,root,mail) %{_libdir}/emacs/%{version}/*-linux/update-game-score

%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/%{version}
%dir %{_datadir}/emacs/%{version}/site-lisp
%dir %{_datadir}/emacs/%{version}/lisp
%dir %{_datadir}/emacs/%{version}/leim
%dir %{_datadir}/emacs/%{version}/lisp/calendar
%dir %{_datadir}/emacs/%{version}/lisp/calc
%dir %{_datadir}/emacs/%{version}/lisp/emacs-lisp
%dir %{_datadir}/emacs/%{version}/lisp/emulation
%dir %{_datadir}/emacs/%{version}/lisp/international
%dir %{_datadir}/emacs/%{version}/lisp/language
%dir %{_datadir}/emacs/%{version}/lisp/mail
%dir %{_datadir}/emacs/%{version}/lisp/play
%dir %{_datadir}/emacs/%{version}/lisp/progmodes
%dir %{_datadir}/emacs/%{version}/lisp/term
%dir %{_datadir}/emacs/%{version}/lisp/textmodes
%dir %{_datadir}/emacs/%{version}/lisp/eshell
%dir %{_datadir}/emacs/%{version}/lisp/net
%dir %{_datadir}/emacs/%{version}/lisp/obsolete
%dir %{_datadir}/emacs/%{version}/lisp/mh-e

%{_datadir}/emacs/site-lisp
%{_datadir}/emacs/%{version}/etc
%{_datadir}/emacs/%{version}/lisp/*.elc
%{_datadir}/emacs/%{version}/lisp/README
%{_datadir}/emacs/%{version}/lisp/cus-load.el
%{_datadir}/emacs/%{version}/lisp/cus-start.el.gz
%{_datadir}/emacs/%{version}/lisp/cus-theme.el.gz
%{_datadir}/emacs/%{version}/lisp/finder-inf.el
%{_datadir}/emacs/%{version}/lisp/forms-pass.el
%{_datadir}/emacs/%{version}/lisp/generic-x.el.gz
%{_datadir}/emacs/%{version}/lisp/load*.el
%{_datadir}/emacs/%{version}/lisp/load*.el.gz
%{_datadir}/emacs/%{version}/lisp/ldefs-boot.el
%{_datadir}/emacs/%{version}/lisp/longlines.el.gz
%{_datadir}/emacs/%{version}/lisp/patcomp.el
%{_datadir}/emacs/%{version}/lisp/paths.el
%{_datadir}/emacs/%{version}/lisp/subdirs.el
%{_datadir}/emacs/%{version}/lisp/version.el
%{_datadir}/emacs/%{version}/lisp/language/*.elc
%{_datadir}/emacs/%{version}/lisp/mail/*.elc
%{_datadir}/emacs/%{version}/lisp/mail/blessmail.el
%{_datadir}/emacs/%{version}/lisp/play/*.elc
%{_datadir}/emacs/%{version}/lisp/play/bruce.el
%{_datadir}/emacs/%{version}/lisp/term/*.elc
%{_datadir}/emacs/%{version}/lisp/term/cygwin.el
%{_datadir}/emacs/%{version}/lisp/term/AT386.el
%{_datadir}/emacs/%{version}/lisp/term/apollo.el
%{_datadir}/emacs/%{version}/lisp/term/bobcat.el
%{_datadir}/emacs/%{version}/lisp/term/internal.el
%{_datadir}/emacs/%{version}/lisp/term/iris-ansi.el
%{_datadir}/emacs/%{version}/lisp/term/linux.el
%{_datadir}/emacs/%{version}/lisp/term/lk201.el
%{_datadir}/emacs/%{version}/lisp/term/news.el
%{_datadir}/emacs/%{version}/lisp/term/rxvt.el.gz
%{_datadir}/emacs/%{version}/lisp/term/vt102.el
%{_datadir}/emacs/%{version}/lisp/term/vt125.el
%{_datadir}/emacs/%{version}/lisp/term/vt2*
%{_datadir}/emacs/%{version}/lisp/term/vt3*
%{_datadir}/emacs/%{version}/lisp/term/vt4*
%{_datadir}/emacs/%{version}/lisp/term/wyse50.el
%{_datadir}/emacs/%{version}/lisp/term/xterm.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/*.elc
%{_datadir}/emacs/%{version}/lisp/international/*.elc
%{_datadir}/emacs/%{version}/lisp/international/latin-*.el
%{_datadir}/emacs/%{version}/lisp/international/mule-conf.el
%{_datadir}/emacs/%{version}/lisp/international/latexenc.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/*.elc
%{_datadir}/emacs/%{version}/lisp/calc/*.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/README*
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/*.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-specs.el
%{_datadir}/emacs/%{version}/lisp/textmodes/*.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/*.elc
%{_datadir}/emacs/%{version}/lisp/eshell/*.elc
%{_datadir}/emacs/%{version}/lisp/eshell/esh-groups.el
%{_datadir}/emacs/%{version}/lisp/net/*.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/*.elc
%{_datadir}/emacs/%{version}/lisp/url/*.elc
%{_datadir}/emacs/%{version}/lisp/url/*.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/*.elc
%{_datadir}/emacs/%{version}/lisp/toolbar
%{_datadir}/emacs/%{version}/lisp/mh-e/*.el
%{_datadir}/emacs/%{version}/lisp/mh-e/*.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/*.elc

/var/games/emacs/tetris-scores
/var/games/emacs/snake-scores

%{_datadir}/emacs/%{version}/site-lisp/subdirs.el
%{_datadir}/emacs/%{version}/site-lisp/tuareg.el
%{_datadir}/emacs/%{version}/site-lisp/nemerle.el

%files extras
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/b2m
%attr(755,root,root) %{_bindir}/rcs-checkin
%attr(755,root,root) %{_bindir}/grep-changelog

%files el
%defattr(644,root,root,755)
%{_datadir}/emacs/%{version}/lisp/forms-d2.dat
%{_datadir}/emacs/%{version}/lisp/a*.el.gz
%{_datadir}/emacs/%{version}/lisp/b*.el.gz
%{_datadir}/emacs/%{version}/lisp/c[a-tv]*.el.gz
%{_datadir}/emacs/%{version}/lisp/cus-[a-k]*.el.gz
%{_datadir}/emacs/%{version}/lisp/custom.el.gz
%{_datadir}/emacs/%{version}/lisp/g[f-z]*.el.gz
%{_datadir}/emacs/%{version}/lisp/[de]*.el.gz
%{_datadir}/emacs/%{version}/lisp/f[!io]*.el.gz
%{_datadir}/emacs/%{version}/lisp/fi[!n]*.el.gz
%{_datadir}/emacs/%{version}/lisp/find[!e]*.el.gz
%{_datadir}/emacs/%{version}/lisp/finder.el.gz
%{_datadir}/emacs/%{version}/lisp/fo[!r]*.el.gz
%{_datadir}/emacs/%{version}/lisp/form[!s]*.el.gz
%{_datadir}/emacs/%{version}/lisp/forms.el.gz
%{_datadir}/emacs/%{version}/lisp/forms-d2.el
%{_datadir}/emacs/%{version}/lisp/[h-k]*.el.gz
%{_datadir}/emacs/%{version}/lisp/l[a-n]*.el.gz
%{_datadir}/emacs/%{version}/lisp/locate.el.gz
%{_datadir}/emacs/%{version}/lisp/log-*.el.gz
%{_datadir}/emacs/%{version}/lisp/l[p-z]*.el.gz
%{_datadir}/emacs/%{version}/lisp/[m-o]*.el.gz
%{_datadir}/emacs/%{version}/lisp/paren.el.gz
%{_datadir}/emacs/%{version}/lisp/p[b-z]*.el.gz
%{_datadir}/emacs/%{version}/lisp/[q-r]*.el.gz
%{_datadir}/emacs/%{version}/lisp/s-*.el.gz
%{_datadir}/emacs/%{version}/lisp/s[a-t]*.el.gz
%{_datadir}/emacs/%{version}/lisp/subr.el.gz
%{_datadir}/emacs/%{version}/lisp/[t-u]*.el.gz
%{_datadir}/emacs/%{version}/lisp/[w-z]*.el.gz
%{_datadir}/emacs/%{version}/lisp/v[a-d]*.el.gz
%{_datadir}/emacs/%{version}/lisp/v[f-z]*.el.gz
%{_datadir}/emacs/%{version}/lisp/language/*.el
%{_datadir}/emacs/%{version}/lisp/language/*.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/[c-r]*.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/[t-z]*.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/sendmail.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/smtpmail.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/supercite.el.gz
%{_datadir}/emacs/%{version}/lisp/play/[!b]*.el.gz
%{_datadir}/emacs/%{version}/lisp/play/b[!r]*.el.gz
%{_datadir}/emacs/%{version}/lisp/term/*-win.el.gz
%{_datadir}/emacs/%{version}/lisp/term/sun.el.gz
%{_datadir}/emacs/%{version}/lisp/term/sup-mouse.el.gz
%{_datadir}/emacs/%{version}/lisp/term/tty-colors.el.gz
%{_datadir}/emacs/%{version}/lisp/term/tvi*.el.gz
%{_datadir}/emacs/%{version}/lisp/term/vt100.el.gz
%{_datadir}/emacs/%{version}/lisp/term/sun-mouse.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/*.el.gz
%{_datadir}/emacs/%{version}/lisp/international/[a-k]*.el.gz
%{_datadir}/emacs/%{version}/lisp/international/[o-z]*.el.gz
%{_datadir}/emacs/%{version}/lisp/international/latin*-disp.el.gz
%{_datadir}/emacs/%{version}/lisp/international/mule-cmds.el.gz
%{_datadir}/emacs/%{version}/lisp/international/mule-diag.el.gz
%{_datadir}/emacs/%{version}/lisp/international/mule-util.el.gz
%{_datadir}/emacs/%{version}/lisp/international/mule.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/*.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/[!c]*.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/c[a-k]*.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/c[m-z]*.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-[!s]*.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-seq.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/*.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/*.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/e[a-r]*.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/esh-[!g]*.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/esh-*.el
%{_datadir}/emacs/%{version}/lisp/eshell/esh[a-z]*.el.gz
%{_datadir}/emacs/%{version}/lisp/net/*.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/*.el
%{_datadir}/emacs/%{version}/lisp/obsolete/*.el.gz
%{_datadir}/emacs/%{version}/lisp/toolbar

%files leim
%defattr(644,root,root,755)
%dir %{_datadir}/emacs/%{version}/leim/ja-dic
%dir %{_datadir}/emacs/%{version}/leim/quail
%{_datadir}/emacs/%{version}/leim/leim-list.el
%{_datadir}/emacs/%{version}/leim/quail/*.elc
%{_datadir}/emacs/%{version}/leim/ja-dic/*.elc

%files leim-el
%defattr(644,root,root,755)
%{_datadir}/emacs/%{version}/leim/quail/*.el.gz
%{_datadir}/emacs/%{version}/leim/ja-dic/*.el.gz

%files nox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/emacs-nox

%files gnus
%defattr(644,root,root,755)
%dir %{_datadir}/emacs/%{version}/lisp/gnus
%{_datadir}/emacs/%{version}/lisp/gnus/TODO
%{_datadir}/emacs/%{version}/lisp/gnus/*.*
%exclude %{_datadir}/emacs/%{version}/lisp/gnus/*.el.gz

%files gnus-el
%defattr(644,root,root,755)
%{_datadir}/emacs/%{version}/lisp/gnus/*.el.gz
