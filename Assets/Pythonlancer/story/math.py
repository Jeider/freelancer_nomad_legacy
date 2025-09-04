from scipy.spatial.transform import Rotation as R
import math


def radians_to_degrees(x, y, z):
    return [
        math.degrees(x),
        math.degrees(y),
        math.degrees(z)
    ]


def euler_to_quat(x, y, z):
    r = R.from_euler('xyz', [x, y, z], degrees=True)
    quat = r.as_quat().tolist()
    return [
        quat[3],  # weight should be first
        quat[0],
        quat[1],
        quat[2],
    ]


def euler_to_matrix(x, y, z):
    r = R.from_euler('xyz', [x, y, z], degrees=True)
    return r.as_matrix().tolist()


def quat_to_matrix(quaternion):
    if len(quaternion) != 4:
        raise Exception('Failed: income value is not quaternion')
    r = R.from_quat([
        quaternion[1],
        quaternion[2],
        quaternion[3],
        quaternion[0],
    ])
    return r.as_matrix().tolist()


def quat_to_euler(quaternion):
    if len(quaternion) != 4:
        raise Exception('Failed: income value is not quaternion')
    r = R.from_quat(quaternion)
    return r.as_euler().tolist()


def convert_quat_from_blender_to_fl(quaternion):
    if len(quaternion) != 4:
        raise Exception('Failed: income value is not quaternion')
    return [
        quaternion[0],
        -quaternion[1],
        -quaternion[2],
        -quaternion[3],
    ]
