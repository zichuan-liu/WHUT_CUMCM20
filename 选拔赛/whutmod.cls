%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% UNOFFICIAL LaTeX Template for WHUT Summer Modeling Training
%% Derived from and Compatible with latexstudio/CUMCMThesis
%% Modified by Mark Huang Communication Engineering (Experimental)
%% First Released on 2018/7/30
%% See https://github.com/Markhng/whutmod
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{whutmod}
				[2018/07/13 v0.991 UNOFFICIAL LaTeX Template for WHUT Modeling]
%% Inital Code
\newif\if@mcm@bwprint\@mcm@bwprintfalse
\newif\if@mcm@preface\@mcm@prefacetrue
% tokens definition
%%%% 承诺书
\newcommand\mcm@tokens@keywords{}
\renewcommand\@title{}
\newcommand*\mcm@tokens@tihao{}
\newcommand*\mcm@tokens@team{}
\newcommand*\mcm@tokens@membera{}
\newcommand*\mcm@tokens@memberb{}
\newcommand*\mcm@tokens@memberc{}
\newcommand*\mcm@tokens@joba{}
\newcommand*\mcm@tokens@jobb{}
\newcommand*\mcm@tokens@jobc{}
\newcommand*\mcm@tokens@yearinput{\the\year}
\newcommand*\mcm@tokens@monthinput{\the\month}
\newcommand*\mcm@tokens@dayinput{\the\day}

%% Declaration of Options
\DeclareOption{colorprint}{\@mcm@bwprintfalse}
\DeclareOption{bwprint}{\@mcm@bwprinttrue}
\DeclareOption{withoutpreface}{\@mcm@prefacefalse}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
%% Executing of Options
\ExecuteOptions{colorprint}
\ProcessOptions\relax
%% Loading Class
\LoadClass[a4paper,12pt]{article}
%% Loading Package
\RequirePackage{ifxetex}
\RequireXeTeX
\ifxetex\else
\ClassError{whutmod}{You must use the `xelatex' driver\MessageBreak Please choose `xelatex'}{%
Just choose `xelatex', no `pdflatex' or `latex' and so on.}
\fi
\RequirePackage{ctex}
\RequirePackage{geometry}
\RequirePackage{amsmath}
\RequirePackage{amsfonts}
\RequirePackage{amssymb}
\RequirePackage{bm}
\RequirePackage{titletoc}
\RequirePackage{xcolor}
\RequirePackage{graphicx}
\RequirePackage{array}
\RequirePackage{longtable}
\RequirePackage{booktabs}
\RequirePackage{multirow}
\RequirePackage{bigstrut}
\RequirePackage{bigdelim}
\RequirePackage{cprotect}
\RequirePackage{listings}
\RequirePackage{xcolor}
\RequirePackage{hyperref}

\definecolor{dkgreen}{rgb}{0,0.6,0}
\definecolor{gray}{rgb}{0.5,0.5,0.5}
\definecolor{mauve}{rgb}{0.58,0,0.82}
\lstset{
	frame=tb,
	aboveskip=3mm,
	belowskip=3mm,
	showstringspaces=false,
	columns=flexible,
	framerule=1pt,
	rulecolor=\color{gray!35},
	backgroundcolor=\color{gray!5},
	basicstyle={\small\ttfamily},
	numbers=none,
	numberstyle=\tiny\color{gray},
	keywordstyle=\color{blue},
	commentstyle=\color{dkgreen},
	stringstyle=\color{mauve},
	breaklines=true,
	breakatwhitespace=true,
	tabsize=3,
}
\RequirePackage{indentfirst}
\RequirePackage{caption}
\RequirePackage{enumitem}
\RequirePackage{ulem}
\RequirePackage{calc}
\RequirePackage{hyperref}
%% Document Layout
\geometry{top=25mm,bottom=25mm,left=25mm,right=25mm}
\renewcommand*{\baselinestretch}{1.38}
\let\mcm@oldtabular\tabular
\let\mcm@endoldtabular\endtabular
\renewenvironment{tabular}%
	{\bgroup%
	\renewcommand{\arraystretch}{1.38}%
	\mcm@oldtabular}%
	{\mcm@endoldtabular\egroup}
