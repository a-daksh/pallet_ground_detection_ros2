from setuptools import find_packages, setup

package_name = 'yolo_inference'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='daksh',
    maintainer_email='dakshadhar1810@gmail.com',
    description='YOLO inference node for object detection and segmentation',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'yolo_node = yolo_inference.yolo_node:main',
        ],
    },
)



