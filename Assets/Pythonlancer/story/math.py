from scipy.spatial.transform import Rotation as R


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
    r = R.from_quat(quaternion)
    return r.as_matrix().tolist()
