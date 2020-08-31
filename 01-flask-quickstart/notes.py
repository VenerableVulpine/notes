"""
flask-quickstart app structure:
    ROOT
    -- main.py              <-- the entry point of the app
    -- config.py            <-- separates config for ease of use
    -- WEBSITE              <-- actual content goes here
        -- __init__.py      <-- creates the app and imports modules before we do anything
        -- routing.py       <-- handles url-function pairing
        -- forms.py         <-- separates forms for ease of use
        -- models.py        <-- separates database models for ease of use
        -- STATIC           <-- files to be served along w/ the website
            -- CSS
                -- (OPT)bootstrap.min.css   <-- a CDN is recommended instead
                -- site.css                 <-- if you have custom css 
            -- JS
        -- TEMPLATES            <-- JINJA templating here
            -- PAGES            <-- you'll use these in render_template directly
                -- page1.html
                -- page2.html
                -- ...
            -- base1.html        <-- pages inherit from these
            -- base2.html        <-- pages inherit from these

The reason for using this will become clear later.
Much simpler structures are possible (you can create an entire app in a single file),
but as projects grow maintainence would become cumbersome.

https://en.wikipedia.org/wiki/Separation_of_concerns
"""