\setlength\parindent{2em}
\setmainfont{Times New Roman}
\setsansfont{Arial}
\setCJKfamilyfont{kai}[AutoFakeBold]{simkai.ttf}
\newcommand*{\kai}{\CJKfamily{kai}}
\setCJKfamilyfont{song}[AutoFakeBold]{SimSun}
\newcommand*{\song}{\CJKfamily{song}}
\setCJKfamilyfont{fs}[AutoFakeBold]{STFangsong}
\newcommand*{\fs}{\CJKfamily{fs}}
%\setCJKfamilyfont{fangsong}{STFangsong}
%\newcommand*{\fangsong}{\CJKfamily{fangsong}}

\renewcommand\normalsize{%
	\@setfontsize\normalsize{12.05}{14.45}%
	\abovedisplayskip 12\p@ \@plus3\p@ \@minus7\p@
	\abovedisplayshortskip \z@ \@plus3\p@
	\belowdisplayshortskip 6.5\p@ \@plus3.5\p@ \@minus3\p@}
\newtheorem{definition}{\mcm@cap@definition}
\newtheorem{theorem}{\mcm@cap@theorem}
\newtheorem{lemma}{\mcm@cap@lemma}
\newtheorem{corollary}{\mcm@cap@corollary}
\newtheorem{assumption}{\mcm@cap@assumption}
\newtheorem{conjecture}{\mcm@cap@conjecture}
\newtheorem{axiom}{\mcm@cap@axiom}
\newtheorem{principle}{\mcm@cap@principle}
\newtheorem{problem}{\mcm@cap@problem}
\newtheorem{example}{\mcm@cap@example}
\newtheorem{proof}{\mcm@cap@proof}
\newtheorem{solution}{\mcm@cap@solution}

 \renewcommand*{\textfraction}{0.05}
 \renewcommand*{\topfraction}{0.9}
 \renewcommand*{\bottomfraction}{0.8}
 \renewcommand*{\floatpagefraction}{0.85}
\DeclareGraphicsExtensions{.pdf,.eps,.jpg,.png}
\graphicspath{{figures/}{figure/}{pictures/}%
  {picture/}{pic/}{pics/}{image/}{images/}}
\DeclareCaptionFont{song}{\songti}
\DeclareCaptionFont{minusfour}{\zihao{-4}}
\captionsetup[figure]{%
	format=hang,
	labelsep=quad,
	font={song,minusfour,bf},
	position=bottom
}
\captionsetup[table]{%
	format=hang,
	labelsep=quad,
	font={song,minusfour,bf},
	position=top
}

\setlist{%
	topsep=0.3em,
	partopsep=0pt,
	itemsep=0ex plus 0.1ex,
	parsep=0pt,
	leftmargin=1.5em,
	rightmargin=0em,
	labelsep=0.5em,
	labelwidth=2em
}


