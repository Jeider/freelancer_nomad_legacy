"""Lossless support for authored THN fields absent from convenience templates.

Only the explicitly supported event schemas are accepted. No Lua execution,
opaque source strings, or fallback that silently discards events.
"""
import json
import re
import copy
from types import MethodType
from story.cutscenes.content import Event, Character, LookAtCamera, StaticCamera, Ship, Prop, Light, Sound, SpatialSound, Alchemy, MotionPath, Marker

SYMBOL_FIELDS = {'type','flags','up','front','target_type','on'}
SYMBOLS = set('COMPOUND DEFORMABLE CAMERA LIGHT SOUND PSYS MOTION_PATH MARKER ROOT PART HARDPOINT Y N L_DIRECT L_POINT L_SPOT HIDDEN LIT_DYNAMIC LIT_AMBIENT SPATIAL LOOP LOOK_AT POSITION ORIENTATION ENTITY_RELATIVE ORIENTATION_RELATIVE REFERENCE X_AXIS Y_AXIS Z_AXIS NEG_X_AXIS NEG_Y_AXIS NEG_Z_AXIS'.split())

def lua(value, key=None):
    if isinstance(value, dict):
        return '{'+', '.join(f'{k}={lua(v,k)}' for k,v in value.items())+'}'
    if isinstance(value,(list,tuple)):
        return '{'+', '.join(lua(v,'axisrot' if key=='axisrot' else None) for v in value)+'}'
    if isinstance(value,str):
        if key in SYMBOL_FIELDS or key=='axisrot':
            parts=value.replace(' ','').split('+')
            if not all(p in SYMBOLS for p in parts): raise ValueError(('Unknown THN symbol',key,value))
            return '+'.join(parts)
        return json.dumps(value,ensure_ascii=True)
    if value is None: return 'nil'
    if isinstance(value,bool): return 'Y' if value else 'N'
    return repr(value)

class SourceEvent(Event):
    KIND = None
    FIELDS = set()
    def __init__(self, targets, root, group='main', time_delay=0, **properties):
        unexpected=set(properties)-self.FIELDS
        if unexpected: raise ValueError((self.KIND, 'Unsupported properties',unexpected))
        self.targets=targets
        self.properties=properties
        super().__init__(root=root,group=group,time_delay=time_delay)
    def get_thorn(self,time):
        return '{'+repr(time)+', '+self.KIND+', '+lua(self.targets)+', '+lua(self.properties)+'}'

class SourceAttachEvent(SourceEvent):
    KIND='ATTACH_ENTITY'
    FIELDS=set('duration flags target_type target_part front up offset'.split())

class SourceSpatialEvent(SourceEvent):
    KIND='START_SPATIAL_PROP_ANIM'
    FIELDS=set('duration target_type target_part spatialprops param_curve pcurve_period'.split())

class SourcePathEvent(SourceEvent):
    KIND='START_PATH_ANIMATION'
    FIELDS=set('duration flags front up offset start_percent stop_percent param_curve pcurve_period'.split())

class SourceAlchemyAnimEvent(SourceEvent):
    KIND='START_PSYS_PROP_ANIM'
    FIELDS=set('duration psysprops param_curve pcurve_period'.split())

class SourceMotionEvent(SourceEvent):
    KIND='START_MOTION'
    FIELDS=set('duration animation time_scale start_time trans_time trans_scale weight heading event_flags'.split())

