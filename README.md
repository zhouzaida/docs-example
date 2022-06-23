# docs-example

## Build Docs

```bash
conda create -n docs-example python=3.7
conda activate docs-example
git clone git@github.com:zhouzaida/docs-example.git
cd docs-example
pip install -r requirements/docs.txt
cd docs/en
make html
```

After typing above commands, open the _build/html/index.html file and docs will be displayed.
