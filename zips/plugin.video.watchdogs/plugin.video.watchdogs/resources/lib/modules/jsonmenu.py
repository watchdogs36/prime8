
import json
import os
import traceback

from resources.lib.modules import client, control, log_utils


class jsonMenu(object):
    def __init__(self):
        # Default root locations, if none is set by the indexer
        self.local_root = os.path.join(control.addonPath, 'menu')
        self.menu = None

        self.agent = 'QXRyZWlkZXMgSlNPTiBNZW51x'[1:].decode('base64')

    def load(self, menu_file):
        if 'http' in menu_file:
            try:
                header = {'User-Agent': self.agent}
                response = client.request(menu_file, headers=header)
                self.menu = json.loads(response)
            except Exception:
                failure = traceback.format_exc()
                log_utils.log('jsonMenu - Open Remote Exception: \n' + str(failure))
        else:
            try:
                menu_file = os.path.join(self.local_root, menu_file)
                fileref = control.openFile(menu_file)
                content = fileref.read()
                fileref.close()
                self.menu = json.loads(content)
            except Exception:
                failure = traceback.format_exc()
                log_utils.log('jsonMenu - Open Local Exception: \n' + str(failure))