\lstnewenvironment{tcode}
  {
    \lstset{basicstyle = \small\ttfamily,
        language=TeX,
        tabsize = 4,
        frame = single,
        escapechar = `,
        breaklines = true,
        breakatwhitespace = true,
        frameround = tttt,
    }
  }
  {}

%% Document Markup

\renewcommand{\maketitle}{\par
	\begingroup
      \newpage
      \global\@topnum\z@
      \@maketitle
    \endgroup
  \global\let\thanks\relax
  \global\let\maketitle\relax
  \global\let\@maketitle\relax
  \global\let\@thanks\@empty
  \global\let\@author\@empty
  \global\let\@date\@empty
  \global\let\@title\@empty
  \global\let\title\relax
  \global\let\author\relax
  \global\let\date\relax
  \global\let\and\relax
}
\def\@maketitle{%
  \newpage
  \if@mcm@preface
  \null
  
	\vskip2ex
	\thispagestyle{empty}
	\setcounter{page}{1}
	\begin{center}
		
		\includegraphics[width=12.83cm]{whut.jpg}
		\vskip2ex
		{\zihao{2}\fs \textbf{数学建模暑期培训论文}}
		\vskip7ex
		{\zihao{2}\fs \textbf{第\;{\color{red} \mcm@tokens@tihao}\;题}}
		
		\vskip5ex
		{\zihao{2}\fs \textbf{\@title}
			\\[-30pt]\noindent\rule{12.83cm}{2pt}\par}
		\vskip14ex
		{\zihao{2} \bfseries 第 {\;\color{red}\mcm@tokens@team} 组}\\[5pt]
		\begin{tabular}{w{l}{28ex}w{c}{20ex}}
			{\fs \zihao{3} \textbf{姓名}} & {\fs \zihao{3} \textbf{方向}} \\
			{\fs \zihao{-3} \color{red}\mcm@tokens@membera （组长）} & {\fs \zihao{-3} \mcm@tokens@joba}\\
			{\fs \zihao{-3} \color{red}\mcm@tokens@memberb} & {\fs \zihao{-3} \mcm@tokens@jobb}\\
			{\fs \zihao{-3} \color{red}\mcm@tokens@memberc} & {\fs \zihao{-3} \mcm@tokens@jobc}\\
		\end{tabular}
		\vfill
		{\zihao{-3}\bfseries \mcm@tokens@yearinput 年  \mcm@tokens@monthinput 月 \mcm@tokens@dayinput 日}
	\end{center}
%	\null
%	\fi
	\newpage}


% 中文标题名称设置
\renewcommand\contentsname{\mcm@cap@contentsname}
\renewcommand\listfigurename{\mcm@cap@listfigurename}
\renewcommand\listtablename{\mcm@cap@listtablename}
\renewcommand\refname{\mcm@cap@refname}
\renewcommand\indexname{\mcm@cap@indexname}
\renewcommand\figurename{\mcm@cap@figurename}
\renewcommand\tablename{\mcm@cap@tablename}
\renewcommand\appendixname{\mcm@cap@appendixname}
\renewcommand\abstractname{\mcm@cap@abstractname}

\setcounter{secnumdepth}{3}
\def\@seccntformat#1{\csname the#1\endcsname\ }
\renewcommand\thesection{\chinese{section}、}
\renewcommand\thesubsection{\arabic{section}\thinspace.\thinspace\arabic{subsection}}
\renewcommand\thesubsubsection{\thesubsection\thinspace.\thinspace\arabic{subsubsection}}
\renewcommand\section{\@startsection{section}{1}{\z@}%
 	{-3.5ex \@plus -1ex \@minus -.2ex}%
	{2.3ex \@plus.2ex}%
	{\centering\normalfont\Large\bfseries}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
	{-3.25ex\@plus -1ex \@minus -.2ex}%
	{1.5ex \@plus .2ex}%
	{\normalfont\large\bfseries}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
	{-3.25ex\@plus -1ex \@minus -.2ex}%
	{1.5ex \@plus .2ex}%
	{\normalfont\normalsize\bfseries}}
\renewcommand\paragraph{\@startsection{paragraph}{4}{\z@}%
	{3.25ex \@plus1ex \@minus.2ex}%
	{-1em}%
	{\normalfont\normalsize\bfseries}}
\renewcommand\subparagraph{\@startsection{subparagraph}{5}{\parindent}%
	 {3.25ex \@plus1ex \@minus .2ex}%
	 {-1em}%
	 {\normalfont\normalsize\bfseries}}

\renewenvironment{abstract}{%
\if@twocolumn
		\section*{\abstractname}%
	\else
	 \begin{center}%
	{\zihao{4}\bfseries \abstractname\vspace{-.5em}\vspace{\z@}}%
	 \end{center}%
 	 \quotation
	\fi}
	{\if@twocolumn\else\endquotation\newpage\null\fi}
\renewenvironment{quotation}
	{\list{}{\listparindent 2em%
	 \itemindent \listparindent
	 \rightmargin\z@
	 \leftmargin\z@
	 \parsep \z@ \@plus\p@}%
	\item\relax}
	{\endlist}

\newcommand\keywords[1]{%
	\renewcommand{\mcm@tokens@keywords}{#1}
	~\\
	\par
	\vskip1ex
	{\noindent\zihao{-4}\heiti\mcm@cap@keywordsname：}~{\bf\mcm@tokens@keywords}
	}

\let\@oldappendix\appendix
\renewcommand\appendix{\par
	\@oldappendix
%	\setcounter{section}{0}%
%	\setcounter{subsection}{0}%
	\gdef\thesection{\appendixname\@Alph\c@section}
	\gdef\thesubsection{\Alph{section}.\@arabic\c@subsection}
	\gdef\thesubsubsection{\Alph{section}.\arabic{subsection}.\@arabic\c@subsubsection}
}

\renewenvironment{thebibliography}[1]
     {\section*{\refname}%
      \@mkboth{\MakeUppercase\refname}{\MakeUppercase\refname}%
      \list{\@biblabel{\@arabic\c@enumiv}}%
           {\settowidth\labelwidth{\@biblabel{#1}}%
            \leftmargin\labelwidth
            \advance\leftmargin\labelsep
            \@openbib@code
            \usecounter{enumiv}%
            \let\p@enumiv\@empty
            \renewcommand\theenumiv{\@arabic\c@enumiv}}%
      \sloppy
      \clubpenalty4000
      \@clubpenalty \clubpenalty
      \widowpenalty4000%
      \sfcode`\.\@m}
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \endlist}	

