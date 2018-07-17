from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Baxis(BaseTraceHierarchyType):

    # arraydtick
    # ----------
    @property
    def arraydtick(self):
        """
        The stride between grid lines along the axis
    
        The 'arraydtick' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['arraydtick']

    @arraydtick.setter
    def arraydtick(self, val):
        self['arraydtick'] = val

    # arraytick0
    # ----------
    @property
    def arraytick0(self):
        """
        The starting index of grid lines along the axis
    
        The 'arraytick0' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['arraytick0']

    @arraytick0.setter
    def arraytick0(self, val):
        self['arraytick0'] = val

    # autorange
    # ---------
    @property
    def autorange(self):
        """
        Determines whether or not the range of this axis is computed in
        relation to the input data. See `rangemode` for more info. If
        `range` is provided, then `autorange` is set to *false*.
    
        The 'autorange' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'reversed']

        Returns
        -------
        Any
        """
        return self['autorange']

    @autorange.setter
    def autorange(self, val):
        self['autorange'] = val

    # categoryarray
    # -------------
    @property
    def categoryarray(self):
        """
        Sets the order in which categories on this axis appear. Only
        has an effect if `categoryorder` is set to *array*. Used with
        `categoryorder`.
    
        The 'categoryarray' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['categoryarray']

    @categoryarray.setter
    def categoryarray(self, val):
        self['categoryarray'] = val

    # categoryarraysrc
    # ----------------
    @property
    def categoryarraysrc(self):
        """
        Sets the source reference on plot.ly for  categoryarray .
    
        The 'categoryarraysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['categoryarraysrc']

    @categoryarraysrc.setter
    def categoryarraysrc(self, val):
        self['categoryarraysrc'] = val

    # categoryorder
    # -------------
    @property
    def categoryorder(self):
        """
        Specifies the ordering logic for the case of categorical
        variables. By default, plotly uses *trace*, which specifies the
        order that is present in the data supplied. Set `categoryorder`
        to *category ascending* or *category descending* if order
        should be determined by the alphanumerical order of the
        category names. Set `categoryorder` to *array* to derive the
        ordering from the attribute `categoryarray`. If a category is
        not found in the `categoryarray` array, the sorting behavior
        for that attribute will be identical to the *trace* mode. The
        unspecified categories will follow the categories in
        `categoryarray`.
    
        The 'categoryorder' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['trace', 'category ascending', 'category descending',
                'array']

        Returns
        -------
        Any
        """
        return self['categoryorder']

    @categoryorder.setter
    def categoryorder(self, val):
        self['categoryorder'] = val

    # cheatertype
    # -----------
    @property
    def cheatertype(self):
        """
        The 'cheatertype' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['index', 'value']

        Returns
        -------
        Any
        """
        return self['cheatertype']

    @cheatertype.setter
    def cheatertype(self, val):
        self['cheatertype'] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets default for all colors associated with this axis all at
        once: line, font, tick, and grid colors. Grid color is
        lightened by blending this with the plot background Individual
        pieces can override this.
    
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # dtick
    # -----
    @property
    def dtick(self):
        """
        The stride between grid lines along the axis
    
        The 'dtick' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['dtick']

    @dtick.setter
    def dtick(self, val):
        self['dtick'] = val

    # endline
    # -------
    @property
    def endline(self):
        """
        Determines whether or not a line is drawn at along the final
        value of this axis. If *true*, the end line is drawn on top of
        the grid lines.
    
        The 'endline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['endline']

    @endline.setter
    def endline(self, val):
        self['endline'] = val

    # endlinecolor
    # ------------
    @property
    def endlinecolor(self):
        """
        Sets the line color of the end line.
    
        The 'endlinecolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['endlinecolor']

    @endlinecolor.setter
    def endlinecolor(self, val):
        self['endlinecolor'] = val

    # endlinewidth
    # ------------
    @property
    def endlinewidth(self):
        """
        Sets the width (in px) of the end line.
    
        The 'endlinewidth' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['endlinewidth']

    @endlinewidth.setter
    def endlinewidth(self, val):
        self['endlinewidth'] = val

    # exponentformat
    # --------------
    @property
    def exponentformat(self):
        """
        Determines a formatting rule for the tick exponents. For
        example, consider the number 1,000,000,000. If *none*, it
        appears as 1,000,000,000. If *e*, 1e+9. If *E*, 1E+9. If
        *power*, 1x10^9 (with 9 in a super script). If *SI*, 1G. If
        *B*, 1B.
    
        The 'exponentformat' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['none', 'e', 'E', 'power', 'SI', 'B']

        Returns
        -------
        Any
        """
        return self['exponentformat']

    @exponentformat.setter
    def exponentformat(self, val):
        self['exponentformat'] = val

    # fixedrange
    # ----------
    @property
    def fixedrange(self):
        """
        Determines whether or not this axis is zoom-able. If true, then
        zoom is disabled.
    
        The 'fixedrange' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['fixedrange']

    @fixedrange.setter
    def fixedrange(self, val):
        self['fixedrange'] = val

    # gridcolor
    # ---------
    @property
    def gridcolor(self):
        """
        Sets the axis line color.
    
        The 'gridcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['gridcolor']

    @gridcolor.setter
    def gridcolor(self, val):
        self['gridcolor'] = val

    # gridwidth
    # ---------
    @property
    def gridwidth(self):
        """
        Sets the width (in px) of the axis line.
    
        The 'gridwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['gridwidth']

    @gridwidth.setter
    def gridwidth(self, val):
        self['gridwidth'] = val

    # labelpadding
    # ------------
    @property
    def labelpadding(self):
        """
        Extra padding between label and the axis
    
        The 'labelpadding' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)

        Returns
        -------
        int
        """
        return self['labelpadding']

    @labelpadding.setter
    def labelpadding(self, val):
        self['labelpadding'] = val

    # labelprefix
    # -----------
    @property
    def labelprefix(self):
        """
        Sets a axis label prefix.
    
        The 'labelprefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['labelprefix']

    @labelprefix.setter
    def labelprefix(self, val):
        self['labelprefix'] = val

    # labelsuffix
    # -----------
    @property
    def labelsuffix(self):
        """
        Sets a axis label suffix.
    
        The 'labelsuffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['labelsuffix']

    @labelsuffix.setter
    def labelsuffix(self, val):
        self['labelsuffix'] = val

    # linecolor
    # ---------
    @property
    def linecolor(self):
        """
        Sets the axis line color.
    
        The 'linecolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['linecolor']

    @linecolor.setter
    def linecolor(self, val):
        self['linecolor'] = val

    # linewidth
    # ---------
    @property
    def linewidth(self):
        """
        Sets the width (in px) of the axis line.
    
        The 'linewidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['linewidth']

    @linewidth.setter
    def linewidth(self, val):
        self['linewidth'] = val

    # minorgridcolor
    # --------------
    @property
    def minorgridcolor(self):
        """
        Sets the color of the grid lines.
    
        The 'minorgridcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['minorgridcolor']

    @minorgridcolor.setter
    def minorgridcolor(self, val):
        self['minorgridcolor'] = val

    # minorgridcount
    # --------------
    @property
    def minorgridcount(self):
        """
        Sets the number of minor grid ticks per major grid tick
    
        The 'minorgridcount' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['minorgridcount']

    @minorgridcount.setter
    def minorgridcount(self, val):
        self['minorgridcount'] = val

    # minorgridwidth
    # --------------
    @property
    def minorgridwidth(self):
        """
        Sets the width (in px) of the grid lines.
    
        The 'minorgridwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['minorgridwidth']

    @minorgridwidth.setter
    def minorgridwidth(self, val):
        self['minorgridwidth'] = val

    # nticks
    # ------
    @property
    def nticks(self):
        """
        Specifies the maximum number of ticks for the particular axis.
        The actual number of ticks will be chosen automatically to be
        less than or equal to `nticks`. Has an effect only if
        `tickmode` is set to *auto*.
    
        The 'nticks' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['nticks']

    @nticks.setter
    def nticks(self, val):
        self['nticks'] = val

    # range
    # -----
    @property
    def range(self):
        """
        Sets the range of this axis. If the axis `type` is *log*, then
        you must take the log of your desired range (e.g. to set the
        range from 1 to 100, set the range from 0 to 2). If the axis
        `type` is *date*, it should be date strings, like date data,
        though Date objects and unix milliseconds will be accepted and
        converted to strings. If the axis `type` is *category*, it
        should be numbers, using the scale where each category is
        assigned a serial number from zero in the order it appears.
    
        The 'range' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'range[0]' property accepts values of any type
    (1) The 'range[1]' property accepts values of any type

        Returns
        -------
        list
        """
        return self['range']

    @range.setter
    def range(self, val):
        self['range'] = val

    # rangemode
    # ---------
    @property
    def rangemode(self):
        """
        If *normal*, the range is computed in relation to the extrema
        of the input data. If *tozero*`, the range extends to 0,
        regardless of the input data If *nonnegative*, the range is
        non-negative, regardless of the input data.
    
        The 'rangemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'tozero', 'nonnegative']

        Returns
        -------
        Any
        """
        return self['rangemode']

    @rangemode.setter
    def rangemode(self, val):
        self['rangemode'] = val

    # separatethousands
    # -----------------
    @property
    def separatethousands(self):
        """
        If "true", even 4-digit integers are separated
    
        The 'separatethousands' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['separatethousands']

    @separatethousands.setter
    def separatethousands(self, val):
        self['separatethousands'] = val

    # showexponent
    # ------------
    @property
    def showexponent(self):
        """
        If *all*, all exponents are shown besides their significands.
        If *first*, only the exponent of the first tick is shown. If
        *last*, only the exponent of the last tick is shown. If *none*,
        no exponents appear.
    
        The 'showexponent' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self['showexponent']

    @showexponent.setter
    def showexponent(self, val):
        self['showexponent'] = val

    # showgrid
    # --------
    @property
    def showgrid(self):
        """
        Determines whether or not grid lines are drawn. If *true*, the
        grid lines are drawn at every tick mark.
    
        The 'showgrid' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showgrid']

    @showgrid.setter
    def showgrid(self, val):
        self['showgrid'] = val

    # showline
    # --------
    @property
    def showline(self):
        """
        Determines whether or not a line bounding this axis is drawn.
    
        The 'showline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showline']

    @showline.setter
    def showline(self, val):
        self['showline'] = val

    # showticklabels
    # --------------
    @property
    def showticklabels(self):
        """
        Determines whether axis labels are drawn on the low side, the
        high side, both, or neither side of the axis.
    
        The 'showticklabels' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['start', 'end', 'both', 'none']

        Returns
        -------
        Any
        """
        return self['showticklabels']

    @showticklabels.setter
    def showticklabels(self, val):
        self['showticklabels'] = val

    # showtickprefix
    # --------------
    @property
    def showtickprefix(self):
        """
        If *all*, all tick labels are displayed with a prefix. If
        *first*, only the first tick is displayed with a prefix. If
        *last*, only the last tick is displayed with a suffix. If
        *none*, tick prefixes are hidden.
    
        The 'showtickprefix' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self['showtickprefix']

    @showtickprefix.setter
    def showtickprefix(self, val):
        self['showtickprefix'] = val

    # showticksuffix
    # --------------
    @property
    def showticksuffix(self):
        """
        Same as `showtickprefix` but for tick suffixes.
    
        The 'showticksuffix' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self['showticksuffix']

    @showticksuffix.setter
    def showticksuffix(self, val):
        self['showticksuffix'] = val

    # smoothing
    # ---------
    @property
    def smoothing(self):
        """
        The 'smoothing' property is a number and may be specified as:
          - An int or float in the interval [0, 1.3]

        Returns
        -------
        int|float
        """
        return self['smoothing']

    @smoothing.setter
    def smoothing(self, val):
        self['smoothing'] = val

    # startline
    # ---------
    @property
    def startline(self):
        """
        Determines whether or not a line is drawn at along the starting
        value of this axis. If *true*, the start line is drawn on top
        of the grid lines.
    
        The 'startline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['startline']

    @startline.setter
    def startline(self, val):
        self['startline'] = val

    # startlinecolor
    # --------------
    @property
    def startlinecolor(self):
        """
        Sets the line color of the start line.
    
        The 'startlinecolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['startlinecolor']

    @startlinecolor.setter
    def startlinecolor(self, val):
        self['startlinecolor'] = val

    # startlinewidth
    # --------------
    @property
    def startlinewidth(self):
        """
        Sets the width (in px) of the start line.
    
        The 'startlinewidth' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['startlinewidth']

    @startlinewidth.setter
    def startlinewidth(self, val):
        self['startlinewidth'] = val

    # tick0
    # -----
    @property
    def tick0(self):
        """
        The starting index of grid lines along the axis
    
        The 'tick0' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['tick0']

    @tick0.setter
    def tick0(self, val):
        self['tick0'] = val

    # tickangle
    # ---------
    @property
    def tickangle(self):
        """
        Sets the angle of the tick labels with respect to the
        horizontal. For example, a `tickangle` of -90 draws the tick
        labels vertically.
    
        The 'tickangle' property is a angle (in degrees) that may be
        specified as a number between -180 and 180. Numeric values outside this
        range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self['tickangle']

    @tickangle.setter
    def tickangle(self, val):
        self['tickangle'] = val

    # tickfont
    # --------
    @property
    def tickfont(self):
        """
        Sets the tick font.
    
        The 'tickfont' property is an instance of Tickfont
        that may be specified as:
          - An instance of plotly.graph_objs.carpet.baxis.Tickfont
          - A dict of string/value properties that will be passed
            to the Tickfont constructor
    
            Supported dict properties:
                
                color
    
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include *Arial*,
                    *Balto*, *Courier New*, *Droid Sans*,, *Droid
                    Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
                    Standard TT*, *Open Sans*, *Overpass*, *PT Sans
                    Narrow*, *Raleway*, *Times New Roman*.
                size

        Returns
        -------
        plotly.graph_objs.carpet.baxis.Tickfont
        """
        return self['tickfont']

    @tickfont.setter
    def tickfont(self, val):
        self['tickfont'] = val

    # tickformat
    # ----------
    @property
    def tickformat(self):
        """
        Sets the tick label formatting rule using d3 formatting mini-
        languages which are very similar to those in Python. For
        numbers, see: https://github.com/d3/d3-format/blob/master/READM
        E.md#locale_format And for dates see:
        https://github.com/d3/d3-time-
        format/blob/master/README.md#locale_format We add one item to
        d3's date formatter: *%{n}f* for fractional seconds with n
        digits. For example, *2016-10-13 09:15:23.456* with tickformat
        *%H~%M~%S.%2f* would display *09~15~23.46*
    
        The 'tickformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['tickformat']

    @tickformat.setter
    def tickformat(self, val):
        self['tickformat'] = val

    # tickformatstops
    # ---------------
    @property
    def tickformatstops(self):
        """
        The 'tickformatstops' property is a tuple of instances of
        Tickformatstop that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.carpet.baxis.Tickformatstop
          - A list or tuple of dicts of string/value properties that
            will be passed to the Tickformatstop constructor
    
            Supported dict properties:
                
                dtickrange
                    range [*min*, *max*], where *min*, *max* -
                    dtick values which describe some zoom level, it
                    is possible to omit *min* or *max* value by
                    passing *null*
                value
                    string - dtickformat for described zoom level,
                    the same as *tickformat*

        Returns
        -------
        tuple[plotly.graph_objs.carpet.baxis.Tickformatstop]
        """
        return self['tickformatstops']

    @tickformatstops.setter
    def tickformatstops(self, val):
        self['tickformatstops'] = val

    # tickmode
    # --------
    @property
    def tickmode(self):
        """
        The 'tickmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['linear', 'array']

        Returns
        -------
        Any
        """
        return self['tickmode']

    @tickmode.setter
    def tickmode(self, val):
        self['tickmode'] = val

    # tickprefix
    # ----------
    @property
    def tickprefix(self):
        """
        Sets a tick label prefix.
    
        The 'tickprefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['tickprefix']

    @tickprefix.setter
    def tickprefix(self, val):
        self['tickprefix'] = val

    # ticksuffix
    # ----------
    @property
    def ticksuffix(self):
        """
        Sets a tick label suffix.
    
        The 'ticksuffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['ticksuffix']

    @ticksuffix.setter
    def ticksuffix(self, val):
        self['ticksuffix'] = val

    # ticktext
    # --------
    @property
    def ticktext(self):
        """
        Sets the text displayed at the ticks position via `tickvals`.
        Only has an effect if `tickmode` is set to *array*. Used with
        `tickvals`.
    
        The 'ticktext' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['ticktext']

    @ticktext.setter
    def ticktext(self, val):
        self['ticktext'] = val

    # ticktextsrc
    # -----------
    @property
    def ticktextsrc(self):
        """
        Sets the source reference on plot.ly for  ticktext .
    
        The 'ticktextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['ticktextsrc']

    @ticktextsrc.setter
    def ticktextsrc(self, val):
        self['ticktextsrc'] = val

    # tickvals
    # --------
    @property
    def tickvals(self):
        """
        Sets the values at which ticks on this axis appear. Only has an
        effect if `tickmode` is set to *array*. Used with `ticktext`.
    
        The 'tickvals' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['tickvals']

    @tickvals.setter
    def tickvals(self, val):
        self['tickvals'] = val

    # tickvalssrc
    # -----------
    @property
    def tickvalssrc(self):
        """
        Sets the source reference on plot.ly for  tickvals .
    
        The 'tickvalssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['tickvalssrc']

    @tickvalssrc.setter
    def tickvalssrc(self, val):
        self['tickvalssrc'] = val

    # title
    # -----
    @property
    def title(self):
        """
        Sets the title of this axis.
    
        The 'title' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['title']

    @title.setter
    def title(self, val):
        self['title'] = val

    # titlefont
    # ---------
    @property
    def titlefont(self):
        """
        Sets this axis' title font.
    
        The 'titlefont' property is an instance of Titlefont
        that may be specified as:
          - An instance of plotly.graph_objs.carpet.baxis.Titlefont
          - A dict of string/value properties that will be passed
            to the Titlefont constructor
    
            Supported dict properties:
                
                color
    
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include *Arial*,
                    *Balto*, *Courier New*, *Droid Sans*,, *Droid
                    Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
                    Standard TT*, *Open Sans*, *Overpass*, *PT Sans
                    Narrow*, *Raleway*, *Times New Roman*.
                size

        Returns
        -------
        plotly.graph_objs.carpet.baxis.Titlefont
        """
        return self['titlefont']

    @titlefont.setter
    def titlefont(self, val):
        self['titlefont'] = val

    # titleoffset
    # -----------
    @property
    def titleoffset(self):
        """
        An additional amount by which to offset the title from the tick
        labels, given in pixels
    
        The 'titleoffset' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['titleoffset']

    @titleoffset.setter
    def titleoffset(self, val):
        self['titleoffset'] = val

    # type
    # ----
    @property
    def type(self):
        """
        Sets the axis type. By default, plotly attempts to determined
        the axis type by looking into the data of the traces that
        referenced the axis in question.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['-', 'linear', 'date', 'category']

        Returns
        -------
        Any
        """
        return self['type']

    @type.setter
    def type(self, val):
        self['type'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'carpet'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        arraydtick
            The stride between grid lines along the axis
        arraytick0
            The starting index of grid lines along the axis
        autorange
            Determines whether or not the range of this axis is
            computed in relation to the input data. See `rangemode`
            for more info. If `range` is provided, then `autorange`
            is set to *false*.
        categoryarray
            Sets the order in which categories on this axis appear.
            Only has an effect if `categoryorder` is set to
            *array*. Used with `categoryorder`.
        categoryarraysrc
            Sets the source reference on plot.ly for  categoryarray
            .
        categoryorder
            Specifies the ordering logic for the case of
            categorical variables. By default, plotly uses *trace*,
            which specifies the order that is present in the data
            supplied. Set `categoryorder` to *category ascending*
            or *category descending* if order should be determined
            by the alphanumerical order of the category names. Set
            `categoryorder` to *array* to derive the ordering from
            the attribute `categoryarray`. If a category is not
            found in the `categoryarray` array, the sorting
            behavior for that attribute will be identical to the
            *trace* mode. The unspecified categories will follow
            the categories in `categoryarray`.
        cheatertype

        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        dtick
            The stride between grid lines along the axis
        endline
            Determines whether or not a line is drawn at along the
            final value of this axis. If *true*, the end line is
            drawn on top of the grid lines.
        endlinecolor
            Sets the line color of the end line.
        endlinewidth
            Sets the width (in px) of the end line.
        exponentformat
            Determines a formatting rule for the tick exponents.
            For example, consider the number 1,000,000,000. If
            *none*, it appears as 1,000,000,000. If *e*, 1e+9. If
            *E*, 1E+9. If *power*, 1x10^9 (with 9 in a super
            script). If *SI*, 1G. If *B*, 1B.
        fixedrange
            Determines whether or not this axis is zoom-able. If
            true, then zoom is disabled.
        gridcolor
            Sets the axis line color.
        gridwidth
            Sets the width (in px) of the axis line.
        labelpadding
            Extra padding between label and the axis
        labelprefix
            Sets a axis label prefix.
        labelsuffix
            Sets a axis label suffix.
        linecolor
            Sets the axis line color.
        linewidth
            Sets the width (in px) of the axis line.
        minorgridcolor
            Sets the color of the grid lines.
        minorgridcount
            Sets the number of minor grid ticks per major grid tick
        minorgridwidth
            Sets the width (in px) of the grid lines.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            *auto*.
        range
            Sets the range of this axis. If the axis `type` is
            *log*, then you must take the log of your desired range
            (e.g. to set the range from 1 to 100, set the range
            from 0 to 2). If the axis `type` is *date*, it should
            be date strings, like date data, though Date objects
            and unix milliseconds will be accepted and converted to
            strings. If the axis `type` is *category*, it should be
            numbers, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        rangemode
            If *normal*, the range is computed in relation to the
            extrema of the input data. If *tozero*`, the range
            extends to 0, regardless of the input data If
            *nonnegative*, the range is non-negative, regardless of
            the input data.
        separatethousands
            If "true", even 4-digit integers are separated
        showexponent
            If *all*, all exponents are shown besides their
            significands. If *first*, only the exponent of the
            first tick is shown. If *last*, only the exponent of
            the last tick is shown. If *none*, no exponents appear.
        showgrid
            Determines whether or not grid lines are drawn. If
            *true*, the grid lines are drawn at every tick mark.
        showline
            Determines whether or not a line bounding this axis is
            drawn.
        showticklabels
            Determines whether axis labels are drawn on the low
            side, the high side, both, or neither side of the axis.
        showtickprefix
            If *all*, all tick labels are displayed with a prefix.
            If *first*, only the first tick is displayed with a
            prefix. If *last*, only the last tick is displayed with
            a suffix. If *none*, tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        smoothing

        startline
            Determines whether or not a line is drawn at along the
            starting value of this axis. If *true*, the start line
            is drawn on top of the grid lines.
        startlinecolor
            Sets the line color of the start line.
        startlinewidth
            Sets the width (in px) of the start line.
        tick0
            The starting index of grid lines along the axis
        tickangle
            Sets the angle of the tick labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            tick labels vertically.
        tickfont
            Sets the tick font.
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see: https://github.com/d3/d3-form
            at/blob/master/README.md#locale_format And for dates
            see: https://github.com/d3/d3-time-
            format/blob/master/README.md#locale_format We add one
            item to d3's date formatter: *%{n}f* for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat *%H~%M~%S.%2f* would
            display *09~15~23.46*
        tickformatstops
            plotly.graph_objs.carpet.baxis.Tickformatstop instance
            or dict with compatible properties
        tickmode

        tickprefix
            Sets a tick label prefix.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            *array*. Used with `tickvals`.
        ticktextsrc
            Sets the source reference on plot.ly for  ticktext .
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to *array*.
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on plot.ly for  tickvals .
        title
            Sets the title of this axis.
        titlefont
            Sets this axis' title font.
        titleoffset
            An additional amount by which to offset the title from
            the tick labels, given in pixels
        type
            Sets the axis type. By default, plotly attempts to
            determined the axis type by looking into the data of
            the traces that referenced the axis in question.
        """

    def __init__(
        self,
        arg=None,
        arraydtick=None,
        arraytick0=None,
        autorange=None,
        categoryarray=None,
        categoryarraysrc=None,
        categoryorder=None,
        cheatertype=None,
        color=None,
        dtick=None,
        endline=None,
        endlinecolor=None,
        endlinewidth=None,
        exponentformat=None,
        fixedrange=None,
        gridcolor=None,
        gridwidth=None,
        labelpadding=None,
        labelprefix=None,
        labelsuffix=None,
        linecolor=None,
        linewidth=None,
        minorgridcolor=None,
        minorgridcount=None,
        minorgridwidth=None,
        nticks=None,
        range=None,
        rangemode=None,
        separatethousands=None,
        showexponent=None,
        showgrid=None,
        showline=None,
        showticklabels=None,
        showtickprefix=None,
        showticksuffix=None,
        smoothing=None,
        startline=None,
        startlinecolor=None,
        startlinewidth=None,
        tick0=None,
        tickangle=None,
        tickfont=None,
        tickformat=None,
        tickformatstops=None,
        tickmode=None,
        tickprefix=None,
        ticksuffix=None,
        ticktext=None,
        ticktextsrc=None,
        tickvals=None,
        tickvalssrc=None,
        title=None,
        titlefont=None,
        titleoffset=None,
        type=None,
        **kwargs
    ):
        """
        Construct a new Baxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.carpet.Baxis
        arraydtick
            The stride between grid lines along the axis
        arraytick0
            The starting index of grid lines along the axis
        autorange
            Determines whether or not the range of this axis is
            computed in relation to the input data. See `rangemode`
            for more info. If `range` is provided, then `autorange`
            is set to *false*.
        categoryarray
            Sets the order in which categories on this axis appear.
            Only has an effect if `categoryorder` is set to
            *array*. Used with `categoryorder`.
        categoryarraysrc
            Sets the source reference on plot.ly for  categoryarray
            .
        categoryorder
            Specifies the ordering logic for the case of
            categorical variables. By default, plotly uses *trace*,
            which specifies the order that is present in the data
            supplied. Set `categoryorder` to *category ascending*
            or *category descending* if order should be determined
            by the alphanumerical order of the category names. Set
            `categoryorder` to *array* to derive the ordering from
            the attribute `categoryarray`. If a category is not
            found in the `categoryarray` array, the sorting
            behavior for that attribute will be identical to the
            *trace* mode. The unspecified categories will follow
            the categories in `categoryarray`.
        cheatertype

        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        dtick
            The stride between grid lines along the axis
        endline
            Determines whether or not a line is drawn at along the
            final value of this axis. If *true*, the end line is
            drawn on top of the grid lines.
        endlinecolor
            Sets the line color of the end line.
        endlinewidth
            Sets the width (in px) of the end line.
        exponentformat
            Determines a formatting rule for the tick exponents.
            For example, consider the number 1,000,000,000. If
            *none*, it appears as 1,000,000,000. If *e*, 1e+9. If
            *E*, 1E+9. If *power*, 1x10^9 (with 9 in a super
            script). If *SI*, 1G. If *B*, 1B.
        fixedrange
            Determines whether or not this axis is zoom-able. If
            true, then zoom is disabled.
        gridcolor
            Sets the axis line color.
        gridwidth
            Sets the width (in px) of the axis line.
        labelpadding
            Extra padding between label and the axis
        labelprefix
            Sets a axis label prefix.
        labelsuffix
            Sets a axis label suffix.
        linecolor
            Sets the axis line color.
        linewidth
            Sets the width (in px) of the axis line.
        minorgridcolor
            Sets the color of the grid lines.
        minorgridcount
            Sets the number of minor grid ticks per major grid tick
        minorgridwidth
            Sets the width (in px) of the grid lines.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            *auto*.
        range
            Sets the range of this axis. If the axis `type` is
            *log*, then you must take the log of your desired range
            (e.g. to set the range from 1 to 100, set the range
            from 0 to 2). If the axis `type` is *date*, it should
            be date strings, like date data, though Date objects
            and unix milliseconds will be accepted and converted to
            strings. If the axis `type` is *category*, it should be
            numbers, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        rangemode
            If *normal*, the range is computed in relation to the
            extrema of the input data. If *tozero*`, the range
            extends to 0, regardless of the input data If
            *nonnegative*, the range is non-negative, regardless of
            the input data.
        separatethousands
            If "true", even 4-digit integers are separated
        showexponent
            If *all*, all exponents are shown besides their
            significands. If *first*, only the exponent of the
            first tick is shown. If *last*, only the exponent of
            the last tick is shown. If *none*, no exponents appear.
        showgrid
            Determines whether or not grid lines are drawn. If
            *true*, the grid lines are drawn at every tick mark.
        showline
            Determines whether or not a line bounding this axis is
            drawn.
        showticklabels
            Determines whether axis labels are drawn on the low
            side, the high side, both, or neither side of the axis.
        showtickprefix
            If *all*, all tick labels are displayed with a prefix.
            If *first*, only the first tick is displayed with a
            prefix. If *last*, only the last tick is displayed with
            a suffix. If *none*, tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        smoothing

        startline
            Determines whether or not a line is drawn at along the
            starting value of this axis. If *true*, the start line
            is drawn on top of the grid lines.
        startlinecolor
            Sets the line color of the start line.
        startlinewidth
            Sets the width (in px) of the start line.
        tick0
            The starting index of grid lines along the axis
        tickangle
            Sets the angle of the tick labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            tick labels vertically.
        tickfont
            Sets the tick font.
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see: https://github.com/d3/d3-form
            at/blob/master/README.md#locale_format And for dates
            see: https://github.com/d3/d3-time-
            format/blob/master/README.md#locale_format We add one
            item to d3's date formatter: *%{n}f* for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat *%H~%M~%S.%2f* would
            display *09~15~23.46*
        tickformatstops
            plotly.graph_objs.carpet.baxis.Tickformatstop instance
            or dict with compatible properties
        tickmode

        tickprefix
            Sets a tick label prefix.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            *array*. Used with `tickvals`.
        ticktextsrc
            Sets the source reference on plot.ly for  ticktext .
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to *array*.
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on plot.ly for  tickvals .
        title
            Sets the title of this axis.
        titlefont
            Sets this axis' title font.
        titleoffset
            An additional amount by which to offset the title from
            the tick labels, given in pixels
        type
            Sets the axis type. By default, plotly attempts to
            determined the axis type by looking into the data of
            the traces that referenced the axis in question.

        Returns
        -------
        Baxis
        """
        super(Baxis, self).__init__('baxis')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.carpet.Baxis 
constructor must be a dict or 
an instance of plotly.graph_objs.carpet.Baxis"""
            )

        # Import validators
        # -----------------
        from plotly.validators.carpet import (baxis as v_baxis)

        # Initialize validators
        # ---------------------
        self._validators['arraydtick'] = v_baxis.ArraydtickValidator()
        self._validators['arraytick0'] = v_baxis.Arraytick0Validator()
        self._validators['autorange'] = v_baxis.AutorangeValidator()
        self._validators['categoryarray'] = v_baxis.CategoryarrayValidator()
        self._validators['categoryarraysrc'
                        ] = v_baxis.CategoryarraysrcValidator()
        self._validators['categoryorder'] = v_baxis.CategoryorderValidator()
        self._validators['cheatertype'] = v_baxis.CheatertypeValidator()
        self._validators['color'] = v_baxis.ColorValidator()
        self._validators['dtick'] = v_baxis.DtickValidator()
        self._validators['endline'] = v_baxis.EndlineValidator()
        self._validators['endlinecolor'] = v_baxis.EndlinecolorValidator()
        self._validators['endlinewidth'] = v_baxis.EndlinewidthValidator()
        self._validators['exponentformat'] = v_baxis.ExponentformatValidator()
        self._validators['fixedrange'] = v_baxis.FixedrangeValidator()
        self._validators['gridcolor'] = v_baxis.GridcolorValidator()
        self._validators['gridwidth'] = v_baxis.GridwidthValidator()
        self._validators['labelpadding'] = v_baxis.LabelpaddingValidator()
        self._validators['labelprefix'] = v_baxis.LabelprefixValidator()
        self._validators['labelsuffix'] = v_baxis.LabelsuffixValidator()
        self._validators['linecolor'] = v_baxis.LinecolorValidator()
        self._validators['linewidth'] = v_baxis.LinewidthValidator()
        self._validators['minorgridcolor'] = v_baxis.MinorgridcolorValidator()
        self._validators['minorgridcount'] = v_baxis.MinorgridcountValidator()
        self._validators['minorgridwidth'] = v_baxis.MinorgridwidthValidator()
        self._validators['nticks'] = v_baxis.NticksValidator()
        self._validators['range'] = v_baxis.RangeValidator()
        self._validators['rangemode'] = v_baxis.RangemodeValidator()
        self._validators['separatethousands'
                        ] = v_baxis.SeparatethousandsValidator()
        self._validators['showexponent'] = v_baxis.ShowexponentValidator()
        self._validators['showgrid'] = v_baxis.ShowgridValidator()
        self._validators['showline'] = v_baxis.ShowlineValidator()
        self._validators['showticklabels'] = v_baxis.ShowticklabelsValidator()
        self._validators['showtickprefix'] = v_baxis.ShowtickprefixValidator()
        self._validators['showticksuffix'] = v_baxis.ShowticksuffixValidator()
        self._validators['smoothing'] = v_baxis.SmoothingValidator()
        self._validators['startline'] = v_baxis.StartlineValidator()
        self._validators['startlinecolor'] = v_baxis.StartlinecolorValidator()
        self._validators['startlinewidth'] = v_baxis.StartlinewidthValidator()
        self._validators['tick0'] = v_baxis.Tick0Validator()
        self._validators['tickangle'] = v_baxis.TickangleValidator()
        self._validators['tickfont'] = v_baxis.TickfontValidator()
        self._validators['tickformat'] = v_baxis.TickformatValidator()
        self._validators['tickformatstops'
                        ] = v_baxis.TickformatstopsValidator()
        self._validators['tickmode'] = v_baxis.TickmodeValidator()
        self._validators['tickprefix'] = v_baxis.TickprefixValidator()
        self._validators['ticksuffix'] = v_baxis.TicksuffixValidator()
        self._validators['ticktext'] = v_baxis.TicktextValidator()
        self._validators['ticktextsrc'] = v_baxis.TicktextsrcValidator()
        self._validators['tickvals'] = v_baxis.TickvalsValidator()
        self._validators['tickvalssrc'] = v_baxis.TickvalssrcValidator()
        self._validators['title'] = v_baxis.TitleValidator()
        self._validators['titlefont'] = v_baxis.TitlefontValidator()
        self._validators['titleoffset'] = v_baxis.TitleoffsetValidator()
        self._validators['type'] = v_baxis.TypeValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('arraydtick', None)
        self.arraydtick = arraydtick if arraydtick is not None else _v
        _v = arg.pop('arraytick0', None)
        self.arraytick0 = arraytick0 if arraytick0 is not None else _v
        _v = arg.pop('autorange', None)
        self.autorange = autorange if autorange is not None else _v
        _v = arg.pop('categoryarray', None)
        self.categoryarray = categoryarray if categoryarray is not None else _v
        _v = arg.pop('categoryarraysrc', None)
        self.categoryarraysrc = categoryarraysrc if categoryarraysrc is not None else _v
        _v = arg.pop('categoryorder', None)
        self.categoryorder = categoryorder if categoryorder is not None else _v
        _v = arg.pop('cheatertype', None)
        self.cheatertype = cheatertype if cheatertype is not None else _v
        _v = arg.pop('color', None)
        self.color = color if color is not None else _v
        _v = arg.pop('dtick', None)
        self.dtick = dtick if dtick is not None else _v
        _v = arg.pop('endline', None)
        self.endline = endline if endline is not None else _v
        _v = arg.pop('endlinecolor', None)
        self.endlinecolor = endlinecolor if endlinecolor is not None else _v
        _v = arg.pop('endlinewidth', None)
        self.endlinewidth = endlinewidth if endlinewidth is not None else _v
        _v = arg.pop('exponentformat', None)
        self.exponentformat = exponentformat if exponentformat is not None else _v
        _v = arg.pop('fixedrange', None)
        self.fixedrange = fixedrange if fixedrange is not None else _v
        _v = arg.pop('gridcolor', None)
        self.gridcolor = gridcolor if gridcolor is not None else _v
        _v = arg.pop('gridwidth', None)
        self.gridwidth = gridwidth if gridwidth is not None else _v
        _v = arg.pop('labelpadding', None)
        self.labelpadding = labelpadding if labelpadding is not None else _v
        _v = arg.pop('labelprefix', None)
        self.labelprefix = labelprefix if labelprefix is not None else _v
        _v = arg.pop('labelsuffix', None)
        self.labelsuffix = labelsuffix if labelsuffix is not None else _v
        _v = arg.pop('linecolor', None)
        self.linecolor = linecolor if linecolor is not None else _v
        _v = arg.pop('linewidth', None)
        self.linewidth = linewidth if linewidth is not None else _v
        _v = arg.pop('minorgridcolor', None)
        self.minorgridcolor = minorgridcolor if minorgridcolor is not None else _v
        _v = arg.pop('minorgridcount', None)
        self.minorgridcount = minorgridcount if minorgridcount is not None else _v
        _v = arg.pop('minorgridwidth', None)
        self.minorgridwidth = minorgridwidth if minorgridwidth is not None else _v
        _v = arg.pop('nticks', None)
        self.nticks = nticks if nticks is not None else _v
        _v = arg.pop('range', None)
        self.range = range if range is not None else _v
        _v = arg.pop('rangemode', None)
        self.rangemode = rangemode if rangemode is not None else _v
        _v = arg.pop('separatethousands', None)
        self.separatethousands = separatethousands if separatethousands is not None else _v
        _v = arg.pop('showexponent', None)
        self.showexponent = showexponent if showexponent is not None else _v
        _v = arg.pop('showgrid', None)
        self.showgrid = showgrid if showgrid is not None else _v
        _v = arg.pop('showline', None)
        self.showline = showline if showline is not None else _v
        _v = arg.pop('showticklabels', None)
        self.showticklabels = showticklabels if showticklabels is not None else _v
        _v = arg.pop('showtickprefix', None)
        self.showtickprefix = showtickprefix if showtickprefix is not None else _v
        _v = arg.pop('showticksuffix', None)
        self.showticksuffix = showticksuffix if showticksuffix is not None else _v
        _v = arg.pop('smoothing', None)
        self.smoothing = smoothing if smoothing is not None else _v
        _v = arg.pop('startline', None)
        self.startline = startline if startline is not None else _v
        _v = arg.pop('startlinecolor', None)
        self.startlinecolor = startlinecolor if startlinecolor is not None else _v
        _v = arg.pop('startlinewidth', None)
        self.startlinewidth = startlinewidth if startlinewidth is not None else _v
        _v = arg.pop('tick0', None)
        self.tick0 = tick0 if tick0 is not None else _v
        _v = arg.pop('tickangle', None)
        self.tickangle = tickangle if tickangle is not None else _v
        _v = arg.pop('tickfont', None)
        self.tickfont = tickfont if tickfont is not None else _v
        _v = arg.pop('tickformat', None)
        self.tickformat = tickformat if tickformat is not None else _v
        _v = arg.pop('tickformatstops', None)
        self.tickformatstops = tickformatstops if tickformatstops is not None else _v
        _v = arg.pop('tickmode', None)
        self.tickmode = tickmode if tickmode is not None else _v
        _v = arg.pop('tickprefix', None)
        self.tickprefix = tickprefix if tickprefix is not None else _v
        _v = arg.pop('ticksuffix', None)
        self.ticksuffix = ticksuffix if ticksuffix is not None else _v
        _v = arg.pop('ticktext', None)
        self.ticktext = ticktext if ticktext is not None else _v
        _v = arg.pop('ticktextsrc', None)
        self.ticktextsrc = ticktextsrc if ticktextsrc is not None else _v
        _v = arg.pop('tickvals', None)
        self.tickvals = tickvals if tickvals is not None else _v
        _v = arg.pop('tickvalssrc', None)
        self.tickvalssrc = tickvalssrc if tickvalssrc is not None else _v
        _v = arg.pop('title', None)
        self.title = title if title is not None else _v
        _v = arg.pop('titlefont', None)
        self.titlefont = titlefont if titlefont is not None else _v
        _v = arg.pop('titleoffset', None)
        self.titleoffset = titleoffset if titleoffset is not None else _v
        _v = arg.pop('type', None)
        self.type = type if type is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))