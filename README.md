# zoomoomoo

This exposes any Python file's global callables as an MCP. To call it, use:

./zimomo.py -f [test.py]

There are intentionally no safeguards: if you don't read the target python file and you get rm'ed, look in the mirror for the person responsible.

If you are using a conda environment, run this as:
```
conda run -n <env_name> python /abspath/to/zimomo.py -f /abspath/to/module
```

You need to use 'python' not 'python3' on Mac (credit to chatgpt for identifying this)
