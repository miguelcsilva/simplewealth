LIGHT_CYAN="\033[1;36m"
DARK_GREY="\033[1;30m"
NO_COLOR="\033[0m"
SEPARATOR="${DARK_GREY}---------------------------${NO_COLOR}\n"

printf "$SEPARATOR${LIGHT_CYAN}Running isort:${NO_COLOR}\n"
isort .
printf "$SEPARATOR${LIGHT_CYAN}Running black:${NO_COLOR}\n"
black .
printf "$SEPARATOR${LIGHT_CYAN}Running flake8:${NO_COLOR}\n"
flake8 --statistics .
printf "$SEPARATOR${LIGHT_CYAN}Running mypy:${NO_COLOR}\n"
mypy .
printf "$SEPARATOR${LIGHT_CYAN}Running sqlfluff:${NO_COLOR}\n"
sqlfluff lint .
printf "$SEPARATOR${LIGHT_CYAN}Running pytest:${NO_COLOR}\n"
pytest --quiet tests/
printf $SEPARATOR
