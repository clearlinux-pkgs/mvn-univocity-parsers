#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-univocity-parsers
Version  : 2.7.3
Release  : 2
URL      : https://github.com/uniVocity/univocity-parsers/archive/v2.7.3.tar.gz
Source0  : https://github.com/uniVocity/univocity-parsers/archive/v2.7.3.tar.gz
Source1  : https://repo1.maven.org/maven2/com/univocity/univocity-parsers/2.7.3/univocity-parsers-2.7.3.jar
Source2  : https://repo1.maven.org/maven2/com/univocity/univocity-parsers/2.7.3/univocity-parsers-2.7.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-univocity-parsers-data = %{version}-%{release}

%description
![thumbnail](./images/univocity-parsers.png)
Welcome to univocity-parsers
============================

%package data
Summary: data components for the mvn-univocity-parsers package.
Group: Data

%description data
data components for the mvn-univocity-parsers package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/univocity/univocity-parsers/2.7.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/univocity/univocity-parsers/2.7.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/univocity/univocity-parsers/2.7.3
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/univocity/univocity-parsers/2.7.3


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/univocity/univocity-parsers/2.7.3/univocity-parsers-2.7.3.jar
/usr/share/java/.m2/repository/com/univocity/univocity-parsers/2.7.3/univocity-parsers-2.7.3.pom
