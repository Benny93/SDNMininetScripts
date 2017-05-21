
apt-get update
apt-get install -y curl
mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
touch ~/.vimrc
echo 'execute pathogen#infect()\n
syntax on\n
filetype plugin indent on\n
\n
:let mapleader = ","'
ls .vim
cd ~/.vim/bundle/ && git clone --recursive https://github.com/davidhalter/jedi-vim.git
git clone https://github.com/Shougo/neosnippet.vim.git
git clone https://github.com/Shougo/neocomplete.vim.git
