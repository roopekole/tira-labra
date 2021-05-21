from flask_wtf import FlaskForm
from wtforms import IntegerField, BooleanField, validators


class MapForm(FlaskForm):
    start_x = IntegerField('X:', [validators.NumberRange(min=0, max=330)], render_kw={"disabled id": "start_x", "class": "form-control"})
    start_y = IntegerField('Y:', [validators.NumberRange(min=0, max=330)], render_kw={"disabled id": "start_y", "class": "form-control"})
    end_x = IntegerField('X:', [validators.NumberRange(min=0, max=330)], render_kw={"disabled id": "end_x", "class": "form-control"})
    end_y = IntegerField('Y:', [validators.NumberRange(min=0, max=330)], render_kw={"disabled id": "end_y", "class": "form-control"})
    jps = BooleanField("JPS", render_kw={"checked":"True"})
    ida = BooleanField("IDA*", render_kw={"checked":"True"})
    a_star = BooleanField("A*", render_kw={"disabled src":""}, )

    class Meta:
        csrf = False