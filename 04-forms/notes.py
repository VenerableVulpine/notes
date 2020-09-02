"""
----------------


flask_wtf & wtforms
NOTE: this is a flask wrapper around the wtforms (but you have to import both)

$ pip install WTForms
$ pip install Flask-WTF

flask_wtf.FlaskForm
    -- superclass for froms, inside which wtforms Fields reside

Inputs:
        -- assingn the field to a variable, ans use the variable's name (NOT field_name) in JINJA
        -- wtforms.fields.core
                -- this is what FlaskForm returns
                -- wrap this in an HTML <form>, <input>-s not required
            in JINJA:
            -- REQUIRES .<form_name>.hidden_tag() first in JINJA  
            -- .<variable_name>.label          -- field_name in JINJA
            -- .<variable_name>(size={int}, **kwargs)    
                -- renders <input> fields automatically
                -- can add any html argument as a kwarg, useful example include:
                    -- style ="CUSTOMCSS;"
                    -- class_="CLASSNAME    
                        -- NOTE: watch the undescore, class is a reserved python name
                    -- input whitespaces are generally preserved
                       to display them properly, use in the output CSS style::
                        -- white-space: pre-line; whitespace trimmed to single whitespace
                        -- white-space: pre-wrap; all whitespace preserved
                     
            -- .submit()                       -- renders SubmitField <input type='submit'> 
                -- wtforms.SubmitField has to be created for FlaskForm
            in python:
            -- .validate_on_submit()
                -- use in routing function as "if <form_name>.validate_on_submit(): DO SMTHNG"
            -- .<variable_name>.data           -- data entered in field
            -- .<variable_name>                -- returns entire html input tag
        -- validators always passed in a list
    Fields:
        wtforms.StringField         (field_name{str}, validators=[])
        wtforms.PasswordField       (field_name{str}, validators=[])
        wtforms.TextAreaField       (field_name{str}, validators=[])
        wtforms.SelectField         (field_name{str}, choices=[{tuple of 2 str}...])    -- TODO
            -- in choices is like this: choices=[('cpp', 'C++'), ('py', 'Python'))]
        wtforms.SelectMultipleField (field_name{str}) -- TODO
        wtforms.BooleanField        (field_name{str})
        wtforms.SubmitField         (field_name{str})
    Validators:
        wtforms.validators.DataRequired()
        wtforms.validators.EuqalTo(fieldname{str}, message{str}=None???)
            fieldname       -- python variable name converted to string
            message         -- message raised on mismatch (unknown default)
        wtforms.validators.InputRequired()
        wtforms.validators.Length(min=-1, max=-1, message=None)
...

"""