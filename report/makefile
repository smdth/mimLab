DOC_NAME=report
default:
	pandoc \
		--from markdown+yaml_metadata_block+table_captions \
		--to latex \
		--variable documentclass=scrartcl \
    --variable classoption=a4paper \
    --variable classoption=10pt \
		--include-in-header $(DOC_NAME)-header.tex \
		--include-after-body $(DOC_NAME)-footer.tex \
		--listings \
		--output $(DOC_NAME).tex \
		--template=template.latex \
		$(DOC_NAME).md
	latexmk -pdflatex="pdflatex --shell-escape %O %S" -pdf $(DOC_NAME).tex


		#--variable theme=Minimal \

clean:
	latexmk -c
