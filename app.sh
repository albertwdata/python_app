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
    # confirm argument contains "="
    if ! [[ "$argument" =~ .*=.* ]]; then
        print_and_exit "ensure argument is passed as key=value"
    fi

    # parse argument into "key" and "value" variables
    key="${argument%%=*}"
    value="${argument#*=}"

    # confirm "key" is not empty
    if [ -z "$key" ]; then
        print_and_exit 'key cannot be empty'
    fi

    # confirm "value" is not empty
    if [ -z "$value" ]; then
        print_and_exit 'value cannot be empty'
    fi

    case "$key" in

        'APP_CONFIG_PATH')
            # confirm config is toml file
            if ! [[ "$value" =~ \.toml$ ]]; then
                print_and_exit 'APP_CONFIG_PATH must be a .toml file'
            fi

            ;;

        'TEST_SUBJECT')
            # confirm test subject is "tests" folder or anything within
            if ! [[ "$value" =~ ^(\./)?tests ]]; then
                print_and_exit 'TEST_SUBJECT must begin with "tests" or "./tests"'
            fi

            # confirm test subject is either:
                # a directory, ("tests" or any other name if a subfolder),
                # or a file ending with "_test.py"
                    # the default for python's unittest module is to look for python files prefixed with "test_"
                    # this script runs unittest with the pattern "*_test.py"
                    # python test files must contain "_test" as the suffix instead of the prefix
            if ! ([ -d "$value" ] || [[ "$value" =~ _test.py$ ]]); then
                print_and_exit 'TEST_SUBJECT must be a folder, or a file ending with "_test.py"'
            fi

            ;;

        *)
            print_and_exit "unexpected argument: $argument. parameters include: APP_CONFIG_PATH, TEST_SUBJECT" ;;

    esac

    # confirm value exists
    if ! [ -e "$value" ]; then
        print_and_exit "$value is not a valid path"
    fi

    # define key:value pair
    declare "$key"="$value"

done

unset argument
unset key
unset value


# clear venv and cache
function clear_venv_and_pycache {
    rm -rf .venv
    rm -f uv.lock
    find . -type d -name '__pycache__' -prune -exec rm -rf '{}' '+'
}


# set up venv
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


# run test
function run_test {

    # export path to app
    if [ -z "${PYTHONPATH-}" ]; then
        export PYTHONPATH="$(realpath app)"
    else
        export PYTHONPATH="$PYTHONPATH:$(realpath app)"
    fi

    # move into tests folder
    cd tests

    # remove "./tests/"
    TEST_SUBJECT="${TEST_SUBJECT#./}"
    TEST_SUBJECT="${TEST_SUBJECT#tests}"
    TEST_SUBJECT="${TEST_SUBJECT#/}"

    # set relative path for "tests" if it is the test subject
    if [ -z $TEST_SUBJECT ]; then
        TEST_SUBJECT=.
    fi

    # if test subject is directory, test files ending with "_test.py"
    if [ -d $TEST_SUBJECT ]; then
        python -m unittest discover -s $TEST_SUBJECT -p '*_test.py'
    # if test subject is file, test it
    # validation will have already confirmed it is a "_test.py" file
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
