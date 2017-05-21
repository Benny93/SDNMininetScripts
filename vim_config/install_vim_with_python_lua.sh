#!/bin/bash

apt-get update

apt-get install -y libncurses5-dev libgnome2-dev libgnomeui-dev \
	libgtk2.0-dev libatk1.0-dev libbonoboui2-dev \
	libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev \
	python3-dev ruby-dev lua5.1 lua5.1-dev libperl-dev git

apt-get remove -y vim vim-runtime gvim
apt-get remove -y vim-tiny vim-common vim-gui-common vim-nox

cd ~
git clone https://github.com/vim/vim.git
cd vim
./configure --with-features=huge \
	--enable-multibyte \
	--enable-rubyinterp=yes \
	--enable-python3interp=yes \
	--with-python3-config-dir=/usr/lib/python3.5/config \
	--enable-perlinterp=yes \
	--enable-luainterp=yes \
	--enable-gui=gtk2 --enable-cscope --prefix=/usr
make VIMRUNTIMEDIR=/usr/share/vim/vim80


apt-get install checkinstall
cd ~/vim
sudo checkinstall

#backup
#	--enable-pythoninterp=yes \
#	--with-python-config-dir=/usr/lib/python2.7/config \
