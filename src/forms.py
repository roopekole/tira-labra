from flask_wtf import FlaskForm
from wtforms import IntegerField, BooleanField, validators


class MapForm(FlaskForm):
    """
    Form class to pass the map, the coordinates and the algorithmic selection
    """
    start_x = IntegerField('X:', [validators.number_range(min=0, max=256)],
                           render_kw={"id": "start_x", "class": "form-control"})
    start_y = IntegerField('Y:', [validators.number_range(min=0, max=256)],
                           render_kw={"id": "start_y", "class": "form-control"})
    end_x = IntegerField('X:', [validators.number_range(min=0, max=256)],
                         render_kw={"id": "end_x", "class": "form-control"})
    end_y = IntegerField('Y:', [validators.number_range(min=0, max=256)],
                         render_kw={"id": "end_y", "class": "form-control"})
    jps = BooleanField("JPS", render_kw={"checked":"True"})
    ida = BooleanField("IDA*", render_kw={"checked":"True"})
    a_star = BooleanField("A*", render_kw={"disabled src":""}, )

    class Meta:
        """
        Meta class for Flaskform
        """
        csrf = False
