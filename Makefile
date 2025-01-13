PYTHON := python3
VENV := venv
ACTIVATE := source $(VENV)/bin/activate
REQUIREMENTS := requirements.txt

install:
	$(PYTHON) -m venv $(VENV) && $(ACTIVATE) && pip install --upgrade pip && pip install -r $(REQUIREMENTS)

run:
	$(ACTIVATE) && $(PYTHON) src/main.py

clean:
	rm -rf $(VENV)

help:
	@echo "Доступные команды:"
	@echo "  make install   - Установить зависимости"
	@echo "  make run       - Запустить проект"
	@echo "  make clean     - Удалить виртуальное окружение"
