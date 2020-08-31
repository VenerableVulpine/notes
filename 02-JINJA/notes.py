"""
JINJA2:
statements: {{  }}          <-- use this to print
blocks:     {%  %}          <-- statements and blocks

{{ python_variable }}          <-- works
{{ python variable = 10 }}     <-- doesn't work


Template blocks:
    {% include "example.html" %}    --  TBA         <--- use this one
    {% import "example.html" %}     --  TBA

    {% extends "example.html" %}    --  calls a parent, path is relative, do not forget quotes
    {% block blockname %}           --  declares a block on the parent side or fills it              >
    {% endblock blockname %}        --  on the child's side (parent should have declared it first)   |
Useful blocks to create:
    meta    --  meta info
    head    --  still within meta, but below title (subtitle, etx)
    main    --  main block
    script  --  script block (best import from static/js)
Conditional:
    {% if STATEMENT %}
        HTML & JINJA code 
    {% else %}
        HTML & JINJA code
    {% endif %}
Loops:
    {% for STATEMENT %}
        HTML & JINJA code
    {% endfor %}
    {{ loop.index0 }}   --  0 based index
    {{ loop.index }}    --  1 based index
Setter:
    {% set variable = value %}  --  set a variable to a value
"""