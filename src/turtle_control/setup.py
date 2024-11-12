from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'turtle_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vipul',
    maintainer_email='vipul@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "control=turtle_control.turtle_controller:main",
        "control_p=turtle_control.turtle_controller_p:main",
        "control_pi=turtle_control.turtle_controller_pi:main",
        "control_pid=turtle_control.turtle_controller_pid:main"
        ],
    },
)