# programmingCheatSheet
A CheatSheet for programming contests

## How to build
**Requirements**:
* `make`
* `python`
* `pdflatex`

To build the pdf run: `make` or `make pdf`

## How to extend
To add other code snippets, add them to the `algorithms`-directory. A code snippet is as follows:
~~~
# Title of the code snippet
## Extra explanations or text that will be visible in between the title and code
## Can be of arbitrary length and full LaTeX-syntax supported
def something():
  pass
~~~

In the document this will become:
~~~
\subsection*{Title of the code snippet}
Extra explanations or text that will be visible in between the title and code
Can be of arbitrary length and full LaTeX-syntax supported
\begin{lstlisting}[language=python]
def something():
  pass
\end{lstlisting}
~~~