\newcommand*\tihao[1]{%
	\renewcommand{\mcm@tokens@tihao}{#1}}
\newcommand*\team[1]{%
	\renewcommand{\mcm@tokens@team}{#1}}
\newcommand*\membera[1]{%
	\renewcommand{\mcm@tokens@membera}{#1}}
\newcommand*\memberb[1]{%
	\renewcommand{\mcm@tokens@memberb}{#1}}
\newcommand*\memberc[1]{%
	\renewcommand{\mcm@tokens@memberc}{#1}}
\newcommand*\joba[1]{%
	\renewcommand{\mcm@tokens@joba}{#1}}
\newcommand*\jobb[1]{%
	\renewcommand{\mcm@tokens@jobb}{#1}}
\newcommand*\jobc[1]{%
	\renewcommand{\mcm@tokens@jobc}{#1}}
\newcommand*\yearinput[1]{%
	\renewcommand{\mcm@tokens@yearinput}{#1}}
\newcommand*\monthinput[1]{%
	\renewcommand{\mcm@tokens@monthinput}{#1}}
\newcommand*\dayinput[1]{%
	\renewcommand{\mcm@tokens@dayinput}{#1}}

\newcommand*{\mcm@cap@definition}{定义}
\newcommand*{\mcm@cap@theorem}{定理}
\newcommand*{\mcm@cap@lemma}{引理}
\newcommand*{\mcm@cap@corollary}{推论}
\newcommand*{\mcm@cap@assumption}{假设}
\newcommand*{\mcm@cap@conjecture}{猜想}
\newcommand*{\mcm@cap@axiom}{公理}
\newcommand*{\mcm@cap@principle}{定律}
\newcommand*{\mcm@cap@problem}{问题}
\newcommand*{\mcm@cap@example}{例}
\newcommand*{\mcm@cap@proof}{证明}
\newcommand*{\mcm@cap@solution}{解}
\newcommand*{\mcm@cap@contentsname}{目录}
\newcommand*{\mcm@cap@listfigurename}{插图清单}
\newcommand*{\mcm@cap@listtablename}{附表清单}
\newcommand*{\mcm@cap@refname}{参考文献}
\newcommand*{\mcm@cap@indexname}{索引}
\newcommand*{\mcm@cap@figurename}{图}
\newcommand*{\mcm@cap@tablename}{表}
\newcommand*{\mcm@cap@appendixname}{附录}
\newcommand*{\mcm@cap@abstractname}{摘要}
\newcommand*{\mcm@cap@keywordsname}{关键词}

\titlecontents{section}[0pt]{\vspace{2mm}\bfseries}
{\thecontentslabel\hskip.5em}{}{\titlerule*[0.5pc]{.}\contentspage}
\titlecontents{subsection}[30pt]{\songti}
{\thecontentslabel\hskip.5em}{}{\titlerule*[0.5pc]{.}\contentspage}
\titlecontents{subsubsection}[55pt]{\songti}
{\thecontentslabel\hskip.5em}{}{\titlerule*[0.5pc]{.}\contentspage}

\endinput

