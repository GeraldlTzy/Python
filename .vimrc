set number 
set number
set mouse=a
set numberwidth=1
set clipboard=unnamed
""Añadidos
let python_highlight_all=1
set splitbelow
set splitright
set foldmethod=indent
set foldlevel=99
let g:SimpylFold_docstring_preview=1
let g:slime_target = "tmux"
let g:slime_python_ipython = 1
let g:slime_python_ipython_exe = 'ipython'
let g:slime_python_default = 'ipython'

autocmd FileType python setlocal makeprg=jupyter\ nbconvert\ --to=python\ --stdout\ %
let g:jupyter_console_cmd = "ipython"
let g:ycm_autoclose_preview_window_after_completion=1

set nocompatible
filetype plugin on
set omnifunc=syntaxcomplete#Complete
syntax on
set showcmd
set ruler
set cursorline
set encoding=utf-8
set showmatch
set termguicolors
set sw=2
set relativenumber
so ~/.vim/plugins.vim
so ~/.vim/plugin-config.vim
so ~/.vim/maps.vim

highlight Normal ctermbg=NONE
set laststatus=2
set noshowmode
let g:python3_host_prog = '/usr/bin/python3'

au BufNewFile,BufRead *.html set filetype=htmldjango

"" Searching
set hlsearch                    " highlight matches
set incsearch                   " incremental searching
set ignorecase                  " searches are case insensitive...
set smartcase                   " ... unless they contain at least one capital letter

" Python settings 
au BufNewFile,BufRead *.py
    \set tabstop=4
    \set softtabstop=4
    \set shiftwidth=4
    \set textwidth=79
    \set expandtab
    \set autoindent
    \set fileformat=unix

au BufNewFile,BufRead *.js, *.html, *css
	  \set tabstop=2
	  \set softtabstop=2
 		\set shiftwidth=2
