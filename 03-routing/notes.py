"""
flask.render_template(path{str}, **kwargs)    
    --  renders template in the template_folder of a Flask instance
    --  remember to declare subfolders too in path
flask.url_for(funcion_name{str}, **kwargs, _external=False)
    -- gets url for the given routed function
    -- can pass arbitrary kwargs (eg. an id), that are taken by a routed function as positional
    -- should also be used for static files, eg:
        <link href="{{ url_for('static', filename='css/bootstrap.css') }}" rel="stylesheet">
    -- _external=True generates absolute url
return flask.redirect(url{str})
    -- ONLY WORKS W/ RETURN
    -- redirects for given url
    -- use in conjunction w/ flask.url_for()
"""
