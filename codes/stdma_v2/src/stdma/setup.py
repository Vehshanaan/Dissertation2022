from setuptools import setup
import os
from glob import glob

package_name = 'stdma_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(
            os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aeagr',
    maintainer_email='arthur.richards@bristol.ac.uk',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = stdma_ros.stdma_talker:main',
                'timer = stdma_ros.stdma_timer:main',
                'channel_visualiser = stdma_ros.channel_visualiser:main',
                "map = stdma_ros.map:main",
        ],
    },
)
