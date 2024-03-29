from setuptools import setup
import os   # launch脚本识别所必需的导入
from glob import glob # launch脚本的识别所必需的引入
package_name = 'sites'

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
    maintainer='vehshanaan',
    maintainer_email='1959180242@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "timer = sites.stdma_timer:main",
            "map = sites.map:main",
            "channel_visualiser = sites.channel_visualiser:main",
            "talker = sites.stdma_talker:main",
        ],
    },
)
