# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

#pubsub
zmq_pub_drone_fdm=('127.0.0.1',5566)
#zmq_pub_drone_fdm=('127.0.0.1',12466)
topic_sitl_position_report=b'position_rep'

zmq_pub_unreal_proxy=('127.0.0.1',5577)
topic_unreal_state=b'unreal_state'
topic_unreal_drone_rgb_camera=b'rgb_camera_%d'

zmq_pub_comp_vis = 8877 #only port
topic_comp_vis = b'comp_vis'

n_drones = 1


zmq_pub_joy=9117
topic_button = b'topic_button'
topic_axes = b'topic_axes'


