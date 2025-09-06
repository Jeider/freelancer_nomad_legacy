from scipy.spatial.transform import Rotation as R
import math
import numpy as np



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


def rotate_point_around_pivot(point, pivot, angle_degrees):
    translated_point = point - pivot

    # 2. Perform rotation
    # Create a 2D rotation in the XY plane (around the Z-axis)
    rotation = R.from_euler('z', angle_degrees, degrees=True)
    rotated_translated_point = rotation.apply(np.append(translated_point, 0))[:2] # Apply and remove Z-component

    # 3. Translate back
    rotated_point = rotated_translated_point + pivot

    return rotated_point


def relocate_point(point, rotate_y, pivot=None):
    if len(point) != 3:
        raise Exception('Point should have 3 indices')

    np_point = np.array([point[0], point[2]])
    np_pivot = np.array([pivot[0], pivot[1]] if pivot else [0, 0])

    rotated_point = rotate_point_around_pivot(np_point, np_pivot, rotate_y)

    return [rotated_point[0], point[1], rotated_point[1]]


def rotate_point(xyz, rotate_core):
    if len(xyz) != 3:
        raise Exception('xyz should have 3 indices')
    point_rot = R.from_euler('xyz', [xyz[0], xyz[1], xyz[2]], degrees=True)
    new_rot = R.from_euler('zyx', [0, rotate_core, 0], degrees=True)

    final_rot = point_rot * new_rot

    return final_rot.as_euler('xyz', degrees=True)
