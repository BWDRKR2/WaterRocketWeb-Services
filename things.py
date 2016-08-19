import falcon


class Reset(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Dan Immanuel Kant\n\n')


app = falcon.API()

reset = Reset()

app.add_route('/things', reset)
app.add_route('/reset', reset)
app.add_route('/arm', reset)
app.add_route('/unarm', reset)
app.add_route('/begin_fuel', reset)
app.add_route('/end_fuel', reset)
app.add_route('/abort', reset)
app.add_route('/launch', reset)
