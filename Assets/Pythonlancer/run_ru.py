# from screeninfo import get_monitors
# for m in get_monitors():
#     print(str(m))

from startup.meta import ScreenMeta
from startup.config import StartupConfig
from managers.jinja_manager import JinjaTemplateManager
from managers.options import OptionsManager

meta = ScreenMeta()
config = StartupConfig(screen_meta=meta, resolution=[1280, 1024])
manager = OptionsManager(tpl_manager=JinjaTemplateManager(), config=config)
manager.sync_data()


