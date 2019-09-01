ALGORITHMS=./algorithms
.PHONY: pdf main.pdf clean
main.pdf:
	mkdir -p build
	python substitute.py $(ALGORITHMS)
	pdflatex --output-directory ./build main_mod.tex
	cp ./build/main_mod.pdf ./main.pdf
pdf: main.pdf
clean:
	rm -R ./build
