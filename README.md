# jinja2-templating
this is a small script utilizing the jinja2 templating capabilities I love about ansible
it also contains a small example for rendering a `.ssh/config` file from a yaml dictionary

## requirements

`pip3 install jinja2 pyyaml`

## usage

```bash
run.py example/vars.yaml example/ssh_config.j2
```

**OR**

```bash
run.py example/vars.yaml example/ssh_config.j2 outfile.txt
```
