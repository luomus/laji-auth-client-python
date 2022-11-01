# Development

## Testing

Start by creating a Python virtual environment and installing dependencies

    python3.8 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    pip install -e .

Run the tests

    python -m unittest

## Publishing

Build the package

    python setup.py sdist bdist_wheel

You can first publish the package to TestPyPI to confirm that it works

    twine upload -r testpypi dist/*

Then you can publish it to PyPI

    twine upload dist/*