def preserve_entity(entity, fields=None, **extra):
    """Retain only extra THN metadata; constructor parameters remain editable.

    Standard properties always come from the live object. Source-only fields
    (model override, actor binding, aspect ratio, specular, etc.) are explicit.
    """
    fields=dict(fields or {},**extra)
    entity.source_fields=fields
    def render(self):
        if isinstance(self,Character): typ='DEFORMABLE'
        elif isinstance(self,(LookAtCamera,StaticCamera)): typ='CAMERA'
        elif isinstance(self,Prop): typ='COMPOUND'
        elif isinstance(self,Light): typ='LIGHT'
        elif isinstance(self,Sound): typ='SOUND'
        elif isinstance(self,Alchemy): typ='PSYS'
        elif isinstance(self,MotionPath): typ='MOTION_PATH'
        elif isinstance(self,Marker): typ='MARKER'
        else: raise TypeError(type(self))
        table=dict(copy.deepcopy(self.source_fields),entity_name=self.name,type=typ)
        table.setdefault('template_name','')
        table.setdefault('srt_grp',getattr(self,'SRT_GRP',0))
        table.setdefault('usr_flg',getattr(self,'USR_FLG',0))
        table['lt_grp']=getattr(self,'light_group',table.get('lt_grp',0))
        if isinstance(self,(Character,Prop)):
            if table['template_name']=='': table['template_name']=self.get_compound_template_name()
            # Keep additional flags, but lighting follows the editable constructor.
            if not isinstance(table.get('flags'),(int,float)):
                flags=[f.strip() for f in str(table.get('flags','')).split('+')
                       if f.strip() and f.strip() not in ('LIT_DYNAMIC','LIT_AMBIENT')]
                table['flags']='+'.join(self.get_flags().replace(' ','').split('+')+flags)
        if isinstance(self,(LookAtCamera,StaticCamera)):
            p=table.setdefault('cameraprops',{})
            p.setdefault('hvaspect',1.85);p.setdefault('nearplane',0.2)
            p.update(fovh=self.fov,farplane=self.farplane)
            table.setdefault('flags','HIDDEN')
        if isinstance(self,Light):
            table['entity_name']=self.get_light_name()
            p=table.setdefault('lightprops',{})
            p.setdefault('specular',[0,0,0])
            p.update(on='Y' if self.on else 'N',color=self.color,diffuse=self.diffuse,
                     ambient=self.ambient,direction=self.direction,range=self.range,
                     cutoff=self.cutoff,theta=self.theta,type=self.light_type,atten=self.attenuation)
        if isinstance(self,Sound):
            table['template_name']=self.sound
            if self.FLAGS: table['flags']=self.FLAGS
            p=table.setdefault('audioprops',{})
            for k,v in dict(pan=0,ain=360,aout=360,atout=0,rmix=0).items():p.setdefault(k,v)
            p.update(attenuation=self.attenuation,dmin=self.dmin,dmax=self.dmax)
        if isinstance(self,Alchemy):
            table['template_name']=self.particles
            table.setdefault('psysprops',{})['sparam']=self.sparam
        point=getattr(self,'point',None)
        if point is not None:
            # Point.matrix_from_quat is formatted Lua; use the same quaternion
            # conversion numerically so no original spatial data masks edits.
            from story import math
            matrix=math.quat_to_matrix(point.orientation)
            if hasattr(self,'source_basis'):
                import numpy as np
                initial=math.quat_to_matrix(self.reference_orientation)
                matrix=(np.asarray(matrix) @ np.linalg.inv(initial) @ np.asarray(self.source_basis)).tolist()
            table['spatialprops']={'pos':point.position,'orient':matrix}
        else:
            table['spatialprops']={'pos':[0,0,0],'orient':[[1,0,0],[0,1,0],[0,0,1]]}
        if isinstance(self,Character):
            table.setdefault('template_name',self.actor.CUTSCENE_APPEARANCE)
            table.setdefault('compoundprops',{})['floor_height']=self.floor_height
            table.setdefault('userprops',{'Actor':self.actor.get_game_actor(),'category':'Character'})
        if isinstance(self,MotionPath):
            table['pathprops']={'path_type':'CV_CROrientationSplinePath','path_data':'OPEN, '+self.extract_path_data()}
        return lua(table)
    entity.get_thorn=MethodType(render,entity)
    return entity

def preserve_spatial(entity, source_basis, reference_orientation):
    """Keep scale/shear in the original THN while Blender edits rotate its basis."""
    if not hasattr(entity,'source_fields'):
        preserve_entity(entity, template_name='')
    entity.source_basis=source_basis
    entity.reference_orientation=reference_orientation

def select_dialogue(root, mission, class_name, prefix):
    """Select the actual source segment for a scene spanning mission boundaries."""
    import importlib
    if not hasattr(root,'original_props'): root.original_props=root.props
    if getattr(root,'validation_dialogue',None):
        root.props=root.validation_dialogue[prefix]
    else:
        module=importlib.import_module(f'story.scripts.main.mission{mission}')
        root.props=getattr(module,class_name)(root.original_props.mission)

def restore_dialogue(root):
    if hasattr(root,'original_props'): root.props=root.original_props
