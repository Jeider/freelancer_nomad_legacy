"""Shortest routes through authored TradeConnections and jumpgate links."""
from collections import deque


def paths_from(root,jumpgate_type,excluded,minimize_jumps=False):
    paths={root:[]};costs={root:0};pending=deque([root])
    while pending:
        obj=pending.popleft();edges=[]
        for connection in obj.connections:
            ends=connection.get_destination_objects()
            # ATTACKED_BY patrol origins are not a traversable tradelane.
            if obj in ends:
                edges.extend((other,'tradelane') for other in ends if other is not obj)
        if isinstance(obj,jumpgate_type):
            try:
                target=obj.get_target_jumpgate()
                if target.system.SCAN_JUMP:edges.append((target,'jumpgate'))
            except KeyError as error:
                excluded.add((obj.system.NAME+':'+obj.get_full_alias(),str(error)))
        for target,kind in edges:
            cost=int(kind=='jumpgate') if minimize_jumps else 1
            total=costs[obj]+cost
            if target in costs and costs[target]<=total:continue
            step={'kind':kind,'from':obj.system.NAME+':'+obj.get_full_alias(),
                  'to':target.system.NAME+':'+target.get_full_alias()}
            paths[target]=paths[obj]+[step];costs[target]=total
            if cost:pending.append(target)
            else:pending.appendleft(target)
    return paths
