#!/bin/bash


# cd to this script's folder
cd "$(dirname "$(realpath $0)")"


# print errors
function print_and_exit {

    echo ""
    echo "#"
    echo "# $1"
    echo "#"
    echo ""

    exit 1

}


# set default arguments
APP_CONFIG_PATH="$HOME/.app/config.toml"

# get passed arguments
for argument in "$@"
do
    if ! [[ "$argument" =~ .*=.* ]]; then
        print_and_exit "ensure argument is passed as key=value"
    fi

    key="${argument%%=*}"
    value="${argument#*=}"

    if [ -z "$key" ]; then
        print_and_exit 'key cannot be empty'
    fi

    if [ -z "$value" ]; then
        print_and_exit 'value cannot be empty'
    fi

    case "$key" in

        'APP_CONFIG_PATH')
            if ! [[ "$value" =~ \.toml$ ]]; then
                print_and_exit 'APP_CONFIG_PATH must be a .toml file'
            fi

            if ! [ -e "$value" ]; then
                print_and_exit "$value is not a valid path"
            fi

            ;;

        'TEST_SUBJECT')
            if ! [[ "$value" =~ ^(\./)?tests ]]; then
                print_and_exit 'TEST_SUBJECT must begin with "tests" or "./tests"'
            fi

            if ! [ -e "$value" ]; then
                print_and_exit "$value is not a valid path"
            fi

            if ! ([ -d "$value" ] || [[ "$value" =~ _test.py$ ]]); then
                print_and_exit 'TEST_SUBJECT must be a folder, or a file ending with "_test.py"'
            fi

            ;;

        *)
            print_and_exit "unexpected argument: $argument. parameters include: APP_CONFIG_PATH, TEST_SUBJECT" ;;

    esac

    declare "$key"="$value"

done

unset argument
unset key
unset value


# manage venv and cache
function clear_venv_and_pycache {
    rm -rf .venv
    rm -f uv.lock
    find . -type d -name '__pycache__' -prune -exec rm -rf '{}' '+'
}


function set_up_venv {
    uv sync --native-tls
    source .venv/bin/activate
}


# run python
function run_app {
    cd app
    uv run app.py
    cd ..
}


function run_test {

    if [ -z "${PYTHONPATH-}" ]; then
        export PYTHONPATH="$(realpath app)"
    else
        export PYTHONPATH="$PYTHONPATH:$(realpath app)"
    fi

    cd tests

    TEST_SUBJECT="${TEST_SUBJECT#./}"
    TEST_SUBJECT="${TEST_SUBJECT#tests}"
    TEST_SUBJECT="${TEST_SUBJECT#/}"

    if [ -z $TEST_SUBJECT ]; then
        TEST_SUBJECT=.
    fi

    if [ -d $TEST_SUBJECT ]; then
        python -m unittest discover -s $TEST_SUBJECT -p '*_test.py'
    elif [ -f $TEST_SUBJECT ]; then
        python -m unittest $TEST_SUBJECT
    else
        echo 'nothing to test'
    fi

    cd ..

    unset PYTHONPATH

}


# set up
clear_venv_and_pycache

set_up_venv


# run python
export APP_CONFIG_PATH="$(realpath $APP_CONFIG_PATH)"

if test -n "${TEST_SUBJECT-}"; then
    run_test
else
    run_app
fi

unset APP_CONFIG_PATH


# reset
deactivate

clear_venv_and_pycache


# confirm
echo 'completed'
