NAME=cbz
SRC=cbz
ZIP=$(NAME).zip
SRC_FILES=__init__.py

$(ZIP): $(addprefix $(SRC)/,$(SRC_FILES))
	cd $(SRC) && zip -r ../$(ZIP) $(SRC_FILES)

zip: $(ZIP)

install: $(ZIP)
	calibre-customize -a $(ZIP)

test: install
	calibre-debug -e $(SRC)/__init__.py

clean:
	rm -f $(ZIP)
