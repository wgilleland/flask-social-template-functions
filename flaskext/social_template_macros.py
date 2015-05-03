# -*- coding: utf-8 -*-
"""
    flaskext.social_template_macros
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Description of the module goes here...

    :copyright: (c) 2015 by Deathnerd.
    :license: MIT, see LICENSE for more details.
"""


from flask import Markup


class SocialButtons(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        if hasattr(app, 'teardown_appcontext'):
            self.app.teardown_appcontext(self.teardown)
        else:
            self.app.teardown_request(self.teardown)

        self.app.template_global('facebook_button_javascript')(self._facebook_button_javascript)
        self.app.template_global('facebook_button')(self._facebook_button)

    def _facebook_button_javascript(self):
        return Markup(u'''
            <div id="fb-root"></div>
            <script>(function(d, s, id) {{
              var js, fjs = d.getElementsByTagName(s)[0];
              if (d.getElementById(id)) return;
              js = d.createElement(s); js.id = id;
              js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.3&appId={app_id}";
              fjs.parentNode.insertBefore(js, fjs);
            }}(document, 'script', 'facebook-jssdk'));</script>
        '''.format(app_id=self.app.config.get('FB_APP_ID')))

    def _facebook_button(self):
        facebook_href = self.app.config.get('FB_HREF', 'https://developers.facebook.com/docs/plugins/')
        facebook_button_class = self.app.config.get('FB_BUTTON_CLASS', 'fb-like')
        facebook_button_layout = self.app.config.get('FB_BUTTON_LAYOUT', 'button_count')
        facebook_button_action = self.app.config.get('FB_BUTTON_ACTION', 'like')
        facebook_button_show_faces = self.app.config.get('FB_BUTTON_SHOW_FACES', True)
        facebook_button_share = self.app.config.get('FB_BUTTON_SHARE', 'True')
        return Markup(u'''
                        <div
                        class={fb_class}
                        data-href="{fb_href}"
                        data-layout="{fb_layout}"
                        data-action="{fb_action}"
                        data-show-faces="{fb_faces}"
                        data-share="{fb_share}"></div>
        ''').format(fb_href=facebook_href,
                                   fb_class=facebook_button_class,
                                   fb_layout=facebook_button_layout,
                                   fb_action=facebook_button_action,
                                   fb_faces=facebook_button_show_faces,
                                   fb_share=facebook_button_share)

    def teardown(self, exception):
        pass