# Open3D: www.open3d.org
# The MIT License (MIT)
# See license file or visit www.open3d.org for details

import copy
import numpy as np
from open3d import *

if __name__ == "__main__":

    # generate some neat n times 3 matrix using a variant of sync function
    x = np.linspace(-3, 3, 401)
    mesh_x, mesh_y = np.meshgrid(x,x)
    z = np.sinc((np.power(mesh_x,2)+np.power(mesh_y,2)))
    z_norm = (z-z.min())/(z.max()-z.min())
    xyz = np.zeros((np.size(mesh_x),3))
    xyz[:,0] = np.reshape(mesh_x,-1)
    xyz[:,1] = np.reshape(mesh_y,-1)
    xyz[:,2] = np.reshape(z_norm,-1)
    print('xyz')
    print(xyz)

    # Pass xyz to Open3D.PointCloud and visualize
    pcd = PointCloud()
    pcd.points = Vector3dVector(xyz)
    write_point_cloud("../../TestData/sync.ply", pcd)

    # Load saved point cloud and visualize it
    pcd_load = read_point_cloud("../../TestData/sync.ply")
    draw_geometries([pcd_load])

    # convert Open3D.PointCloud to numpy array
    xyz_load = np.asarray(pcd_load.points)
    print('xyz_load')
    print(xyz_load)

    # save z_norm as an image (change [0,1] range to [0,255] range with uint8 type)
    img = Image((z_norm*255).astype(np.uint8))
    write_image("../../TestData/sync.png", img)
    draw_geometries([img])
