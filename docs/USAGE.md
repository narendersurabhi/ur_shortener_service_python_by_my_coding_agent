# Usage

This document gives a concise, practical overview of how to run the project (CLI) and how to use it as a library (programmatically). Replace placeholder package and entrypoint names with the concrete project names in this repository.

## Quick start

Install (pick one):

    npm install --save project-name

or

    pip install project-name

Run the command-line tool (if provided):

    project-name [options] <input>

or directly via node/python:

    node ./bin/cli.js [options] <input>
    python -m project_name [options] <input>

## Common CLI options

    -h, --help       Show help
    -v, --version    Show version
    -c, --config     Path to config file (JSON/YAML)
    -o, --output     Output file or directory

(Options vary by project; run --help to see the real list.)

## Library usage (JavaScript)

    // CommonJS
    const lib = require('project-name');
    // or ES module
    import lib from 'project-name';

    // Typical pattern
    const result = lib.process({ input: 'input.txt', options: { verbose: true } });

    // If the API is async
    (async () => {
      const out = await lib.processAsync({ input: 'input.txt' });
      console.log(out);
    })();

## Library usage (Python)

    from project_name import process

    result = process(input='input.txt', verbose=True)

## Configuration

Put configuration in a JSON or YAML file and reference it with --config. Example config keys:

    {
      "input": "path/to/input",
      "output": "path/to/output",
      "options": { "flag": true }
    }

## Troubleshooting

- If something fails, run with a verbose or debug flag to get more logs.
- Ensure required runtime (node/python) and dependencies are installed.
- For permission errors, check file system permissions for input/output paths.

## Next steps

See docs/EXAMPLES.md for concrete usage patterns and expected behavior.