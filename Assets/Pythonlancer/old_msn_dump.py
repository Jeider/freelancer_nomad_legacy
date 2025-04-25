from story.actors import ActorManager


MSN = ''
RU_STRING = ''
EN_STRING = ''



LINE_TPL = """VoiceLine(
    {line},
    {actor},
    ru="{ru}",
    en="{en}",
),"""


manager = ActorManager()


class Comm:
    def __init__(self, string_id, line):
        self.string_id = string_id
        self.line = line
        self.ru = None
        self.en = None

    def set_ru(self, ru):
        self.ru = ru

    def set_en(self, en):
        self.en = en

    def get_ru(self):
        return self.ru.split(r'\n')[1]

    def get_en(self):
        return self.en.split(r'\n')[1]

    def get_index(self):
        return int(self.line.split('_')[2])

    def get_actor_name(self):
        return self.line.split('_')[3]

    def get_actor(self):
        return manager.get_by_name(self.get_actor_name()).__name__


comms = {}

for line in MSN.splitlines():
    split = line.split('=')
    if len(split) < 2:
        continue

    if split[0].strip() == 'Act_EtherComm':
        comm_split = split[1].strip().split(',')

        string_id = int(comm_split[1])
        comms[string_id] = Comm(string_id, comm_split[3].strip())


break_items = 3

keys = comms.keys()

last_index = None
break_count = 0
for line in RU_STRING.splitlines():
    if break_count == 0:
        last_index = int(line)

    if break_count == 2:
        if last_index in keys:
            comms[last_index].set_ru(line)

    break_count += 1
    if break_count == break_items:
        break_count = 0


last_index = None
break_count = 0
for line in EN_STRING.splitlines():
    if break_count == 0:
        last_index = int(line.strip())

    if break_count == 2:
        if last_index in keys:
            comms[last_index].set_en(line)

    break_count += 1
    if break_count == break_items:
        break_count = 0


for comm in comms.values():
    msg = LINE_TPL.format(
        line=comm.get_index(),
        actor=comm.get_actor(),
        ru=comm.get_ru(),
        en=comm.get_en(),
    )
    print(msg)







#
# for line in MSN.splitlines():
#     items = line.split('	')
#     index = int(items[0].split('_')[2])
#     actor_name = items[0].split('_')[3]
#     ru = items[5].split(r'\n')[1]
#     en = items[4].split(r'\n')[1]
#
#     msg = LINE_TPL.format(
#         line=index,
#         actor=manager.get_by_name(actor_name).__name__,
#         ru=ru,
#         en=en,
#     )
#     print(msg)
#
#

