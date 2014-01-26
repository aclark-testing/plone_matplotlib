from zope.publisher.browser import BrowserPage


class PloneMatPlotLib(BrowserPage):
    """
    """

    def __call__(self):

        import cStringIO
        from matplotlib.figure import Figure
        from matplotlib.backends.backend_agg import FigureCanvasAgg

        x, y = 4, 4
#        qs = parse_qs(request.query_string)
#        if 'x' in qs:
#            x = int(qs['x'][0])
#        if 'y' in qs:
#            y = int(qs['y'][0])
        fig = Figure(figsize=[x, y])
        ax = fig.add_axes([.1, .1, .8, .8])
        ax.scatter([1, 2], [3, 4])
        canvas = FigureCanvasAgg(fig)

        # write image data to a string buffer and get the PNG image bytes
        buf = cStringIO.StringIO()
        canvas.print_png(buf)
        data = buf.getvalue()

        # write image bytes back to the browser
#        response = Response(data)
#        response.content_type = 'image/png'
#        response.content_length = len(data)
#        return response

        self.request.response.setHeader("Content-type", "image/png")
        return data
