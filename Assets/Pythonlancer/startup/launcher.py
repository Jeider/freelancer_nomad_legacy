import os
import webview

"""
An example of serverless app architecture
"""


class Api:
    def demo(self, variable):
        print('Turned %s' % variable)

    def test(self):
        print('test')


if __name__ == '__main__':
    api = Api()
    webview.create_window('NL Launcher', 'launcher_content/launcher.html', js_api=api, width=770, height=750)
    # webview.create_window('NL Launcher', 'https://freelancer2.space', width=770, height=750)
    webview.start()
