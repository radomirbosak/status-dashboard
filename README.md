# Status Dashboard

This repo contains a simple python script which runs scripts from the `probes/` directory, executes them and produces a HTML dashboard containing the scripts' output colored according to their exit code.

| Exit code | Meaning | Color |
| --------- | ------- | ----- |
| 0         | OK      | green |
| 1         | Error   | red   |
| 2         | Warning | orange |
| 3         | Info    | blue  |
| other     | Error   | red   |


## Usage

```console
$ cd status-dashboard
$ python3 generate_dashboard.py > dashboard.html
```
