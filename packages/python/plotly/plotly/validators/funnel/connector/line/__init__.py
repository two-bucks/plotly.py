import _plotly_utils.basevalidators


class WidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="width", parent_name="funnel.connector.line", **kwargs
    ):
        super(WidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DashValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="dash", parent_name="funnel.connector.line", **kwargs
    ):
        super(DashValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop(
                "values", ["solid", "dot", "dash", "longdash", "dashdot", "longdashdot"]
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="color", parent_name="funnel.connector.line", **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )