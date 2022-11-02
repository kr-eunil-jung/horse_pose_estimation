dataset_info = dict(
    dataset_name='custom',
    paper_info=dict(
        author='',
        title='Animal',
        container='',
        year='2022',
        homepage='',
    ),
    keypoint_info={
        0:
        dict(name='fore_head', id=0, color=[51, 153, 255], type='upper', swap=''),
        1:
        dict(
            name='neck',
            id=1,
            color=[51, 153, 255],
            type='upper',
            swap=''),
        2:
        dict(
            name='fore_spine',
            id=2,
            color=[51, 153, 255],
            type='upper',
            swap=''),
        3:
        dict(
            name='fore_right_shoulder',
            id=3,
            color=[51, 153, 255],
            type='upper',
            swap='fore_left_shoulder'),
        4:
        dict(
            name='fore_right_knee',
            id=4,
            color=[51, 153, 255],
            type='upper',
            swap='fore_left_knee'),
        5:
        dict(
            name='fore_right_foot',
            id=5,
            color=[0, 255, 0],
            type='upper',
            swap='fore_left_foot'),
        6:
        dict(
            name='fore_left_shoulder',
            id=6,
            color=[255, 128, 0],
            type='upper',
            swap='fore_right_shoulder'),
        7:
        dict(
            name='fore_left_knee',
            id=7,
            color=[0, 255, 0],
            type='upper',
            swap='fore_right_knee'),
        8:
        dict(
            name='fore_left_foot',
            id=8,
            color=[255, 128, 0],
            type='upper',
            swap='fore_right_foot'),
        9:
        dict(
            name='rear_spine',
            id=9,
            color=[0, 255, 0],
            type='upper',
            swap=''),
        10:
        dict(
            name='rear_right_shoulder',
            id=10,
            color=[255, 128, 0],
            type='upper',
            swap='rear_left_shoulder'),
        11:
        dict(
            name='rear_right_knee',
            id=11,
            color=[0, 255, 0],
            type='lower',
            swap='rear_left_knee'),
        12:
        dict(
            name='rear_right_foot',
            id=12,
            color=[255, 128, 0],
            type='lower',
            swap='rear_left_foot'),
        13:
        dict(
            name='rear_left_shoulder',
            id=13,
            color=[0, 255, 0],
            type='lower',
            swap='rear_right_shoulder'),
        14:
        dict(
            name='rear_left_knee',
            id=14,
            color=[255, 128, 0],
            type='lower',
            swap='rear_right_knee'),
        15:
        dict(
            name='rear_left_foot',
            id=15,
            color=[0, 255, 0],
            type='lower',
            swap='rear_right_foot'),
        16:
        dict(
            name='hip',
            id=16,
            color=[255, 128, 0],
            type='lower',
            swap='')
    },
    skeleton_info={
        0:
        dict(link=('fore_head', 'neck'), id=0, color=[0, 255, 0]),
        1:
        dict(link=('neck', 'fore_spine'), id=1, color=[0, 255, 0]),
        2:
        dict(link=('fore_spine', 'fore_right_shoulder'), id=2, color=[0, 255, 0]),
        3:
        dict(link=('fore_right_shoulder', 'fore_right_knee'), id=3, color=[0, 255, 0]),
        4:
        dict(link=('fore_right_knee', 'fore_right_foot'), id=4, color=[0, 255, 0]),
        5:
        dict(link=('fore_spine', 'fore_left_shoulder'), id=5, color=[0, 255, 0]),
        6:
        dict(link=('fore_left_shoulder', 'fore_left_knee'), id=6, color=[0, 255, 0]),
        7:
        dict(
            link=('fore_left_knee', 'fore_left_foot'),
            id=7,
            color=[0, 255, 0]),
        8:
        dict(link=('fore_spine', 'rear_spine'), id=8, color=[0, 255, 0]),
        9:
        dict(
            link=('rear_spine', 'rear_right_shoulder'), id=9, color=[0, 255, 0]),
        10:
        dict(link=('rear_right_shoulder', 'rear_right_knee'), id=10, color=[0, 255, 0]),
        11:
        dict(link=('rear_right_knee', 'rear_right_foot'), id=11, color=[0, 255, 0]),
        12:
        dict(link=('rear_spine', 'rear_left_shoulder'), id=12, color=[0, 255, 0]),
        13:
        dict(link=('rear_left_shoulder', 'rear_left_knee'), id=13, color=[0, 255, 0]),
        14:
        dict(link=('rear_left_knee', 'rear_left_foot'), id=14, color=[0, 255, 0]),
        15:
        dict(link=('rear_spine', 'hip'), id=15, color=[0, 255, 0])
    },
    joint_weights=[
        1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1.,
        1., 1.
    ],
    sigmas=[
        0.05, 0.05, 0.05, 0.05, 0.05,
        0.05, 0.05, 0.05, 0.05, 0.05,
        0.05, 0.05, 0.05, 0.05, 0.05,
        0.05, 0.05
    ])
